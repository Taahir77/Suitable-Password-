


# Requests password from user
user_password = input("Please enter your password: ")

# Initialises characteristics as False Booleans
have_length = False
up_case     = False
low_case    = False 
have_num    = False

# Asks user questions
question1 = input("Is your password more than 6 characters?: ")
question2 = input("Does your password contain at least 1 upper case?: ")
question3 = input("Does your password contain at least 1 lower case?: ")
question4 = input ("Does your password contain at least 1 digit?: ")

# Verifies password and changes Booleans
# If user answer yes, the Boolean is set to True
# No (or any other answer) keeps the Boolean as False
# Converts user's answer to lower case (.lower())
# Removes spaces before and after text (.strip())
# Does not matter if user inputs "YeS" or " yes " etc.

if question1.lower().strip() == ("yes"):
    have_length = True

if question2.lower().strip() == ("yes"):
    up_case     = True

if question3.lower().strip() == ("yes"):
    low_case    = True

if question4.lower().strip() == ("yes"):
    have_num    = True

# True == 1 and False == 0, allowing a total to be calculated
total = int(have_length + up_case + low_case + have_num) 


# If at least 3 answers are True, this tells the user their password is suitable
# If not, it tells the user it is not suitable
if total >= 3:
    print("This is a suitable password")   
else:
    print("This is NOT a suitable password")