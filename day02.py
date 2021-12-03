##############################################
# AoC Day 02
## P01 answer - 2039912
## P02 answer - 1942068080
##############################################

from request_input_data import get_input
get_input(2)

## Print lines in input file
#for line in get_input(2):
    #print(line)


## PART 1 ##
# down z = depth - z
# up z= depth + z
# forward x = horizontal + x

# depth = 0
# horizontal = 0
# aim = 0

# for command in get_input(2):
#     #use index '-2' to skip the \n in each string.
#     if 'down' in command:
#         depth += int(command[-1])
#     else:
#         if 'up' in command:
#             depth -= int(command[-1])
#         else:
#             if 'forward' in command:
#                 horizontal += int(command[-1])


# answer = depth * horizontal
# print(answer)


## PART 2 ##

depth = 0
horizontal = 0
aim = 0

for command in get_input(2):
    #could use parse each line using for line in data: list.append(tuple(line.strip("\n").split()))
    if 'down' in command:
        #depth += int(command[-1])
        aim += int(command[-1])
    elif 'up' in command:
        #depth -= int(command[-1])
        aim -= int(command[-1])
    elif 'forward' in command:
        horizontal += int(command[-1])
        depth += (aim*int(command[-1]))

print(depth)
print(horizontal)
print(aim)

answer = horizontal*depth
print(answer)



"""SOLUTION USING NUMPY AND VECTORS
https://www.reddit.com/r/adventofcode/comments/r6zd93/2021_day_2_solutions/ """

# import numpy as np

# with open('input/day02') as f:
#     directions = list(filter(None, f.read().split()))

# vectors = dict(zip(['forward', 'up', 'down'], map(np.array, [[1, 1, 0], [0, 0, -1], [0, 0, 1]])))

# position1, position2 = [0,0,0], [0,0,0]  # [horizontal, n/a, depth], [horizontal, depth, aim]
# for name, val in zip(directions[::2], directions[1::2]):
#     position1 += int(val) * vectors[name]
#     position2 += int(val) * np.array([1, position2[2], 1]) * vectors[name]

# print(position1[0]*position1[2])
# print(position2[0]*position2[1])