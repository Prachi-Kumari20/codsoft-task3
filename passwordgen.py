import random
import string
print("Welcome to our Random Password Generator")

def my_func():
    
    length= int(input("Enter the length of password: "))
    lowerdata = string.ascii_lowercase
    upperdata = string.ascii_uppercase
    digitsdata = string.digits
    symbolsdata = string.punctuation
    combine = lowerdata + upperdata + digitsdata + symbolsdata
    D = random.sample(combine,length)
    password ="".join(D)
    print(password)
    my_func()
my_func()

