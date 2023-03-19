#Python function to sum all the numbers in a list

def sum_of_list(l):
  total = 0
  for val in l:
    total = total + val
  return total

my_list = [8,2,3,0,7]
print ("The sum of my_list is", sum_of_list(my_list))


#Python program to reverse a string

s = input("the string is:")
def reverse(str):
    str = str[::-1]
    return str
print("the original string is:",s)
print("the reversed string is:",reverse(s))


#Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def count(s):
    u = 0
    l = 0
    for i in s:
        if i.isupper():
            l += 1
        elif i.islower():
            u += 1
    print("number of upper case characters:",l)
    print("number of lower case characters:",u)
s =input("enter :")
count(s)

 


 