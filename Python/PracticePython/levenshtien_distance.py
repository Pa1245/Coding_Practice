def iterative_levenshtein(s, t, costs=(1, 1, 1)):
    rows = len(s) + 1
    cols = len(t) + 1
    deletes, inserts, substitutes = costs

    dist = [[0 for x in range(cols)] for x in range(rows)]

    #source prefixes can be transformed into empty strings by deletions
    for row in range(1, rows):
        dist[row][0] = row*deletes

    # target prefixes can be created from an empty string by insertions
    for col in range(1, cols):
        dist[0][col] = col*inserts

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = substitutes
            dist[row][col] = min(dist[row-1][col]+deletes,
                                 dist[row][col-1]+inserts,
                                 dist[row-1][col-1]+cost)

    for r in range(rows):
        print(dist[r])
    print row, col
    return dist[row][col]

print(iterative_levenshtein("abc", "xyz", costs=(1, 1, 2)))
