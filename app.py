first_name = input ("Enter first name: ")
last_name = input ("Enter last name: ")
email = input ("Enter Email: ")
import string
import random
a = first_name
first_two_chars = a[ :2]
b = last_name
last_two_chars = b[-2: ]
def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
print ("Your password is:" + first_two_chars + last_two_chars + randomString())
answer = input("Are you satisfied with the password?""Enter Yes or No:")
if answer == "Yes":
    print (first_name, last_name, email)
else:
    new_password = input ("Choose a password, password must be more than 7 characters.Enter Password:")     
    l=len(new_password)
    if l >= 7:
        print(first_name, last_name, email)
    elif l < 7:
        input("Enter a new password equal to or greater than 7 in length:")
        print(first_name, last_name, email)
    
    
