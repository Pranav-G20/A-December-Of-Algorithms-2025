def can_reach_last(stones):
    maxReach = 0
    for i, jump in enumerate(stones):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + jump)
        if maxReach >= len(stones) - 1:
            return True
    return True
stones = [2, 3, 1, 0, 4]
print(can_reach_last(stones))