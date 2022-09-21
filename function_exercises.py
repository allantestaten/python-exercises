#1Define a function named is_two. It should accept one input and return 
#True if the passed input is either the number or the 
#string 2, False otherwise.

def is_two(n):
    return n == 2 or n == '2'
  

#2 Define a function named is_vowel. 
#It should return True if the passed string is a vowel, False otherwise.
#def is_vowel(n):
    
    if n== 'a' or n== 'e' or n== 'i' or n== 'o' or n=='u':
        return True
    else:
        return False

def is_vowel(somestring):
    if type(somestring) == str:
        if len(somestring) == 1:
            return somestring.lower() in list('aeiou')
        else:
            return False
    else:
        return False

#3 Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
#Use your is_vowel function to accomplish this.
#def is_consonant(n):
    
    if n!= 'a' or n!= 'e' or n!= 'i' or n!= 'o' or n!='u':
        return True
    else:
        return False

def is_consonant(somestring):
    if type(somestring) == str:
        if len(somestring) == 1 and somestring.isalpha():
            return somestring.lower() not in list('aeiou')
        else:
            return False
    else:
        return False    
#4. Define a function that accepts a string that is a word. 
#The function should capitalize the 
#first letter of the word if the word starts with a consonant.
#def cap_first_con(word):
    for letter in word:
        if letter[0] not in['a','e','i','o','u']:
            return word.capitalize()
        else:
            return word
def cap_first_con(somestring):
    if type(somestring) == str:
        if is_consonant(somestring[0]):
            return somestring.capitalize()
        else:
            return somestring
    else:
        return somestring
    
5. #Define a function named calculate_tip. 
#It should accept a tip percentage (a number between 0 and 1) 
#and the bill total, 
#and return the amount to tip.

#def calculate_tip(b,t):
    #return(b*t)

def calculate_tip(bill, tip_percent = .15):
    return bill*tip_percent
    

# variable input = set number or value

#6.Define a function named apply_discount. It should accept a original price, 
#and a discount percentage, 
#and return the price after the discount is applied.

#def apply_discount(x,y):
    return float(x*y)

def apply_discount(orig_price, discount = 0.0):
    return orig_price - orig_price*discount


#7. Define a function named handle_commas. 
#It should accept a string that is a number that contains commas in it as input, 
#and return a number as output.

#def handle_commas(x):
    return x.replace(',','')

def hanlde_commas(fakenumber):
    if type(fakenumber) == str:
        return int(fakenumber.replace(',', ''))
    else:
        return fakenumber

#8.Define a function named get_letter_grade. It should accept a number and 
#return the letter grade associated with that number (A-F).
#def get_letter_grade(n):
    if n >= 90:
        return 'A'
    if n >= 80:
        return 'B'
    if n >= 70:
        return 'C'
    if n >= 60:
        return 'D' 
    else:
        return 'F'

def get_letter_grade(somegrade):
    if somegrade >= 90:
        return 'A'
    elif somegrade >= 80:
        return 'B'
    elif somegrade >= 70:
        return 'C'
    elif somegrade >= 60:
        return 'C'
    else:
        return 'F'

#9. Define a function named remove_vowels that accepts a string 
#and returns a string with all the vowels removed.
#def remove_vowels(word):
    for l in "aeiou":
        word = word.replace(l,"")
    return word

# class
def remove_vowels(word):
    new_word = ''
    for letter in word:
        if not is_vowel(letter):
            new_word += letter 
    return new_word 

#10. 
def normalize_name(name):
    newstring =''
    for letter in name:
        if letter.isidentifier() or letter == ' ':
            newstring +=letter
    return newstring.strip().lower().replace(' ', '_')

    #isidentifier (identifies identifier in string)
11. #11. Write a function named cumulative_sum that accepts a list of numbers 
#and returns a list that is the cumulative sum of the numbers in the list.
