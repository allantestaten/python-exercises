1. Conditional Basics

day_of_week = input()

if day_of_week == 'Monday':
    print ('Monday')
else:
    print('Not Monday')

    day_of_week = input()

if day_of_week == ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday',]:
    print ('Not Weekend')
else:
    print('Weekend')

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
2. 
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
while i <= 1000000:
    print(i)
    i *= i

i = 100
while i >= 5 :
    print(i)
    i -= 5

n = int(input())

for i in range(1, 11):
    print(n, 'x', i, '=', n*i) NEED TO FINISH 111111

n = int(input())
for n in range(0,n):
    if n < 1:
        n -=1
    else:
        print(n)

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

3. 
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

4.
n = int(input())
for i in range(1,2+n):
    if i < n+1:
        print(f'square:{i**2},cube:{i**3}') 
    else:
        print(f'Would you like to continue?')