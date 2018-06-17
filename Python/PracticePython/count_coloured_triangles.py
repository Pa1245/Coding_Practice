def count_col_triang(input_):
    num_points = len(input_)
    colours = list(set([input_[i][1] for i in range(num_points)]))
    points = {colour:[] for colour in colours}
    [points[input_[i][1]].append(input_[i][0]) for i in range(num_points)]
    from itertools import combinations
    count_poss_triang = 0
    aligned_points = 0
    for colour in colours:
        points[colour] = list(combinations(points[colour], 3))
        count_poss_triang = count_poss_triang + len(points[colour])
        for triang in points[colour]:
            if determinant(triang) == 0:
                aligned_points = aligned_points + 1
                points[colour].remove(triang)
    print points
    print aligned_points
    return [num_points, len(colours), count_poss_triang, []]

def determinant(input_):
    det = (input_[0][0]*(input_[1][1]-input_[2][1])-input_[0][1]*(input_[1][0]-input_[2][0])
            + (input_[1][0]*input_[2][1]-input_[1][1]*input_[2][0]))
    return det

print count_col_triang([[[3, -4],
'blue'], [[-7, -1], 'red'],
[[7, -6], 'yellow'], [[2, 5], 'yellow'],
[[1, -5], 'red'], [[-1, 4], 'red'],
[[1, 7], 'red'], [[-3, 5], 'red'],
[[-3, -5], 'blue'], [[4, 1], 'blue']])

print determinant(([3, -4], [-3, -5], [4, 1]))

#answer: [10, 3, 11, ['red',10]]
