#!/usr/bin/env python2
import argparse
import numpy as np
from itertools import izip_longest

biggest_difference = 0.0


def main():

    parser = argparse.ArgumentParser(description="check if two data files are equivalent")
    parser.add_argument("file1", type=str, help="first file to compare")
    parser.add_argument("file2", type=str, help="second file to compare")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    args = parser.parse_args()

    filea = open(args.file1)
    fileb = open(args.file2)

    counter = 0
    while True:
        counter += 1
        linea = filea.readline()
        lineb = fileb.readline()
        if linea == "" and lineb == "":
            print "end of file"
            break
        if linea[0] == "#" and lineb[0] == "#":
            print "line {} was a comment".format(counter)
            continue
        if not comparestrings(linea, lineb):
            print "files not equivalent"
            exit(1)

    print "files matched within tolerance"
    global biggest_difference
    print "biggest mismatch {}".format(biggest_difference)


def numbersfromstring(s):
    numbers = []
    for trial in s.split(","):
        try:
            numbers.append(float(trial))
        except ValueError:
            print "{} could not be a float".format(trial)
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
            print "{} did not match {}".format(*p)
            return False
    return True


if __name__ == "__main__":
    main()
