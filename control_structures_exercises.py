#1. Conditional Basics

# can make list with abbreviations, and would then use In, 
# add lower to catch punctuation differences of same word 

from re import A


day_of_week = input("Enter a day of the Week")

if day_of_week.lower() == 'Monday':
    print ('Monday')
else:
    print('Not Monday')

day_of_week = input()

if day_of_week == ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday',]:
    print ('Not Weekend')
else:
    print('Weekend')
#classroom
hours_worked = 40
hourly_rate = 20

if hours_worked <= 40:
    paycheck = hours_worked * hourly_rate
    print(paycheck)
elif hours_worked > 40:
    print("OVERTIME!")
    ot_hours = (hours_worked - 40)
    ot_rate = hour_rate * 1.5

    ot_paycheck = (40 * hourly_rate) + (ot_hours * ot_rate)

total_hours = input()
hours = 40
ot_hours = int(total_hours) - hours
rate = 30
check = hours * rate
ot = check + (1.5 * int(ot_hours) * rate)

if int(total_hours) <= 40:
    print(f'Paycheck: ${check}')
else:
    print(f'paycheck:${ot}')
#2. 
i = 5 
while i <= 15:
    print(i)
    i += 1 

i = 0
while i <= 100:
    print(i)
    i += 2 

i = 100
while i >= -10:
    print(i)
    i -= 5

i = 2
while i <= 1_000_000:
    print(i)
    i = i**2

i = 100
while i >= 5 :
    print(i)
    i -= 5

n = int(input())
# class print statement 
user_num = input('Enter a number: ')
    print(f'{user_num} x {x} = {int(user_num)* x}')

for i in range(1, 11):
    print(n, 'x', i, '=', n*i)


n = int(input())

for i in range(1, 10):
    print(str(i)*i)

# class 
while True:
    user_num = input('Please enter a positive number:') 

    if user_num.isdigit() == True:
        print('This is a digit')
    if int(user_num) > 0:
        print('The number is positive!')
        break 
user_num = int(user_num)
for i in range(user_num, 0, -1):
    print(i)


# Class solution 

while True:
    user_num = input('Please enter a positive number:') 

    if user_num.isdigit() == True:
        print('This is a digit')
    if int(user_num) > 0:
        print('The number is positive!')
        break 
user_num = int(user_num)
for i in range(int(user_num)+1):
    print(i)

n = int(input())
for n in range(0,n):
    if n < 1:
        n -=1
    else:
        print(n)

#classroom solution
while True:
    user_num = input('Please enter an odd number between 1 and 50:') 

    if user_num.isdigit():
        print('This is a digit')
        if int(user_num) % 2 != 0:
            print('The number an odd number!')
            if (int(user_num)> 1) and (int(user_num) < 50):
                print('This number is between 1 and 50')
                break
user_num = int(user_num)
for i in range (1,50):
    if i == user_num:
        print('Skipped this number')
        continue 
        
    if i % 2 == 1:
        print(i)

user_num = int(user_num)
for i in range(int(user_num)+1):
    print(i)

n = int(input())
for i in range(1,50):
    if n < 1 or n > 50:
        print('Enter number between 1 and 50')
        
    if i == n:
        print(f'Yikes! Skipping this number:{i}')
        continue 
        
    if i % 2 !=0:
        print (f'Here is an odd number:{i}')
    

for n in range(1,101):
    print(n)
    if n>100:
        break

#3. 
# class 
for i in range(1,101):
    if i % 15 == 0:
        print('FizzBuzz')
        continue 
    if i % 3 = 0 
        print('Fizz')
        continue 
    if i % 5 == 0: 
        print ('Buzz')
        continue 
    print (i)

for n in range(1,101):
    if (n % 3 == 0):
        print('Fizz')
    else:
        print(n)

for n in range(1,101):
    if (n % 5 == 0):
        print('Fizz')
    else:
        print(n)

for n in range(1,101):
    if (n % 5 == 0) and (n % 3 == 0):
        print('Fizz')
    else:
        print(n)

#4.
n = int(input())
for i in range(1,2+n):
    if i < n+1:
        print(f'square:{i**2},cube:{i**3}') 
    else:
        print(f'Would you like to continue?')
#classroom
while True:  
    user_num = int(input('Enter an integer: '))
    for i in range(1, user_num+1):
    print(f'{i} |{i**2} {i**3}')
    user_yn: input('Would you like to continue? (y/n): ')
    if user_yn.lower() !='y':
        break

#5. 
    grade = int(input('Enter an integer: '))
    for i in range(0,100):
        if grade >=88:
            print('A')'
        elif grade >= 80
            print('B')
        elif grade >= 67
            print('C')
        elif grade >= 60 
            print ('D')
        else:
            print('F')
            
    user_yn: input('Would you like to continue? (y/n): ')
    if user_yn.lower() !='y':
        break

#6Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author,
#  and genre. Loop through the list and print out information about each book.

books = [{'title': 'title111', 'author': 'author1', 'genre': 'genre1'},
 {'title': 'title222', 'author': 'author1', 'genre': 'genre2'},
 {'title': 'title333', 'author': 'author2', 'genre': 'genre2'},
 {'title': 'title444', 'author': 'author3', 'genre': 'genre2'}]

 for book in books:
    print(book)

    user_genre = input('Enter a genre: ')

    for book in books:
    if book['genre'] == user_genre:
        book['title']