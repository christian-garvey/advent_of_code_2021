##############################################
# AoC Day 01
## P01 answer - 1832
## P02 answer - 1858
##############################################

txtfile = r'C:\Users\christian.garvey\OneDrive - Arup\01 Documents\01-07 Digital\Python\Advent of Code 2021\advent_of_code\day01_input.txt'

with open(txtfile, 'r') as file: 
    list_int = [int(line) for line in file.readlines()]    
print(len(list_int))


## PART 1 ##
# no_greater_than = 0
# counter = -1
# for line in list_int:
#     counter += 1
#     line_minus1 = list_int[counter-1]
#     if counter == 0:
#         pass
#     elif line > line_minus1:
#         no_greater_than += 1
# print(no_greater_than)


## PART 2 ##
## Compare index against index-3
# no_greater_than = 0
# counter = -1
# for line in list_int:
#     counter += 1
#     line_minus3 = list_int[counter-3]
#     if counter == 0:
#         pass
#     elif line > line_minus3:
#         no_greater_than += 1
# print(no_greater_than)


# i= 0
# j= i+3
# windows_greater_than_previous = 0
# for line in list_int:
#     while j < len(list_int):
#         if list_int[j] > list_int[i]:
#             windows_greater_than_previous += 1
#         i += 1
#         j += 1
# print(windows_greater_than_previous)



# num_incs_pt2 = 0

# for x in range(len(lines)): 
#     if x > 2: 
#         if ((int(lines[x])) > (int(lines[x-3]))): 
#             num_incs_pt2 += 1

# print(num_incs_pt2)
