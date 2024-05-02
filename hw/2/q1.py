import itertools
import sys

def main():
    weights = [i*5 for i in range(1, 12)]
    presuf(weights)
    brute_force(weights)

def brute_force(weights):
    print("Brute Force")

    pileA = []
    pileB = []
    perms = itertools.permutations(weights)

    total_sum = sum(weights) 
    smallest = 100000
    for perm in perms:
        smallA = perm[: len(perm) // 2 + 1]
        smallB = perm[len(perm) // 2 + 1:]
        sum_pileA = sum(smallA)
        sum_pileB = total_sum - sum_pileA
        diff = abs(sum_pileA - sum_pileB)
        if diff == 0:
            break
        if diff < smallest:
            smallest = diff
            pileA = smallA
            pileB = smallB
            print(diff, pileA, pileB)
    diff = sum(pileA) - sum(pileB)
    print(diff, pileA, pileB)

def presuf(weights):
    # total = sum(weights)
    total = 0
    n = len(weights)
    for i in range(n): 
        total += weights[i] 
    prefix_sum = 0
    minDiff = sys.maxsize
    pileA = []
    pileB = []
  
    # Traverse the given array 
    for i in range(n - 1): 
        prefix_sum += weights[i] 
  
        # To store minimum difference 
        diff = abs((total - 
                   prefix_sum) - 
                   prefix_sum) 
  
        # Update minDiff 
        if (diff < minDiff): 
            minDiff = diff 
            pileA = weights[:i + 1]
            pileB = weights[i + 1:]
    # Return minDiff
    print(minDiff, pileA, pileB)
    return minDiff 

if __name__ == "__main__":
    main()