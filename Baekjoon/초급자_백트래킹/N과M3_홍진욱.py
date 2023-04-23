n, m = map(int, input().split())
result = []

def backtrack(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
            result.append(i)
            backtrack(i)
            result.pop()

backtrack(1)
