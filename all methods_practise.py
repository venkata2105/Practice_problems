<<<<<<< HEAD
# l1=[1,56,8,9,1,4,20,33,65,98,10,11]
# print(l1[2:5])
# print(l1[:8])
# l1=[1,56,8,9,1,4,[20,33,65],98,10,11]
# print(l1[6])
# print(l1[6][1])
# l1=[1,56,8,9,1,4,20,33,65,98,10,11]
# if 8 in l1:
#     print('yes')
#changing specific value
# l1=[2,54,51,41,6,22,13,45]
# l1[3]=44
# print(l1)

# l1=[2,54,51,41,6,22,13,45]
# print(l1[3])
# l1.insert(3,33)
# print(l1)
# l1=[2,54,51,41,6,22,13,45]
# l2=[100,102,103,601,105]
# for i in l2:
#     l1.append(i)
# print(l1)
#remove
# l1=[2,54,51,41,6,22,13,45]
# print(l1)
# l1.remove(41)
# print(l1)

#pop
# l1=[2,54,51,41,6,22,13,45]
# print(l1.pop())
# print(l1)


# l1=[2,54,51,41,6,22,13,45]
# while l1:
#     l1.pop()
#     print(l1)
# l1=[2,54,51,41,6,22,13,45]
# l1.clear()
# print
# l1=[2,54,51,41,6,22,13,45]
# l1.extend({'venk','naveen'})
# print(l1)
# l1=[2,54,51,41,6,22,13,45]
# l1.sort(reverse=True)
# print(l1)
# l1=[2,54,51,41,6,22,13,45]
# l1.reverse()
# print(l1)
# print(l1.count(2))
# print(l1.index(41))
# print(l1[2])

#DICTIONARY METHODS

#creatina empty dictionary
# dict_1 = {}
# print(dict_1)
# dict_2 = dict()
# # #dict_3 = {"name": 'venkata', "age": 28, "place": "krpuram "}
# # print((dict_2))
# dict_2.update([("name","venkata"),("place","krpuram")])
# print(dict_2)
# Dict_1 = dict([(1,'a'), (2, 'b')]) #{1: 'a', 2: 'b'}
# print(Dict_1)

# it is not adviced to pass list of lists as iterables in update method

# my_dict = {}
# my_dict.update([["name", "John"], ["age", 25], ["city", "New York"]])
# print(my_dict)
# '''The update method in Python expects an iterable of key-value pairs, typically in the form of tuples.
# When you pass a list of lists to update, it doesn't interpret the inner lists as key-value pairs automatically, leading to unexpected
#   behavior.
#
# In your case, you can pass a list of tuples or use a dictionary directly. Here are both approaches:'''
# my_dict = {}
# my_dict.update({"name": "John","age": 25, "city":"New York"})
# print(my_dict)

#METHODS

# dict_1 = {"name": "venkata",
#           "place": "krpuram",
#           "emp_id": "0464700",
#           "branch": "civil"
#           }
# print(dict_1.get("name"))
# print(type(dict_1.get("name"))) #string

#print(dict_1.keys()) # dict_keys(['name', 'place', 'emp_id', 'branch']) keys are retrived in the form of list
#print(dict_1.values()) # dict_values(['venkata', 'krpuram', '0464700', 'civil'])
#print(dict_1.items()) #dict_items([('name', 'venkata'), ('place', 'krpuram'), ('emp_id', '0464700'), ('branch', 'civil')])
# items will be retrieved in the form of tuples in list

# dict_2 = dict()
# print(dict_2.fromkeys(["venkata","krpuran","tpg"]))#{'venkata': None, 'krpuran': None, 'tpg': None}
#
# print(dict_2.fromkeys(("venkata","krpuran","tpg"),1)) #{'venkata': 1, 'krpuran': 1, 'tpg': 1}
# '''Creates a new dictionary from the given iterable (string, list, set, tuple) as keys and with the specified value.'''
# dict_1 = {"name": "venkata",
#           "place": "krpuram",
#           "emp_id": "0464700",
#           "branch": "civil"
#           }
# for i in dict_1:# by default we get keys but it is not adviced
#     print(i)
# for i in dict_1.keys():
#     print(i)
# print(type(i))
# for val in dict_1.values():
#     print(val)
# for key,val in dict_1.items():
#     print(key,val)
# dict_1.update([("branch",200)])
# print(dict_1)
#setdefault

# dict_1 = {"name": "venkata",
#           "place": "krpuram",
#           "emp_id": "0464700",
#           "branch": "civil"
#           }
# # dict_1.update({"college","jntuk"})
# # print(dict_1)
# print(dict_1.setdefault("temple",200))
# '''simalar to get method, bt it throws none when key is not found,we can
# give default value if no value is found it returns tht value'''
# print(dict_1)

# dict_1 = {"name": "venkata",
#           "place": "krpuram",
#           "emp_id": "0464700",
#           "branch": "civil"
#           }
# (dict_1.setdefault("college","anits"))
# dict_1.update([("course",'civil'),("specialization","geotech")])
# # dict_1.pop('place')
# # print(dict_1)
# print(dict_1)
# dict_1.popitem()
# print(dict_1)

#NESTED DICTIONARY
# dicti_1 = {1: {'roll': '101', 'name': 'sam'}, 2: {'roll': '102', 'name': 'ram'}}
# #print(dicti_1[2]["roll"])
# # roll_dict = dicti_1.get(2)
# # for i,val in roll_dict.items():
# #     if i == 'roll':
# #         print(val)
# roll_val = dicti_1.get(2, {})
# if 'roll'in roll_val:
#     value = roll_val["roll"]
#     print(value)
# # else:
# #     print("key not found")

# 1. Adding one pair at a time
#dict_3 = {}
# dict_3[0] = 'a'
# dict_3[1] = 'b'
# print(dict_3)
# dict_4 = dict([(1,"VENKATA"),("age",28),("anits","vizag")])
# print(dict_4)
# dict_1 = {}
# for num in range(1,10):
#     dict_1[num] = (num*num)
# print(dict_1)

#list to dictionary

# list_1 = [1, 25, 32, 65, 9, 41, 22, 13]
# dict_1 = {}
# for i in range(len(list_1)-1):
#     dict_1[f"key_{i}"] = list_1[i]
# print(dict_1)

#Create a list of tuples from the dictionary

# dict_1 = {1: 'a', 2: 'b', 3: 'c'}
# list_1 = list(dict_1.items())
# print(type(list_1))

#How can you delete key-value pair from Dictionary?
# dict_1 = {1: 'a', 2: 'b', 3: 'c'}
# del dict_1[3]
# print(dict_1)
# print(dict_1.pop(3)) # need to pass key
# print(dict_1)
# print(dict_1.popitem()) # dont need to pass any key automatically removes last item
# print(dict_1)
=======
# l1=[1,56,8,9,1,4,20,33,65,98,10,11]
# print(l1[2:5])
# print(l1[:8])
# l1=[1,56,8,9,1,4,[20,33,65],98,10,11]
# print(l1[6])
# print(l1[6][1])
# l1=[1,56,8,9,1,4,20,33,65,98,10,11]
# if 8 in l1:
#     print('yes')
#changing specific value
# l1=[2,54,51,41,6,22,13,45]
# l1[3]=44
# print(l1)

# l1=[2,54,51,41,6,22,13,45]
# print(l1[3])
# l1.insert(3,33)
# print(l1)
# l1=[2,54,51,41,6,22,13,45]
# l2=[100,102,103,601,105]
# for i in l2:
#     l1.append(i)
# print(l1)
#remove
# l1=[2,54,51,41,6,22,13,45]
# print(l1)
# l1.remove(41)
# print(l1)

#pop
# l1=[2,54,51,41,6,22,13,45]
# print(l1.pop())
# print(l1)


# l1=[2,54,51,41,6,22,13,45]
# while l1:
#     l1.pop()
#     print(l1)
# l1=[2,54,51,41,6,22,13,45]
# l1.clear()
# print
# l1=[2,54,51,41,6,22,13,45]
# l1.extend({'venk','naveen'})
# print(l1)
# l1=[2,54,51,41,6,22,13,45]
# l1.sort(reverse=True)
# print(l1)
# l1=[2,54,51,41,6,22,13,45]
# l1.reverse()
# print(l1)
# print(l1.count(2))
# print(l1.index(41))
# print(l1[2])

#DICTIONARY METHODS

#creatina empty dictionary
# dict_1 = {}
# print(dict_1)
# dict_2 = dict()
# # #dict_3 = {"name": 'venkata', "age": 28, "place": "krpuram "}
# # print((dict_2))
# dict_2.update([("name","venkata"),("place","krpuram")])
# print(dict_2)
# Dict_1 = dict([(1,'a'), (2, 'b')]) #{1: 'a', 2: 'b'}
# print(Dict_1)

# it is not adviced to pass list of lists as iterables in update method

# my_dict = {}
# my_dict.update([["name", "John"], ["age", 25], ["city", "New York"]])
# print(my_dict)
# '''The update method in Python expects an iterable of key-value pairs, typically in the form of tuples.
# When you pass a list of lists to update, it doesn't interpret the inner lists as key-value pairs automatically, leading to unexpected
#   behavior.
#
# In your case, you can pass a list of tuples or use a dictionary directly. Here are both approaches:'''
# my_dict = {}
# my_dict.update({"name": "John","age": 25, "city":"New York"})
# print(my_dict)

#METHODS

# dict_1 = {"name": "venkata",
#           "place": "krpuram",
#           "emp_id": "0464700",
#           "branch": "civil"
#           }
# print(dict_1.get("name"))
# print(type(dict_1.get("name"))) #string

#print(dict_1.keys()) # dict_keys(['name', 'place', 'emp_id', 'branch']) keys are retrived in the form of list
#print(dict_1.values()) # dict_values(['venkata', 'krpuram', '0464700', 'civil'])
#print(dict_1.items()) #dict_items([('name', 'venkata'), ('place', 'krpuram'), ('emp_id', '0464700'), ('branch', 'civil')])
# items will be retrieved in the form of tuples in list

# dict_2 = dict()
# print(dict_2.fromkeys(["venkata","krpuran","tpg"]))#{'venkata': None, 'krpuran': None, 'tpg': None}
#
# print(dict_2.fromkeys(("venkata","krpuran","tpg"),1)) #{'venkata': 1, 'krpuran': 1, 'tpg': 1}
# '''Creates a new dictionary from the given iterable (string, list, set, tuple) as keys and with the specified value.'''
# dict_1 = {"name": "venkata",
#           "place": "krpuram",
#           "emp_id": "0464700",
#           "branch": "civil"
#           }
# for i in dict_1:# by default we get keys but it is not adviced
#     print(i)
# for i in dict_1.keys():
#     print(i)
# print(type(i))
# for val in dict_1.values():
#     print(val)
# for key,val in dict_1.items():
#     print(key,val)
# dict_1.update([("branch",200)])
# print(dict_1)
#setdefault

# dict_1 = {"name": "venkata",
#           "place": "krpuram",
#           "emp_id": "0464700",
#           "branch": "civil"
#           }
# # dict_1.update({"college","jntuk"})
# # print(dict_1)
# print(dict_1.setdefault("temple",200))
# '''simalar to get method, bt it throws none when key is not found,we can
# give default value if no value is found it returns tht value'''
# print(dict_1)

# dict_1 = {"name": "venkata",
#           "place": "krpuram",
#           "emp_id": "0464700",
#           "branch": "civil"
#           }
# (dict_1.setdefault("college","anits"))
# dict_1.update([("course",'civil'),("specialization","geotech")])
# # dict_1.pop('place')
# # print(dict_1)
# print(dict_1)
# dict_1.popitem()
# print(dict_1)

#NESTED DICTIONARY
# dicti_1 = {1: {'roll': '101', 'name': 'sam'}, 2: {'roll': '102', 'name': 'ram'}}
# #print(dicti_1[2]["roll"])
# # roll_dict = dicti_1.get(2)
# # for i,val in roll_dict.items():
# #     if i == 'roll':
# #         print(val)
# roll_val = dicti_1.get(2, {})
# if 'roll'in roll_val:
#     value = roll_val["roll"]
#     print(value)
# # else:
# #     print("key not found")

# 1. Adding one pair at a time
#dict_3 = {}
# dict_3[0] = 'a'
# dict_3[1] = 'b'
# print(dict_3)
# dict_4 = dict([(1,"VENKATA"),("age",28),("anits","vizag")])
# print(dict_4)
# dict_1 = {}
# for num in range(1,10):
#     dict_1[num] = (num*num)
# print(dict_1)

#list to dictionary

# list_1 = [1, 25, 32, 65, 9, 41, 22, 13]
# dict_1 = {}
# for i in range(len(list_1)-1):
#     dict_1[f"key_{i}"] = list_1[i]
# print(dict_1)

#Create a list of tuples from the dictionary

# dict_1 = {1: 'a', 2: 'b', 3: 'c'}
# list_1 = list(dict_1.items())
# print(type(list_1))

#How can you delete key-value pair from Dictionary?
# dict_1 = {1: 'a', 2: 'b', 3: 'c'}
# del dict_1[3]
# print(dict_1)
# print(dict_1.pop(3)) # need to pass key
# print(dict_1)
# print(dict_1.popitem()) # dont need to pass any key automatically removes last item
# print(dict_1)
>>>>>>> 315d1c944ede9b2accdca82af0d27905e7f500a6
