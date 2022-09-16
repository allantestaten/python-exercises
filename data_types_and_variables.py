99.9 
# Float
type("False")
# string
False
#Bool
type('0')
#string
0
#integer
True
#Bool
'True'
#string
type([{}])
#list
type({'a':[]})
#dict

# string -A term or phrase typed into a search box?
# Bool- If a user is logged in?
# float- A discount amount to apply to a user's shopping cart?
# Bool- Whether or not a coupon code is valid?
# string- An email address typed into a registration form?
# float- The price of a product?
# list of list - A Matrix?
# list- The email addresses collected from a registration form?
# dictionary- Information about applicants to Codeup's data science program?

- error 
- remainder 2 
- int 
- type 
- error 
- False 
- False 
- False 
- True 
- True 
- '42'
- 1
- False
- false 
-error 
- true 
- true 
- error 
- [1,2]
- [1,1]
- error 
- True 
- error 

#.1 You have rented some movies for your kids: 
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?
class 
price_rate = 3
little_mer = 3
herc = 1 
bro = 5 
total_rate = (little_mer + herc + bro) * price_rate
total_rate

list = [3, 5, 1]
sum([n * 3 for n in list])

#.2 Suppose you're working as a contractor for 3 companies: 
# Google, Amazon and Facebook, they pay you a different rate 
# per hour. Google pays 400 dollars per hour, Amazon 380, 
# and Facebook 350. How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
##class
g_rate = 400
am_rate = 380 
fb = 350 

g_hours = 6
am_hours = 4
fb_hours = 10

paycheck = (g_rate * g_hours) + (am_rate * am_hours) + (fb_rate * fb_hours)
paycheck 

G = 400 * 6
A = 380 * 4
F = 350 * 10

Pay = G+A+F
print(Pay)

#3. A student can be enrolled to a class only 
# if the class is not full and the class schedule does not 
# conflict with her current schedule.

#Capacity 0 for not full, 1 for full
#Schedule 0 for not conflicted, 1 for conflict
class
class_is_not_full = True 
schedule_does_not_conflict = True 
enroll = class_is_not_full and schedule_does_not_conflict

class_capacity = input("Capacity 0 or 1")
capacity = int(class_capacity)
schedule = input("Schedule 0 or 1")
sched = int(schedule)
if capacity + sched < 1:
    print()

#4. A product offer can be applied only if people buys 
# more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.
class 
premium_member = True 
more_than_two_items = False 
coupon_not_expired = True

coupon_not_expired and (more_than_two_items or premium_member)

NEED COUPON REGARDLESS OF WHETHER MEMBER OR NOT


x = input("enter customer status")
premium = ("recieve discount")
not_prem = ("buy 2 items to recieve discount")

################################
username = 'codeup'
password = 'notastrongpassword'

#the password must be at least 5 characters
check_1 = len(password) >= 5


#the username must be no more than 20 characters
check_2 = len(username) <= 20

#the password must not be the same as the username
check_3 = username != password
