def my_uniq(arr):
    seen = {}
    result = []
    for el in arr:
        if el not in seen:
             result.append(el)
             seen[el] = True

    return result

def two_sum(arr):
    result = []
    for i in range(len(arr)):
        val = arr[i]
        for j in range((i+1),len(arr)):
            if val + arr[j] == 0:
                result.append([i,j])

    return result

def my_transpose(grid):
    result = [[]] * len(grid);
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            result[j].append(grid[i][j])
    return result
