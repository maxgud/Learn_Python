types_of_people = 10

#okay so interpolation in python is a pain.
#the variable needs to be surrounded by %()s and 
#the end of the string needs to have % local()
#everything needs to be surrounded by ()
#much more work than ruby!!
x = ("There are %(types_of_people)s types of people." % locals())

binary = "binary"
do_not = "don't"
y = ("Those who know %(binary)s and those who %(do_not)s." % locals())

print(x)
print(y)

print("I said: %(x)s" % locals())
print("I also said: '%(y)s'" % locals())

hilarious = False
joke_evaluation = ("Isn't that joke so funny?! %(hilarious)s" % locals())


w = "This is the left side of..."
e = "a string with a right side."

print(w + e)