#list
fruits = ["apple", "banana", "cherry"]
print(fruits)
#list can have a different type of data in the array
fruits1 = ["apple",65,"test"]
print(fruits1)
#Regular indexing in a list
fruits2 = ["apple","banana","cherry"]
print(fruits2[0])
#Replacing value in index
fruits[0] = "orange"
print(fruits)
#negetive indexing
print(fruits[-1])
fruits[-1] = "mango"
print(fruits)
## list `append` function"
fruits.append("apple")
print(fruits)
# #
# games = []
# n = int(input("number of games: "))
# for i in range(n):
#     game = input(f'Game #{i+1}: ')
#     games.append(game)
# print(games)

# games = []  # Initialize the list before using it
#
# n = int(input("Number of games: "))
# for i in range(n):
#     game = input(f'Game {i+1}: ')
#     games.append(game)
#
# # print("Games list:", games)  # Optional: show the collected games
# games.remove('cricket')
#
# print(games)

#List
fruits.insert(2,"orange")
print(fruits)
#Length of fruit array
print(len(fruits))
## list concatenation
all_list = fruits+fruits1+fruits2
print(all_list)
#sorting
number = [5,5,623,56,3,6,2,6,8,5,21,1,23,4,5,67,7,89,0]
number.sort()
print(number)
number.sort(reverse=True)
print(number)
number.reverse()
print(number)
#list slicing
len(number)
var = number[1:4]
print(var)
## Write a funtion to find the sum and avarage of a list

list_sum = sum(number)
print(list_sum)
avg = sum(number)/len(number)
print(avg)

print(sum(number)/len(number))
# write a function that returns true if one of the elements is common
num1 = [1,2,3]
num2 = [4,3,6]
def find_common(num1,num2):
    for i in num1:
        if i in num2:
            return  True
    return False

print(find_common(num1,num2))



