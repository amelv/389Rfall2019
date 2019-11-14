#!/usr/bin/env python2

import sys
import struct
import time
from datetime import datetime


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))


# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

timestamp, temp = struct.unpack("<LL", data[8:16])

author1, author2 = struct.unpack("<LL", data[12:20])

count, temp2 = struct.unpack("<LL", data[20:28])


if (hex(timestamp) < hex(0x00000000) or hex(timestamp) > hex(0xffffffff)):
	bork("Bad timestamp! %s is not a valid utc timestamp" % (hex(timestamp)))


if (is_ascii(str(author1)) is False or is_ascii(str(author2)) is False):
	bork("Bad author! %s is not ascii-encoded" % (hex(author))) #might need to check for null bytes

if (hex(count) <= 0):
	bork("Bad version number! %s is less than 0" % (hex(version)))

author = hex(author1)[2:].decode("hex")[::-1] + "" + hex(author2)[2:].decode("hex")[::-1]


print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % datetime.utcfromtimestamp(timestamp))
print("AUTHOR: %s" % (author))
print("COUNT: %d" % int(count))

print("-------  BODY  -------")

