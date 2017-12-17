#!/usr/bin/env python
import sys
import slate
# Must remember to read as binary file
with open(sys.argv[1], 'rb') as f:
    doc = slate.PDF(f)
print(sys.argv[2])
