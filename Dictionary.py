dic1 = {
    'name' : "arnob",
    'age' : 22,
    'height' : 70,
    'weight' : 80,
    'city' : "seattle",
    'email': 'test@email.com'
}
print(dic1['name'])
#returns the keys
print(dic1.keys())
#returns the values
print(dic1.values())
#Returnes the values
print(dic1.items())
#updateing value
dic1['age'] = 30
print(dic1['age'])
#add key-value
dic1['hometown'] = 'ctg'
print(dic1['hometown'])
print(dic1)
#Remove items
dic1.pop('age')#Removes specific key value
print(dic1)
dic1.popitem()
print(dic1)
#loop dictionary
for i in dic1:  # Return list of keys
    print(i)
#prints key pair value
for i, j in dic1.items():
    print(f'{i} --> {j}')
#nasted-map
nes_dictioary = {
    'p1' : {
        'name' : 'A',
        'age' : 22,
        'height' : 70,
    },
    'p2' : {
        'name' : 'B',
        'age' : 22,
        'height' : 70,
    },
    'p3' : {
        'name' : 'C',
        'age' : 22,
    }
}
print(nes_dictioary['p1']['name'])
#loop in nested dictionary
for k,d in nes_dictioary.items():
    print(f'{k} -->')
    for k,v in d.items():
        print(f'{k} --> {v}')
#write a Phython script to check whether a given key is available in the dictionary
dic3= {
    'name' : "arnob",
    'age' : 22,
   'height' : 70,
    'weight' : 80,
    'city' : "seattle",
    'email': '<EMAIL>'
}
# key = input("Enter key: ")
# if key in dic3:
#     print("Found")
# else:
#     print("Not found")
#max value and min value in a dictionary
num_dis = {
    'num1' : 30,
    'num2' : 40,
    'num3' : 50,
}
print("Max:", max(num_dis.values()))
print("Min:", min(num_dis.values()))
sorted(num_dis.values())
#using sorted
print(sorted(num_dis.values())[0])
print(sorted(num_dis.values())[-1])
#create a dictionary by interchanging the key and value of another dictionary
dic = {
    "a": 22,
    "b": 22,
    "c": 22,
}

reversed_dic = {}

for key, value in dic.items():
    if value not in reversed_dic:
        reversed_dic[value] = [key]
    else:
        reversed_dic[value].append(key)

print(reversed_dic)





