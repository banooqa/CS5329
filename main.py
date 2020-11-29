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

def random_test(n_mult, m_mult, debug):
    n = (n_mult * 10) + random.randint(-5, 5)
    M = (m_mult * 10) + random.randint(-5, 5)
    W = []
    P = []
    if debug:
        print("n=" + str(n) + ", M=" + str(M))
    for i in range(n):
        W.append(math.ceil(random.random() * 5 * M / n))
        P.append(random.randint(1, 100))
    dyn = Dynamic(W, P, M, debug)
    bru = BruteForce(W, P, M, debug)
    if list_equal(dyn, bru):
        print("Random Test Pass")
    else:
        print("Random Test Fail")


def directed_tests(problem, debug):
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

    start = time.perf_counter()
    greedy = Greedy(W, P, M, debug)
    if list_compare(greedy, sol) == 0:
        print("GREEDY PASS :)")
    else:
        print("GREEDY FAIL :( ")
    greedy_time = time.perf_counter() - start

    start = time.perf_counter()
    dynamic = Dynamic(W, P, M, debug)
    if list_equal(dynamic, sol):
        print("DYNAMIC PASS :)")
    else:
        print("DYNAMIC FAIL :( ")
    dynamic_time = time.perf_counter() - start

    start = time.perf_counter()
    brute = BruteForce(W, P, M, debug)
    if list_equal(brute, sol):
        print("BRUTE PASS :)")
    else:
        print("BRUTE FAIL :( ")
    brute_time = time.perf_counter() - start

    print(f"Brute took {brute_time:0.4f}s, Greedy took {greedy_time:0.4f}s, and Dynamic took {dynamic_time:0.4f}s")
    print(f"total speedup: {brute_time / dynamic_time:0.4f}")

def random_tests(debug):
    n_list = [1, 2, 3]
    m_list = [2, 4]
    for n in n_list:
        for m in m_list:
            random_test(n, m, debug)

if __name__ == '__main__':
    debug = 0
    # directed_tests('p01', debug)
    random_tests(debug)


