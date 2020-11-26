import sys
from Greedy import Greedy
from BruteForce import BruteForce

if __name__ == '__main__':

    path = "inputs/"
    fw = open(path + sys.argv[1] + "_w.txt", 'r')
    fp = open(path + sys.argv[1] + "_p.txt", 'r')
    fc = open(path + sys.argv[1] + "_c.txt", 'r')
    fs = open(path + sys.argv[1] + "_s.txt", 'r')
    W = list(map(int, fw.read().splitlines()))
    P = list(map(int, fp.read().splitlines()))
    M = int(fc.readline())
    S = list(map(int, fs.read().splitlines()))
    fw.close()
    fs.close()
    fp.close()
    fc.close()

    s_mask = 0
    debug = 0
    for idx in range(len(W)):
        s_mask += (2 ** idx) * S[idx]

    if s_mask == Greedy(W, P, M, debug):
        print(" GREEDY PASS :)")
    else:
        print("GREEDY FAIL :( ")

    if s_mask == BruteForce(W, P, M, debug):
        print(" BRUTE PASS :)")
    else:
        print("BRUTE FAIL :( ")