Programing in Python instead
#Codeacademy

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

Unit 3rd - Lesson 2nd - Boolean Exzpressions

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



