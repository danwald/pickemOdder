#!/usr/bin/env python

from pkg_resources import resource_string
import argparse
import sys

from pickem.data_normalizer import get_normed_data

def main():
    ap = argparse.ArgumentParser(description='Parse input game stats and output rank orderd picks')
    ap.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    ap.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)

    args = ap.parse_args()
    data = get_normed_data(args.infile)
    if data:
        args.outfile.write(data)
    return 0


if __name__ == '__main__':
    sys.exit(main())
