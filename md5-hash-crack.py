
#!/usr/python3
# https://www.tutorialspoint.com/md5-hash-encoding-using-python

import hashlib
from itertools import permutations
import sys

chars = "abcdefghijklmnopqrstuvwxyz"
# chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"\#\$%&\\'()*+,-./:;<=>?@"
size = 5

def usage():
    print("Usage: {} <msg> <name>".format(sys.argv[0]))

if __name__ == '__main__':
    if not sys.argv[1:]:
        usage()
        sys.exit(0)

    hashfile = sys.argv[1]

    output = open("passwords.txt", "w+")
    # Create dict - key = permutation; value = hash of perm
    pswdhsh = {}
    tries = map("".join, permutations(chars, size))
    for x in tries:
        trieshash = hashlib.md5(x.encode()).hexdigest()
        pswdhsh[x] = trieshash


    # Compare hashes in file to dict
    with open(hashfile, 'r') as hashes:
        # hashes.strip('\n')
        for k, v in pswdhsh.items():
            if(v in hashes):
                passwords.write(k + "\r")

    output.close()

    # print(x)
    # print(hash.strip('\n'), "TEST", hshtest.hexdigest())
    # hash.strip('\n').intersection(hshtest.hexdigest()):



    # with open(hashfile, 'r') as hashes:
    #     for hash in hashes:
    #         x = 0
    #         while(x == 0):
    #             for x in perm(chars, size):
    #                 hshtest = hashlib.md5(x.encode())
    #                 print(x)
    #                 print(hash.strip('\n'), "TEST", hshtest.hexdigest())
    #                 if(hash.strip('\n') == hshtest.hexdigest()):
    #                     passwords.write(rndmtest + "\r")
    #                     x = 1





# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#
# $%&\'()*+,-./:;<=>?@
#
# import hashlib
#
# user_entered_password = 'pa$$w0rd'
# salt = "5gz"
# db_password = user_entered_password+salt
# h = hashlib.md5(db_password.encode())
# print(h.hexdigest())
