#!/usr/bin/env python

import sys
from passlib.hash import sha256_crypt

if len(sys.argv) != 2:
  print "Please provide one argument: the plain-text password"
  exit()
password = sys.argv[1]

hash = sha256_crypt.encrypt(password);

print hash