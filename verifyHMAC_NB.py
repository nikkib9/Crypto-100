#!/usr/bin/python3
#
#
#
# Take text file and validate each message with the given HMAC.  Output mismatches
#

import hmac
import sys

def gen_tag(msg, key):
    hm = hmac.new(key.encode())
    hm.update(msg.encode())
    return hm.hexdigest()

def usage():
    print("Usage: {} <msg> <name>".format(sys.argv[0]))

if __name__ == '__main__':
    if not sys.argv[2:]:
        usage()
        sys.exit(0)

    tags = sys.argv[1]
    keyfile = sys.argv[2] + '.key'

    with open(keyfile) as f:
        key = f.read()
    # with open(tags, 'r') as tag:
    #     lines = [line.rstrip('\n') for line in tags]

    output = open("mismatch.txt", "w+")

    with open(tags, 'r') as lines:
        for line in lines:
            msg, hash = line.strip('\n').split(':')

            t = gen_tag(msg, key)

            if not(hmac.compare_digest(t, hash)):
                output.write(line + "\r")

    output.close()
