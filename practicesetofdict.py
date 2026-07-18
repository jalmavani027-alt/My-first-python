# This is practice set of Dictionary & Sets

# Question 1 : Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

translate = {
    "dekh" : "see",
    "khursi" : "chair",
    "madad" : "help",
    "aadmi" : "guy",
    "bakri" : "goat"
}

a = input("Write dowm hindi word here you get english meaning of that words :")
print(translate[a])


# Question 2 : Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!.

s = set()

a = input("Enter number :")
s.add(int(a))
a = input("Enter number :")
s.add(int(a))
a = input("Enter number :")
s.add(int(a))
a = input("Enter number :")
s.add(int(a))
a = input("Enter number :")
s.add(int(a))
a = input("Enter number :")
s.add(int(a))
a = input("Enter number :")
s.add(int(a))
a = input("Enter number :")
s.add(int(a))

print(s)


# Question 3 :  Can we have a set with 18 (int) and '18' (str) as a value in it?

t = set()
t.add(int(18))
t.add("18")
print(t)



# Question 4 : What will be the length of following set s:

s = set()
s.add(20)
s.add(20.0)
s.add('20') 

print(len(s))


# Question 5 : Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.

d = {}

name = input("Enter your friend name :")
lang = input("Enter your friend language :")
d.update({name : lang})

name = input("Enter your friend name :")
lang = input("Enter your friend language :")
d.update({name : lang})

name = input("Enter your friend name :")
lang = input("Enter your friend language :")
d.update({name : lang})

name = input("Enter your friend name :")
lang = input("Enter your friend language :")
d.update({name : lang})

print(d)


# Question 6 : . Can you change the values inside a list which is contained in set S?

# s = {8, 7, 12, "Harry", [1,2]}

# we cannot change the value inside the sets it is not possible by any methods 
# Also you cannot add the list inside the any sets.



