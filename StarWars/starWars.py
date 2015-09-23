__author__ = 'Devin Simoneaux'

# CIS-125
# Star Wars Name
#
# The program takes the users name and converts it to the user's specific Star Wars name.

# Input from User
fname = input("What is your first name? ")
lname = input("What is your last name? ")
maiden = input("What is your mother's maiden name? ")
city = input("In which city were you born? ")

# Calculate Star Wars first and last name using the input
swfname = lname[0:4] + fname[0:3]
swlname = maiden[0:3] + city[0:4]

# Output the Star Wars name
print("Your Star Wars name is ", swfname, swlname)