from function_exercises import calculate_tip

print(calculate_tip(600))

# */2. Read about and use the itertools module from the python standard library to help you solve the following problems:

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
from itertools import product
len(list(product('abc','123')))
# How many different combinations are there of 2 letters from "abcd"?
from itertools import combinations
len(list(combinations('abcd', 2)))
# How many different permutations are there of 2 letters from "abcd"? */
from itertools import permutations
len(list(permutations('abcd', 2)))




#3. Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
import json

dictionary = json.load(open('profiles.json'))
# Total number of users
len(dictionary)
# Number of active users
active = 0

for key in dictionary:
    if key['isActive'] == True:
        active += 1
print(active)
# Number of inactive users
not_active = 0
for key in dictionary:
    if key['isActive'] == False:
        not_active += 1
print(not_active)
# Grand total of balances for all users
grand_total = 0

for profile in profiles:
    user_balance = float(profile['balance'].strip('$').replace(',', ''))
    grand_total = grand_total + user_balance
    
print(grand_total)

# Average balance per user
round(grand_total / len(profiles), 2)

# User with the lowest balance
balance_ls = []

for profile in profiles:
    if profile['balance'].strip('$').replace(',', '') == min(balance_ls):
        print(f'User {profile["name"]} has the least amount of cash: {profile["balance"]}')

min(balance_ls)
# User with the highest balance
for profile in profiles:
    if profile['balance'].strip('$').replace(',', '') == max(balance_ls):
        print(f'User {profile["name"]} has the most amount of cash: {profile["balance"]}')

# Most common favorite fruit
fruits = []

for profile in profiles:
    print(profile['favoriteFruit'])
    fruits.append(profile['favoriteFruit'])

set(fruits)

fruits

fruits.count('strawberry')

max(fruits, key=fruits.count)

# Least most common favorite fruit

min(fruits, key=fruits.count)

# Total number of unread messages for all users*/

sum_messages = 0

for profile in profiles:
    message = profile['greeting'].split(' ')
    for word in message:
        if word.isdigit():
            sum_messages = sum_messages + int(word)
            
sum_messages
