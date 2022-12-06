import itertools
import sys

with open('prob.txt') as f:
    sys.stdout.writelines(itertools.islice(f, 1, None, 2))