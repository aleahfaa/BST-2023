#077's notes:
#finding the max value of the number of the elements in the set N that are adjacent to each other with a length Ci
#if there are 2 or more totals that have the same value (the max one), then the output would be 'Ga bisa ditentuin'
#https://its.id/m/HackerrankBootcamp

def findmax(arr, l):
    maxs = sum(arr[:l])
    for i in range(1, len(arr) - l + 1):
        current = sum(arr[i:i+l])
        maxs = max(maxs, current)
    return maxs

def solve(N, Ai, B, Ci):
    maxs = []
    for i in range(N - B + 1):
        maxs.append(findmax(Ai[i:i+B], B))
    
    maxtot = max(maxs)
    if maxs.count(maxtot) > 1:
        return 'Ga bisa ditentuin'
    else:
        return maxtot

#input N
N = int(input())
Ai = []
for _ in range(N):
    Ai.append(int(input()))

#input B
B = int(input())
Ci = []
for _ in range(B):
    Ci.append(int(input()))

#solve the game and print the results
for Cj in Ci:
    result = solve(N, Ai, Cj, Ci)
    print(result)