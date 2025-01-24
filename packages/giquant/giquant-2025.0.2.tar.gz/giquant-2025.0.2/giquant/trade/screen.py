import re
import sys
import duckdb
import warnings
import argparse

import numpy as np
import pandas as pd

def get_col(con_, cols_, ticker_, max_years_):
  sql = f"select year,{cols_} from {REPORTS} where yahoo=='{ticker_}' order by year desc limit {max_years_};"
  df = con_.sql(sql).df()
  return df

def calc_kpi(df_, col_, years_list):
  coll = f'{col_}l'
  colg = f'{col_}g'
  res = {}
  df_ = df_.sort_index(ascending=False)
  df_[coll] = df_[col_].shift(1)
  df_[colg] = df_[col_] / df_[coll]
  df_ = df_.dropna()
  df_ = df_.sort_index(ascending=True)
  for years in years_list.split(','):
    years = int(years)
    res.update( { f'{col_}_last'         : df_.head(1)[col_].mean(),
            f'{col_}_growth_mean{years}' : df_.head(years)[colg].mean(),
            f'{col_}_growth_std{years}'  : df_.head(years)[colg].std(),
            f'{col_}_mean{years}'        : df_.head(years)[col_].mean(),
            f'{col_}_std{years}'         : df_.head(years)[col_].std(),
            f'{col_}_min{years}'         : df_.head(years)[col_].min(),
            f'{col_}_max{years}'         : df_.head(years)[col_].min()
            } )
  return res

# mean() handles NaN ok!
def get_col_last(con_, col_, ticker_):
  df = get_col(con_, col_, ticker_, 1)
  return df[col_].mean()

def calc_exprs(df_, exprs_):
  cols = []
  if not exprs_ is None:
    for expr in  exprs_.split(';'):
      t,e = expr.split('=')
      cols.append(t)
      if e.startswith('mean'):
        args = e.removeprefix('mean(').removesuffix(')').split(',')
        df_[t] = df_.apply(lambda x: np.mean(x[args]), axis=1)
      else:
        terms = re.split(r'([+\-*/])', e)
        if terms[1]=='+':
          df_[t] = df_[terms[0]] + df_[terms[2]]
        elif terms[1]=='-':
          df_[t] = df_[terms[0]] - df_[terms[2]]
        elif terms[1]=='*':
          df_[t] = df_[terms[0]] * df_[terms[2]]
        elif terms[1]=='/':
          df_[t] = df_[terms[0]] / df_[terms[2]]
        else:
          print(f'Unknown operator {terms[1]}')
          sys.exit(1)
  return df_,cols
        
def calc(con_, args):
  price = pd.read_csv(f'{args.folder}/bdlast_ticker.csv')
  sql = f"select distinct(yahoo) from {REPORTS};"
  tickers = con_.sql(sql).fetchall()
  print(f'#tickers:{len(tickers)}')
  res = []
  cnt = 0
  max_years = max(map(lambda x: int(x), args.years.split(',')))+1
  for ticker in tickers:
    if cnt%1000==0:
      print(f'{cnt}...', end='', flush=True)
    cnt += 1
    ticker = ticker[0]
    row = {'ticker' : ticker}
    df = get_col(con_, args.cols, ticker, max_years)
    for col in args.cols.split(','):
      row.update(calc_kpi(df, col, args.years))

    if not args.last is None:
      for col in args.last.split(','):
        row.update({ col : get_col_last(con_, col, ticker) } )

    row.update({ 'Close' : price.loc[price.yahoo==ticker,'Close'].mean() } )
    df['Close'] = row['Close']
    
    if not args.expr is None:
      df,cols = calc_exprs(df, args.expr)
      for col in cols:
        row.update(calc_kpi(df, col, args.years))
    
    res.append(row)
    
  res = pd.DataFrame(res)
  path_ = f'{args.folder}/{args.file}.csv'
  res.to_csv(path_, index=False)
  print('\n',res)
  return res

def filter_df(df_, exprs):
  for e in exprs.split(';'):
    terms = re.split(r'([><])', e)
    if terms[1]=='<':
      df_ = df_.loc[df_[terms[0]]<float(terms[2]),:]
    elif terms[1]=='>':
      df_ = df_.loc[df_[terms[0]]>float(terms[2]),:]
    else:
      print(f'ERROR: Unknown filter operator {terms[1]}')
      sys.exit(1)
  return df_

def show(args):
  df = pd.read_csv(f'{args.folder}/{args.file}.csv')
  print(df.columns)
  
  df.replace([np.inf, -np.inf], np.nan, inplace=True)
  df = df.dropna()
  df,cols = calc_exprs(df, args.expr)

  if not args.filter is None:
    df = filter_df(df, args.filter)
  
  if not args.sort_by is None:
    df = df.sort_values(args.sort_by, ascending=args.sort_asc)
  df = df.head(100)
  
  print(df)
  if not args.outfile is None:
    path_ = f'{args.folder}/{args.outfile}.csv'
    df.to_csv(path_)
    print(f'Save result in {path_}')
    
  
desc_ = 'Screen using fundamental data'
def create_args_parser():
  parser = argparse.ArgumentParser(prog='screen.py', description=desc_)
  parser.add_argument('action',            help='What to do', choices=['calc','show'])
  parser.add_argument('folder',            help='Folder with Börsdata files')
  parser.add_argument('file',              help='Name of file for the screen')
  parser.add_argument('outfile',           help='Save result in a csv-file. Used by show.')
  parser.add_argument('--cols',            help='Börsdata columns to use. Comma separated list. Latest closing price is automatically added using bdlast_ticker.csv.')
  parser.add_argument('--last',            help='Börsdata columns to get most recent value for. Comma separated list.')
  parser.add_argument('--expr',            help='Expression of two columns. Z=X+Y|Z=X-Y|Z=X*Y|Z=X/Y. Semi-colon separated list, eg. Z=X+Y;Z=V/W.')
  parser.add_argument('--years',           help='Number of years of history to use. Comma separated list.', default='3,5,7')
  parser.add_argument('--filter',          help='Filter result. X>0;Y<10.')
  parser.add_argument('--sort_by',         help='Columns to sort result by')
  parser.add_argument('--sort_asc',        help='Sort result ascending. default=False', action=argparse.BooleanOptionalAction, default=False)
  parser.add_argument('--dbname',          help='Name of DuckDb database', default='borsdata.duckdb')
  return parser

def main(args):
  global REPORTS
  REPORTS = args.file

  con = duckdb.connect(f'{args.folder}/{args.dbname}')
  if args.action=='calc':
    if args.cols is None:
      print('--cols is mandatory')
      sys.exit(1)
    calc(con, args)
  elif args.action=='show':
    show(args)
  else:
    print(f'ERROR: Unknown action {args.action}')
  con.close()
  
if __name__ == '__main__':
  parser = create_args_parser()
  args = parser.parse_args()
  print(args)
  with warnings.catch_warnings(action="ignore"):
    main(args)


