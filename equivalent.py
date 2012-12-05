#!/usr/bin/env python2
import logging
import argparse
import numpy as np
from itertools import izip_longest

biggest_difference = 0.0


def main():

    parser = argparse.ArgumentParser(description="Check if two data files are equivalent. Returns 0 if matched and 1 if not")
    parser.add_argument("file1", type=str, help="first data file to compare")
    parser.add_argument("file2", type=str, help="second data file to compare")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    parser.add_argument("-q", "--quiet", action="count", help="run quietly, report only errors, twice report nothing just return value")
    args = parser.parse_args()

    if args.quiet == 1:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.WARN)
    elif args.quiet == 2:
        pass
    elif args.verbose:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
        logging.debug("Verbose debuging mode activated")
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

    filea = open(args.file1)
    fileb = open(args.file2)

    counter = 0
    while True:
        counter += 1
        linea = filea.readline()
        lineb = fileb.readline()
        if linea == "" and lineb == "":
            logging.debug("end of file")
            break
        if linea[0] == "#" and lineb[0] == "#":
            logging.debug("line {} was a comment".format(counter))
            continue
        if not comparestrings(linea, lineb):
            logging.error("files not equivalent")
            exit(1)

    global biggest_difference
    if biggest_difference > 0.0:
        logging.info("files matched within tolerance. biggest mismatch {}".format(biggest_difference))
    else:
        logging.info("files matched Exactly. You could have used diff")


def numbersfromstring(s):
    numbers = []
    for trial in s.split(","):
        try:
            numbers.append(float(trial))
        except ValueError:
            logging.error("{} could not be converted to a float".format(trial))
    return numbers


def comparestrings(s1, s2):
    if s1 == s2:
        return True
    numbers1 = numbersfromstring(s1)
    numbers2 = numbersfromstring(s2)

    # if len(numbers1) is not len(numbers2):
    #     print "warning: line differs in number of data values"

    global biggest_difference
    for p in izip_longest(numbers1, numbers2, fillvalue=0.0):
        e1, e2 = p
        biggest_difference = max(biggest_difference, abs(e1 - e2))
        if not np.allclose(*p):
            logging.error("{} did not match {}".format(*p))
            return False
    return True


if __name__ == "__main__":
    main()
