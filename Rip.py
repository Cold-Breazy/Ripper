#!/usr/bin/env/python3

from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import os
import sys
import time


# RIPPER v1.0

os.system("clear")

if sys.version[0] in "2":
    print ("\n[x] ..n00b.. Ripper Is Not Supported For python 2.x Use Python 3.x \n")
    print ("\n\n\tRipper \033[1;91m LETS HACK TOGETHER \033[0m😃\n\n")
    exit()


class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"


banner = ("""

      ███████████████████████████████████
      █▄─▄▄▀█▄─▄█▄─▄▄─█▄─▄▄─█▄─▄▄─█▄─▄▄▀█
      ██─▄─▄██─███─▄▄▄██─▄▄▄██─▄█▀██─▄─▄█
      ▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀
""")
for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
    Author:  Breazy | Danger 404
    Github:  https://github.com/cold-breazy
    WhatsAp: https://wa.me/+27847611848\n """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n    LET THE GAME AGAINST SYSTEMS BEGIN...!\n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


try:
    data = input("\n  [+] SAVE SITES ? (y/n) : ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] CTRL + C DETECTED !\033[0")
        time.sleep(0.5)
        print ("\n\n\033[1;91m[!] PLENTY OF FISH IN THE SEA \033[0m😃\n\n")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("  [~] FILE TO SAVE AS : ")
    print ("\n" + "  " + "»" * 35 + "\n")
    logger(data)
else:
    print ("  [!] DATA WONT BE SAVED!")
    print ("\n" + "  " + "»" * 35 + "\n")


def dorks():
    try:
        dork = input("\n  [+] SEARCH QUERY  : ")
        amount = input("  [+] NUMBER OF SITES : ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[+] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] CTRL + C DETECTED...!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] THERE ARE PLENTY OF FISH IN THE SEA \033[0m😃\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] DONE FETCHING SITES PLEASE FOLLOW ME")
    print ("\n\t\t\033[34mRIPPER\033[0m")
    print ("\t\t\033[1;91m[!] WEBSITES RIPPED \033[0m😃\n\n")
    sys.exit()


# =====# Main #===== #
if __name__ == "__main__":
    dorks()
