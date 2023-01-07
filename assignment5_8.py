"""
Create a dictionary of 20 random values in the range 1–99. Determine whether there
are any duplicate values in the dictionary.
"""


from random import randint

# initializing list
test_list = 20

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 2, 99

res = dict()
for ele in range(1,21):
    # assigning random elements
    res[ele] = randint(i, j)

# printing result
print("Random range initialized dictionary : " + str(res))
# finding duplicate values
# from dictionary using flip
flipped = {}

for key, value in res.items():
    if value not in flipped:
        flipped[value] = [key]
    else:
        flipped[value].append(key)
        print("duplicted  value = ",value)

# printing result
print("final_dictionary", str(flipped))