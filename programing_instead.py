Programing instead

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



