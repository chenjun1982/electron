#!/usr/bin/env python

import os
import sys

from lib.util import rm_rf


SOURCE_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def main():
  os.chdir(SOURCE_ROOT)
  rm_rf('dist')
  rm_rf('out')

if __name__ == '__main__':
  sys.exit(main())
