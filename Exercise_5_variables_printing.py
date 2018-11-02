my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
name = "Spongebob Squarepants"
print("Who  %(name)s." % locals())

print("Let's talk about %(my_name)s." % locals())
print("He's %(my_height)s inches tall." % locals())
print("He's %(my_weight)s pounds heavy." % locals())
print("Actually that's not too heavy.")
print("He's got %(my_eyes)s eyes and %(my_hair)s hair." % locals())
print("His teeth are usually %(my_teeth)s depending on the coffee." % locals())

total = my_age + my_height + my_weight
print("If I add %(my_age)s, %(my_height)s, and %(my_weight)s I get %(total)s." % locals())