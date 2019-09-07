#!/usr/bin/env python

import argparse
import sys

import pandas

from pickem.data_normalizer import get_normed_data

def main():
    ap = argparse.ArgumentParser(description='Parse input game stats and output rank orderd picks')
    ap.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    ap.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)

    args = ap.parse_args()
    data = get_normed_data(args.infile)
    if not data:
        return -1

    header = data[0].split(',')
    df = pandas.DataFrame.from_records(data[1:], columns=header)
    games = df.groupby(by=header[:4])
    df.to_csv(args.outfile)
    return 0


if __name__ == '__main__':
    sys.exit(main())
