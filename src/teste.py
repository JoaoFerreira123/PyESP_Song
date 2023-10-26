test_string = "b'83\r\n'"

# printing original string 
print("The original string : " + test_string)

# using List comprehension + isdigit() +split()
# getting numbers from string 
res = [int(i) for i in test_string.split() if i.isdigit()]

# print result
print("The numbers list is :" + str(res))
