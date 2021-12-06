#!/usr/bin/python3



b = ["fuck","my","ass"]

c = {"fart":b, "newtruck":"is awesome", "tits":"fun bags"}

flag = False


#I can say anything there and it will be ignored.
#This is the begining of the for loop, and the code will repeat over each item in the list.
for i in b:
	if i == "homo":
		flag = True
#After it has gone over each item, the loop is over and now the code continues.

if flag == True:
	print("Homo was in there.")
else:
	print("Homo was not in there.")


print(c["fart"])

for i in c["fart"]:
	print(i) 


def my_cool_function(my_list):
	for i in my_list:
		print(i)


def find_string_in_list(my_string, my_list):
	#This function takes a string and a list. It will return True if given string is in the given list.
	flag = False
	for i in my_list:
		if i == my_string:
			flag = True
	return flag

def find_leter_in_all_strings_in_list(my_letter, my_list):
	flag = False
	for i in my_list:
		for letter in i:
			if letter == my_letter:
				flag = True
	return flag

my_cool_function(c)

new_list = ["budweiser", "strohs", "yingling", "corona"]

my_result = find_string_in_list("o", new_list)
print(my_result)


print("###############################################")


a = "fart"

b = "this is a way to %s stick %s a var in a string"%(a, "shaun")

print(b)