# This is a file a user can configure in order to have more control over the kinds of identities generated.
# This file *must* remain unchanged after you start seriously using idmas32.

# GENDER
# Examples:
# setting gender_male to 1 and gender_female to 1 means roughly half will be male and half will be female
# setting gender_male to 1 and gender_female to 0 means all will be male
# setting gender_mail to 99 and gender_female to 1 means roughly 99% will be male
gender_male=1
gender_female=1

# NATIONALITY
# The default values for nationality were chosen based roughly on how many millions of people live in the country
# Set every nationality you think you cannot be to 0.
# If, for example, you do not think you can be a Brazilian, then set it to 0.
nationalities=[['American',319],['Brazilian',203],['Mexican',120],['German',81],['French',65],['British',64],['Spanish',47],['Polish',38],['Canadian',23],['FrenchCanadian',8],['Australian',23],['Austrian',9],['SwissGerman',5]]
# These commonly have two surnames, so two surnames will be used instead of two first names.
twosurnames=set(['Brazilian','Mexican','Spanish'])

# AGE/BIRTHDAY
# The birthday information is given in unix time: seconds since 1970.
# According to the default settings, you were born between Jan 1, 1970 and Jan 1, 1995
birthday_lowerbound=0
birthday_upperbound=788918400
# Names are organized by gender and nationality. The dictionaries are initialized in names.py.
firstnames = { }
lastnames = { }
