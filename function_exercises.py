#1Define a function named is_two. It should accept one input and return 
#True if the passed input is either the number or the 
#string 2, False otherwise.

def is_two(n):
    if n == 2 :
        return True
    else:
        return False

#2 Define a function named is_vowel. 
#It should return True if the passed string is a vowel, False otherwise.
def is_vowel(n):
    
    if n== 'a' or n== 'e' or n== 'i' or n== 'o' or n=='u':
        return True
    else:
        return False

#3 Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
#Use your is_vowel function to accomplish this.
def is_consonant(n):
    
    if n!= 'a' or n!= 'e' or n!= 'i' or n!= 'o' or n!='u':
        return True
    else:
        return False
#4. Define a function that accepts a string that is a word. 
#The function should capitalize the 
#first letter of the word if the word starts with a consonant.
def cap_first_con(word):
    for letter in word:
        if letter[0] not in['a','e','i','o','u']:
            return word.capitalize()
        else:
            return word

5. #Define a function named calculate_tip. 
#It should accept a tip percentage (a number between 0 and 1) 
#and the bill total, 
#and return the amount to tip.

def calculate_tip(b,t):
    return(b*t)

#6.Define a function named apply_discount. It should accept a original price, 
#and a discount percentage, 
#and return the price after the discount is applied.

def apply_discount(x,y):
    return float(x*y)


#7. Define a function named handle_commas. 
#It should accept a string that is a number that contains commas in it as input, 
#and return a number as output.

def handle_commas(x):
    return x.replace(',','')

#8.Define a function named get_letter_grade. It should accept a number and 
#return the letter grade associated with that number (A-F).