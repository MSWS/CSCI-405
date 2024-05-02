# def min_weight_diff_dp(weights):
#     total_weight = sum(weights)
#     n = len(weights)
#     target = total_weight // 2

#     # Create the DP table
#     dp = [[False] * (target + 1) for _ in range(n)]
#     dp[0][0] = True  # Base case

#     for i in range(1, n):
#         for sum_val in range(target + 1):
#             if dp[i - 1][sum_val]:
#                 dp[i][sum_val] = True
#             elif sum_val >= weights[i] and dp[i - 1][sum_val - weights[i]]:
#                 dp[i][sum_val] = True

#     # Find the optimal split
#     for sum_val in range(target, -1, -1):  
#         if dp[n - 1][sum_val]:
#             return total_weight - 2 * sum_val

def min_weight_diff_dp(weights):
    total_weight = sum(weights)
    n = len(weights)
    target = total_weight // 2

    # Create the DP table
    dp = [[(False, False)] * (target + 1) for _ in range(n)]  # (Possible, Included)
    dp[0][0] = (True, False)  # Base case

    for i in range(1, n):
        for sum_val in range(target + 1):
            if dp[i - 1][sum_val][0]:  # Don't include the current item
                dp[i][sum_val] = (True, False) 
            elif sum_val >= weights[i] and dp[i - 1][sum_val - weights[i]][0]: 
                dp[i][sum_val] = (True, True)  # Include the current item

    # Find the optimal split
    for sum_val in range(target, -1, -1):  
        if dp[n - 1][sum_val][0]:
            break  # Found the weight of the heavier subset

    minVal = total_weight - 2 * sum_val
    # Backtrack to find the groups
    group1 = []
    group2 = []
    i = n - 1
    while i >= 0:
        if dp[i][sum_val][1]:
            group1.append(weights[i])
            sum_val -= weights[i]
        else:
            group2.append(weights[i])
        i -= 1

    return minVal, group1, group2 

# Example usage
weights = [i*5 for i in range(1, 11)]
min_difference, group1, group2 = min_weight_diff_dp(weights)
print("Minimum Difference:", min_difference)
print("Group 1:", group1)
print("Group 2:", group2) 
print(sum(group1) - sum(group2))


# Example usage
# weights = [2, 5, 1, 3]
# min_difference = min_weight_diff_dp(weights)
# print(min_difference)  # Output: 1
