##############################################
# AoC Day 03
## P01 answer - 3009600
## P02 answer - 
##############################################

from request_input_data import get_input
# get_input(3)
# for line in get_input(3):
#     print(line)

txtfile = r'C:\Users\christian.garvey\OneDrive - Arup\01 Documents\01-07 Digital\Python\Advent of Code 2021\advent_of_code\day03_input.txt'

list_binary=[]
with open(txtfile, 'r') as file: 
    # Read and remove '/n' from string using _.strip()
    list_binary = [line.strip() for line in file.readlines()]    

# Calculate length of each line
len_line = 0
for line in list_binary[0]:
    for i in line:
        len_line += 1
print(len_line)   

# Generate a list of counts of '1' for each index of line. 
no_1_list = []
def get_no_1_list(bit_index):
    no_1 = 0
    for line in list_binary:
        if int(line[bit_index]) == 1:
            no_1 += 1
        else: pass
        #print(no_1)    
    #print(no_1) # returns the no_1 for line[0] ('521')
    no_1_list.append(no_1)
    return no_1_list

for i in range(0,len_line):
    get_no_1_list(i)
print(no_1_list)

# Create a list for gamma (if there are more 1's in the index than 0's, then record '1') and epsilon (the opposite to gamma)
gamma = []
epsilon = []
for i in no_1_list:
    print("i is...", i)
    if i > (len(list_binary)/2):
    #print("gamma is 1")
        gamma.append(1)
        #print("...so epsilon is 0")
        epsilon.append(0)
    else:
        #print("gamma is 0")
        gamma.append(0)
        #print("...so epsilon is 1")
        epsilon.append(1)

print(gamma)
print(epsilon)


# Concatenate the integers in gamma and epsilon lists
def concatenate(list):
    concatenated_list = [str(x) for x in list]
    concatenated_list = "".join(concatenated_list)
    return concatenated_list

# Convert binary to decimals
def binary_to_decimal(binary_number):
    decimal_number = int(binary_number,2)
    return decimal_number

print(concatenate(gamma))
print(binary_to_decimal(concatenate(gamma)))

print(concatenate(epsilon))
print(binary_to_decimal(concatenate(epsilon)))

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ANSWER
gamma_decimal = binary_to_decimal(concatenate(gamma))
epsilon_decimal = binary_to_decimal(concatenate(epsilon))
answer = gamma_decimal * epsilon_decimal
print(answer)


