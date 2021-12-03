##############################################
# AoC Day 01
## P01 answer - 1832
## P02 answer - 1858
##############################################

txtfile = r'C:\Users\christian.garvey\OneDrive - Arup\01 Documents\01-07 Digital\Python\Advent of Code 2021\advent_of_code\day01_input.txt'

list_int = []
with open(txtfile, 'r') as file: 
    lines = file.readlines()
    for line in lines:
        line_int = int(line)
        list_int.append(line_int)

    #print(list_int)

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


i= 0
j= i+3
windows_greater_than_previous = 0
for line in list_int:
    while j < len(list_int):
        if list_int[j] > list_int[i]:
            windows_greater_than_previous += 1
        i += 1
        j += 1
print(windows_greater_than_previous)



# num_incs_pt2 = 0

# for x in range(len(lines)): 
#     if x > 2: 
#         if ((int(lines[x])) > (int(lines[x-3]))): 
#             num_incs_pt2 += 1

# print(num_incs_pt2)







## TRYING TO READ IN DIRCECTLY FROM URL --> WEBPAGE IS NOT .HTML THEREFORE CAN'T READ IT

# Read in data from url #https://docs.python.org/3/howto/urllib2.html 
import urllib.request


# req = urllib.request.Request('https://adventofcode.com/2021/day/1/input')
# with urllib.request.urlopen(req) as response:
#    the_page = response.read()


#urllib.request.urlopen() 
# url = "https://adventofcode.com/2021/day/1/input"
# file = urllib.request.urlopen(url)

# for line in file:
# 	decoded_line = line.decode("utf-8")
# 	print(decoded_line)


# from bs4 import BeautifulSoup 
# url = "https://adventofcode.com/2021/day/1/input"
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(

# for script in soup(["script", "style"]):
#     script.decompose()

# strips = list(soup.stripped_strings)
# print(strips[:5])


# import urllib
# import urllib3

# quoted_query = urllib.quote(query)
# host = 'http://www.bing.com/search?q=%s&go=&qs=n&sk=&sc=8-13&first=%s' % (quoted_query, page)
# req = urllib3.Request(host)
# req.add_header('User-Agent', User_Agent)
# response = urllib3.urlopen(req)