#declaring age and height as integer and float respectively
Age = 33
Height = 1.50

#declaring a variable as complex number can be done in two ways
complex_number = complex(2,3)#2 is real number and 3 is the imaginary
# or
COMPLEX_number = 2+3j


# using user input as base and height 
base = float(input('enter a number for base'))
heigth = float(input('enter a number for height'))

#area of triangle is calculated using (0.5*base*height)
area = float(0.5 * base * heigth)
print(area)

#using user input to calculate perimeter
#perimeter = side a+ side b+ side c

side_a = float(input('enter a number(side a)'))
side_b =float(input('enter a number(side b)'))
side_c = float(input('enter a number(side c)'))

perimeter = (side_a)+(side_b)+(side_c)
print(perimeter)

#calculating area of rectangle
length = float(input('enter a number for length'))
width = float(input('enter a number for width'))
area_of_rectangle = length*width
perimeter_of_rectangle = 2*(length+width)
print('the area is',area_of_rectangle )
print('the perimeter is',perimeter_of_rectangle)


#calculating radius and circumference of a circle
# measurement in meters
import math
Pi = math.pi
radius = float(input('enter a radius')) 
area_of_circle = Pi*radius**2
circum_of_cirlce = 2*Pi*radius

print(area_of_circle)
print(circum_of_cirlce)

#calculating slope
#slope = y = mx+b


#checking if python and dragon have different length
pyt=len('python')
drg=len('dragon')
print(pyt!=drg)

#checking if a word is in a text
sentence="I hope this course is not full of jargon"
word= "jargon"
if word in sentence:
 print(f"the word '{word}' is found in the text")
else:
 print('word not found in text')

#checking to see if int(9.8) is equal to 10
 print(int(9.8)==10)

#calculating pay
hours_worked = float(input('enter hours worked'))
pay_rate=float(input('enter hourly rate'))

total_pay=hours_worked*pay_rate
print(f"total pay for {hours_worked}hours is {total_pay}")

#Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live



def seconds_lived(age):
  seconds_per_year = 31536000
  total_seconds = float(age) * seconds_per_year
  return total_seconds
age = int(input("Enter your age: "))  
total_seconds_lived = seconds_lived(age)
print(f"Total seconds lived for a person of age {age}: {total_seconds_lived:.2f}")
