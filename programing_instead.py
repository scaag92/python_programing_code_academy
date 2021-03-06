Programing in Python instead
#Codeacademy

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

WIKI
How to install pip on MacOS

sudo easy_install pip

Or in other cases
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - 1st Lesson:
my_name = "Cristian"
print("Hello and welcome " + my_name + "!")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - 2nd Lesson., How to make comments:
# Buena los perros
persnickety_count = 0

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - 3rd - 4th Lesson, Print

print ("Cristian")

print ('Cristian')

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - 5th Lesson: Variables =

# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "Caldo de Costilla"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = "Pollito asado"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner

# Printing out dinner
print("Calentado Paisa:")
print(meal)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - 6th Lesson: Int & Float Variables 

# Define the release and runtime integer variables below:

release_year_int = 1998
runtime_int = 192

# Define the rating_out_of_10 float variable below: 

rating_out_of_10_float = 1.55

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - 7th Lesson: Numbers

# Define the release and runtime integer variables below:

relase_year = 2001 
runtime = 2


# Define the rating_out_of_10 float variable below: 

rating_out_of_10 = 1.5

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - 8th Lesson: Calculations

int_a = 5
int_b = 10
print( int_a / int_b )

print (25 * 68 + 13 / 28)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - 9th Lesson: Changing Numbers

quilt_width = 8 
quilt_length = 12

print ( quilt_width * quilt_length )

quilt_length = 8

print ( quilt_width * quilt_length )

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - 10th Lesson: Exponents

# Calculation of squares for:
# 6x6 quilt
print (6 ** 2)
# 7x7 quilt
print (7 ** 2)
# 8x8 quilt
print (8 ** 2)
# How many squares for 6 people to have 6 quilts each that are 6x6?
print (6 ** 4 ) 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - 11th Lesson: Modulo

# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)

# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)

# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - 12th Lesson: Concatenation

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1 + string2 + string3 + string4 + string5 + string6

#print(message)

print (message)

++++++++

full_text = greeting_text + " " + question_text

# Prints "Hey there! How are you doing?"
print(full_text)

++++++++

birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"

# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2

# Prints "I am 10 years old today!"
print(full_birthday_string)

# If we just want to print an integer 
# we can pass a variable as an argument to 
# print() regardless of whether 
# it is a string.

# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - 13th Lesson: Plus Equals

total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
total_price += nice_sweater

fun_books = 20.00
total_price += fun_books

# Update total_price here:

print("The total price is", total_price)

+++++++++

hike_caption = "What an amazing time to walk through nature!"

# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - 14th Lesson: Multi-line Strings

# Assign the string here
to_you = '''
Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
'''
print(to_you)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - 15th Lesson: Review

my_age = 26
half_my_age = my_age / 2
greeting = "Hello Every body, my name is "
name = "Cristian, "
greeting_with_name = greeting + name + "I have " + str(my_age)
print (greeting_with_name)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 1 - Script: Furniture Store

lovely_loveseat_description = '''
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. 
'''
lovely_loveseat_price = 254.00

stylish_settee_description  = '''
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
'''
stylish_settee_price = 180.50

luxurious_lamp_description = '''
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
'''
luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax 

print ("Customer One Items:")
print (customer_one_itemization)
print ("Customer One Total:")
print (customer_one_total)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Uni 2nd -  Lesson 2 - Functions
 
def sing_song():
  print("You may say I'm a dreamer")
  print("But I'm not the only one")
  print("I hope some day you'll join us")
  print("And the world will be as one")
  
#call sing_song() below:


sing_song()
sing_song()

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 2dn - Lesson 3rd - Functions

def loading_screen():
  print("This page is loading...")

  loading_screen()

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 2nd - Lesson 4th - Whitespaces

def about_this_computer():
  print("This computer is running on version Everest Puma")
print("This is your desktop")

about_this_computer()

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 2nd - Lesson 5th - Parameters

def mult_two_add_three(number):
  print(number*2 + 3)
  
# Call mult_two_add_three() here:
mult_two_add_three(10)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 2nd - Lesson 6th - Multiple Parameters

def mult_x_add_y(number, x, y):
  print(number*x + y)
  
mult_x_add_y(5, 2, 3)
mult_x_add_y(1, 3, 1)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 2nd - Lesson 7th - Keyword Arguments

def greet_customer(grocery_store, special_item):
    print("Welcome to "+ grocery_store + ".")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")


# Define create_spreadsheet():
def create_spreadsheet(title, row_count):
  print("Creating a spreadsheet called " + title + " with " + str(row_count) + " rows")
	
# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Aplications", 10)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 2nd - Lesson 8th - Returns

def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age
  
my_age = calculate_age(2049, 1993)
print(my_age)

dads_age = calculate_age(2049, 1953)
print(dads_age)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 2nd - Lesson 9th - Multiple Returns

def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = margin + target
  return low_limit, high_limit

low, high = get_boundaries(100, 20)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 2nd - Lesson 10th - Scope

current_year = 2048

def calculate_age(birth_year):
  age = current_year - birth_year
  return "You're age is: " + str(age) + "."

age = calculate_age(1970)
print(age)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 2nd - Lesson 11th - Scope

def repeat_stuff(stuff, num_repeats=10):
  return stuff*num_repeats

lyrics = repeat_stuff("Row ", 2) + "Your Boat. "
song = repeat_stuff(lyrics)

print(song)



train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 2 - Script: Physics Teacher

#Function to convert from Fahrenheit to Celsius
def f_to_c(f_temp):
  c_temp	= (f_temp - 32) * 5/9
  return c_temp
f100_in_celsius = f_to_c(100)

#Function to convert from Celsius to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)

#Function to get force from mass and acceleeration
def get_force(mass,acceleration):
	mass = mass * acceleration
  return mass 
train_force = get_force(train_mass,train_acceleration)
print("The GE train supplies" + train_force + "Newtons of force.")

#Function to get energy from mass and constant speed of light
def get_energy(mass,c = 3*10**8):
  mass = mass * c
	return mass
bomb_energy= get_energy(bomb_mass)
print("A 1kg bomb supplies" + bomb_energy + "Joules.")

def get_work(mass, acceleration, distance):
      force = get_force(mass, acceleration)
      work = force * distance
      return result
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does" + train_work + "Joules of work over" + train_distance + "meters.".)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 2 - CODE CHALLENGE: PYTHON FUNCTIONS

AVERAGE

# Write your average function here:

# Uncomment these function calls to test your average function:
#print(average(1, 100))
# The average of 1 and 100 is 50.5
#print(average(1, -1))
# The average of 1 and -1 is 0
def average(num1, num2):
  num1 += num2
  result = num1 / 2
  return result

TENTH POWER

# Write your tenth_power function here:

# Uncomment these function calls to test your tenth_power function:
#print(tenth_power(1))
# 1 to the 10th power is 1
#print(tenth_power(0))
# 0 to the 10th power is 0
#print(tenth_power(2))
# 2 to the 10th power is 1024
def tenth_power(num):
  return num ** 10

BOND

# Write your introduction function here:

# Uncomment these function calls to test your introduction function:
#print(introduction("James", "Bond"))
# should print Bond, James Bond
#print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou
def introduction(first_name, last_name):
  	return last_name + "," + " " +  first_name + " " + last_name
  
SQUARE ROOT

# Write your square_root function here:

# Uncomment these function calls to test your square_root function:
#print(square_root(16))
# should print 4
#print(square_root(100))
# should print 10
def square_root(num):
  return num**(1/2)

num1 = square_root(8)
print(num1)

TIP

# Write your tip function here:
  
# Uncomment these function calls to test your tip function:
#print(tip(10, 25))
# should print 2.5
#print(tip(0, 100))
# should print 0.0

def tip(total, percentage):
  tip = (( total * percentage ) / 100 )
  return tip
  
WIN PERCENTAGE

# Write your win_percentage function here:

# Uncomment these function calls to test your win_percentage function:
#print(win_percentage(5, 5))
# should print 50
#print(win_percentage(10, 0))
# should print 100

def win_percentage(wins, losses):
  total = (wins + losses)
  wins_percentage = wins * 100 / total
  return wins_percentage


FIRST THREE MULTIPLES

# Write your first_three_multiples function here:
def first_three_multiples(num):
  print(num)
  print(num*2)
  print(num*3)
  return num*3

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

DOG YEARS

# Write your dog_years function here:
def dog_years(name, age):
  age = age * 7
  return name + ", you are " + str(age) + " years old in dog years"
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"


REMAINDER

# Write your remainder function here:
def remainder(num1, num2):
  return (2*num1)%(num2/2)

# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

LOTS OF MATH

# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
  print(a + b)
  print(d - c)
  print((a + b)*(d - c))
  return (((a + b)*(d - c))%a)
  
# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
#print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3 - CODE CHALLENGE: PYTHON FUNCTIONS

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 2nd - BOOLEAN EXZPRESSIONS

# My dog is the cutest dog in the world.
example_statement = "No"

# Dogs are mammals.
statement_one = "Yes"

# My dog is named Pavel.
statement_two = "Yes"

# Dogs make the best pets.
statement_three = "No"

# Cats are female dogs.
statement_four = "Yes"

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 3rd - RELATIONAL OPERATORS: EQUALS AND NOT EQUALS

# Statement one:
# (5 * 2) - 1 == 8 + 1
statement_one = True

#Statement two:
# 13 - 6 != (3 * 2) + 1
statement_two = False

#Statement three:
# 3 * (2 - 1) == 4 - 1
statement_three = True

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 4th - BOOLEAN VARIABLES

my_baby_bool = "true"
print(type(my_baby_bool))
my_baby_bool_two = True
print(type(my_baby_bool_two))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 5th - IF STATEMENTS

def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"
  if user_name != "Dave":
    return "I know it is you Dave! Go away!"
  
# Enter a user name here, make sure to make it a string
user_name = "angela_catlady_87"

print(dave_check(user_name))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 6th - RELATIONAL OPERATORS II

def greater_than(x, y):
	if x > y:
		return x
	if y > x:
		return y
	if y == x:
		return	"These numbers are the same"

print(greater_than(3, 3))


def graduation_reqs(credits):
	if credits >= 120:
		return "You have enough credits to graduate!"

print(graduation_reqs(120))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 7th - RELATIONAL OPERATORS II

def greater_than(x, y):
	if x > y:
		return x
	if y > x:
		return y
	if y == x:
		return	"These numbers are the same"

print(greater_than(3, 3))


def graduation_reqs(credits):
	if credits >= 120:
		return "You have enough credits to graduate!"

print(graduation_reqs(120))


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 8th - BOOLEAN OPERATORS: AND


statement_one = False

statement_two = True

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 8th - BOOLEAN OPERATORS: OR

statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

def graduation_mailer(gpa, credits):
  if (gpa >= 2.0) or (credits >= 120):
  	return True

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 9th - BOOLEAN OPERATORS: NOT

statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and (not credits >= 120):
    return "You do not have enough credits to graduate."
  if (not gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if (not gpa >= 2.0) and (not credits >= 120):
    return "You do not meet either requirement to graduate!"

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 10th - ELSE STATEMENTS 

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 11th - ELSE STATEMENTS 

def grade_converter(gpa):
  grade = "F"
  
  if gpa >= 4.0:
    grade = "A"
  elif gpa >= 3.0:
    grade = "B"
  elif gpa >= 2.0:
    grade = "C"
  elif gpa >= 1.0:
    grade = "D"
    
  return grade

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 12th - TRY AND EXCEPT STATEMENTS 

def raises_value_error():
  try:
  	raise ValueError
  except ValueError:
    print("You raised a ValueError!")

raises_value_error()

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 13th - TRY AND REVIEW

def applicant_selector(gpa, ps_score, ec_count):
  if (gpa>=3.0) and (ps_score>=90) and (ec_count>=3):
  	return "This applicant should be accepted."
  elif (gpa>=3.0) and (ps_score>=90) and not (ec_count>=3):
    return "This applicant should be given an in-person interview."
  elif not(gpa>=3.0) or not (ps_score>=90) or not (ec_count>=3):
    return "This applicant should be rejected."

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 14th - TRY AND EXCEPT STATEMENTS 

def ground_shipping_cost(weight):
	if (weight<=2):
		cost = weight * 1.50 + 20
	elif (weight>2) and (weight<=6):
		cost = weight * 3.0 + 20
	elif (weight>6) and (weight<=10):
		cost = weight * 4.0 + 20	
	elif (weight>10):
		cost = weight * 4.75 + 20
	return cost

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 3rd - Lesson 14th - CODE CHALLENGE: CONTROL FLOW 

IN FLOW

# Write your in_range function here:
def in_range(num, lower, upper):
  if (num>=lower) and (num<=upper):
    return True
  else:
    return False
# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False


MOVIE REVIEW
# Write your movie_review function here:
def movie_review(rating):
  if (rating<=5):
    return "Avoid at all costs!"
  elif (rating>5) and (rating<9):
    return "This one was fun."
  elif (rating>=9):
    return "Outstanding!"
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."
print(movie_review(8))


TWICE AS LARGE
# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if (num1 > num2 * 2):
    return True
  else:
    return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True


POWER
# Write your large_power function here:
def large_power(base, exponent):
  if (base ** exponent > 5000):
    return True
  else:
    return False
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False


DIVISIBLE BY TEN

# Write your divisible_by_ten function here:
def divisible_by_ten(num):
    if(num % 10 == 0):
        return True
    elif (num % 10 != 0):
        return False
# Uncomment these function calls to test your divisible_by_ten function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False


# Write your divisible_by_ten function here:
def divisible_by_ten(num):
    if(num % 10 == 0):
        return True
    else:
        return False
# Uncomment these function calls to test your divisible_by_ten function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

MAX NUMBER

# Write your max_num function here:
def max_num(num1, num2, num3):
    if (num1>num2) and (num1>num3):
        return num1
    elif (num1==num2) or (num1==num3):
        return ("It's a tie!")
    elif (num2>num1) and (num2>num3):
        return num2
    elif (num2==num1) or (num2==num3):
        return ("It's a tie!")
    elif (num3>num1) and (num3>num2):
        return num3
    else:
        return ("It's a tie!")
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"

ALWAYS FALSE

# Write your always_false function here:

def always_false(num):
    if (num >= 0):
        return False
    else:
        return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False


NOT EQUAL

# Write your not_sum_to_ten function here:

def not_sum_to_ten(num1, num2):
    if (num1 + num2 != 10):
        return True
    else:
        return False

# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False


SAME NAME

# Write your same_name function here:

def same_name(your_name, my_name):
    if (your_name == my_name):
        return True
    else:
        return False

# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Unit 4th - Lesson 1st - WHAT IS A LIST? 

heights = [61, 70, 67, 64, 65]

broken_heights = [65, 71, 59, 62]


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4th - Lesson 2nd - LISTS II

ints_and_strings = [1, 2, 3, 'four', 'five', "Hola"]
sam_height = ['Sam', 67]



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4th - Lesson 3rd -  LIST OF LISTS

heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]
ages = [['Aaron', 15], ['Dhruti', 16]]

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4th - Lesson 4th -  ZIP

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']
names_and_dogs_names = zip(names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4th - Lesson 5th -  EMPTY LIST

my_empty_list = []

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4th - Lesson 6th -  GROWING A LIST: APPEND

orders = ['daisies', 'periwinkle']
print(orders)
orders.append('tulips')
orders.append('roses')
print(orders)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4th - Lesson 7th -  GROWING A LIST: PLUS (+)

orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

# Create new orders here:

new_orders = orders + ['lilac', 'iris']

broken_prices = [5, 3, 4, 5, 4] + [4]

print(new_orders)
print(broken_prices)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4th - Lesson 8th -  RANGE I

list1 = range(9)
range1 = range(8)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4th - Lesson 9th - RANGE II

list1 = range(5, 15, 3)
list2 = range(0, 40, 5)
print(list(list1))
print(list(list2))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4th - Lesson 10th - REVIEW

first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
age = []
age.append(42)
all_ages = age + [32, 41, 29]
name_and_age = zip (first_names, all_ages)
ids = range(0, 4)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4th - Lesson 10th - PYTHON GRADEBOOK

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
subjects.append('computer science')
grades.append(100)
gradebook = list(zip(subjects, grades))
gradebook.append(('visual arts', 93))
print(list(gradebook))
full_gradebook=list(zip(gradebook, last_semester_gradebook))
print(full_gradebook)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4th - Lesson 10th - PYTHON GRADEBOOK



=======
Unit 4rd - Lesson 1st - LENGTH OF A LIST

list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 3rd - SELECTING LIST ELEMENTS I

employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']

index4 = employees[4]

print(len(employees))

print(employees[2])

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 4rd - SELECTING LIST ELEMENTS II

shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']

print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(element5 + last_element)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 5th - SLICING LISTS

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]
print(beginning)

middle = suitcase[2:4]
print(middle)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 6th - SLICING LISTS II

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]
end = suitcase[-2:]

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 7th - COUNTING ELEMENTS IN A LIST

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 8th - SORT LIST I

### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:

### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()
print(sorted_cities)
addresses.sort()
print(addresses)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 9th - SORT LIST II

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games)
print(games_sorted)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 9th - REVIEW

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count('twin bed')
inventory.sort()


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 9th - LEN.S SLICE   



toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2 ]
num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizzas = list(zip(prices, toppings))
print(pizzas)

pizzas.sort()
print(pizzas)

cheapest_pizza = pizzas[0]

priciest_pizza = pizzas[-1]

print("I will have your" + str(priciest_pizza) + "pizza!")

three_cheapest = pizzas[0:3]
print(three_cheapest)

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4th - Lesson 12th - LEN.S SLICE  

num_two_dollar_slices = 






---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4th - 2nd DOUBLE INDEX

#Write your function here
def double_index(lst, index):
  if index < len(lst):
    lst[index] = lst[index] * 2
  return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 3rd - REMOVE MIDDLE

#Write your function here
def remove_middle(lst, start, end):
    list1 = lst[:start]
    list2 = lst[end+1:]
    list1 = list1 + list2
    return list1

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 4th - MORE THAN N

#Write your function here
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else: 
    return False
  

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 5th - MORE FREQUENT ITEM

#Write your function here
def more_frequent_item(lst, item1, item2):
    if lst.count(item1) > lst.count(item2) or lst.count(item1) == lst.count(item2):
        return item1
    return item2

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 6th - MIDDLE ITEM

MY CODE

#Write your function here
def middle_element(lst):
    count = len(lst)
    print(count)
    if count % 2 == 1:
        middle = ((count-1)/2)
        return lst[middle]
    else:
        middle = ((lst[(count/2)-1]) + (lst[count/2])) / 2
        print(middle)
#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4]))
middle_element([5, 2, -10, -4])



CODE ACADEMY CODE
#Write your function here
def middle_element(lst):
    if len(lst) % 2 == 0:
        sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
        return sum / 2
    else:
        return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4]))



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 7th - MIDDLE ITEM

#Write your function here

def append_sum(lst):
    el1 = lst[-1] + lst[-2]
    lst.append(el1)
    el1 = lst[-1] + lst[-2]
    lst.append(el1)
    el1 = lst[-1] + lst[-2]
    lst.append(el1)
    return(lst)

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 8th - LARGER LIST

#Write your function here
def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
        return lst1[-1]
    else:
        return lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 9th - COMBINE SORT

#Write your function here
def combine_sort(lst1, lst2):
    lst1 = lst1 + lst2
    lst1.sort()
    return lst1


#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 10th - APPEND SIZE 

#Write your function here
def append_size(lst):
    lst.append(len(lst))
    return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 4rd - Lesson 11th - APPEND SIZE 
MY CODE

def every_three_nums(start):
    if start < 100:
        list = range(start, 101, 3)
        return(list)
    else:
        list = []
        return  list

print(every_three_nums(91))

CODEACADEMY

#Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))


------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 5th - Lesson 1st - INTRODUCTION 

dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
  print(breed)
  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 5th - Lesson 2nd - CREATE A FOR LOOP 


board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
  print(game)
  
for sport in sport_games:
  print(sport)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 5th - Lesson 3rd - USING RANGE IN LOOPS

promise = "I will not chew gum in class"
for i in range(5):
  print(promise)
  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 6th - Lesson 4th -  INFINITE LOOPS

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  #students_period_A.append(student)
  students_period_B.append(student)
  print(student)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 6th - Lesson 5th - BREAK

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'

for breeds in dog_breeds_available_for_adoption:
  print(breeds)
  if breeds == dog_breed_I_want:
    print("They have the dog I want!")
    break
  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 6th - Lesson 6th - CONTINUE

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i < 21:
    continue
  print(i)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 6th - Lesson 7th - WHILE LOOPS

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
  
print(students_in_poetry)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 6th - Lesson 8th - NESTED LOOPS

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  for sold in location:
    scoops_sold += sold
  
print(scoops_sold)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 6th - Lesson 9th - LIST COMPREHENSIONS

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = []

for height in heights:
  if height > 161:
    can_ride_coaster.append(height)
print(can_ride_coaster)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 6th - Lesson 10th -  MORE LIST COMPREHENSIONS

celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = []

for cels in celsius:
  temperature_in_fahrenheit = cels * 9/5 + 32
  fahrenheit.append(temperature_in_fahrenheit)
  
print(fahrenheit)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 6th - Lesson 11th - REVIEW

single_digits = [0, 1, 2, 3, 4, 5, 6 ,7 ,8 ,9]
squares = []
cubes = []
index = 0

for digit in single_digits:
  sqdigit = single_digits[index] **2
  squares.append(sqdigit)
  index += 1
print(squares)

index = 0

for digit in single_digits:
  cudigit = single_digits[index] **3
  cubes.append(cudigit)
  index += 1

print(cubes)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unit 6th - Lesson 12th - CARLYS CLIPPERS

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for pr in prices:
  total_price += pr

average_price = total_price / len(prices) 

print("Average Haircut Price: " + str(average_price))

new_prices=[]

for pr in prices:
  number = pr -5
  new_prices.append(number)

print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)): 
  total_revenue += prices[i] * last_week[i]

print("Total Revenue: " + str(total_revenue))
average_daily_revenue = total_revenue / 7 
print("Average daily revenue " + str(average_daily_revenue))

cuts_under_30=[]

for i in new_prices:
  if i > 30:
    cuts_under_30=[hairstyles[i] , new_prices[i]]

print(cuts_under_30)






