import sys
import time
import random
import math
import collections
from Greedy import Greedy
from BruteForce import BruteForce
from Dynamic import Dynamic

def list_equal(alist, blist):
    alist.sort()
    blist.sort()
    return alist == blist

def list_compare(alist, blist):
    matches = len(set(alist).intersection(blist))
    mismatches = len(alist) + len(blist) - (2 * matches)
    print("There were " + str(matches) + "matches and " + str(mismatches) + " mismatches.")
    return mismatches

def random_test(n_mult, m_mult, debug, timing):
    n = (n_mult * 10) + random.randint(-5, 5)
    M = (m_mult * 10) + random.randint(-5, 5)
    W = []
    P = []
    if debug:
        print("n=" + str(n) + ", M=" + str(M))
    for i in range(n):
        W.append(math.ceil(random.random() * 5 * M / n))
        P.append(random.randint(1, 100))
    dyn = Dynamic(W, P, M, debug, timing)
    if n_mult <= 10 and m_mult <= 10:
        bru = BruteForce(W, P, M, debug, timing)
        if list_equal(dyn, bru):
            print("Random Test Pass :) :) :) :) :) :) :) :)")
        else:
            print("Random Test Fail :____________________(")
    else:
        print("Skipping Brute tests as the problem set is big")


def directed_test(problem, debug, timing):
    path = "inputs/"
    fw = open(path + problem + "_w.txt", 'r')
    fp = open(path + problem + "_p.txt", 'r')
    fc = open(path + problem + "_c.txt", 'r')
    fs = open(path + problem + "_s.txt", 'r')
    W = list(map(int, fw.read().splitlines()))
    P = list(map(int, fp.read().splitlines()))
    M = int(fc.readline())
    S = list(map(int, fs.read().splitlines()))
    fw.close()
    fs.close()
    fp.close()
    fc.close()

    sol = []
    for i in range(len(S)):
        if S[i]:
            sol.append(i)

    greedy = Greedy(W, P, M, debug, timing)
    if list_compare(greedy, sol) == 0:
        print("GREEDY PASS :) :) :) :) :) :) :) :)")
    else:
        print("GREEDY FAIL :____________________( ")

    dynamic = Dynamic(W, P, M, debug, timing)
    if list_equal(dynamic, sol):
        print("DYNAMIC PASS :) :) :) :) :) :) :) :)")
    else:
        print("DYNAMIC FAIL :____________________( ")

    brute = BruteForce(W, P, M, debug, timing)
    if list_equal(brute, sol):
        print("BRUTE PASS :) :) :) :) :) :) :) :)")
    else:
        print("BRUTE FAIL :____________________( ")

def random_tests(debug, timing):
    n_list = [1, 2, 90]
    m_list = [2, 10, 100]
    for n in n_list:
        for m in m_list:
            print("\nRunning random test with approx " + str(n*10) + " elements and a max weight of approx " + str(m*10))
            random_test(n, m, debug, timing)

def directed_tests(debug, timing):
    for i in range(1, 8):
        print("\nRunning test p0" + str(i))
        directed_test("p0" + str(i), debug, timing)

if __name__ == '__main__':
    debug = 0
    timing = 1
    directed_tests(debug, timing)
    random_tests(debug, timing)


