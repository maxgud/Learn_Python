
formatter = "{} hmmm"+ "{} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "What what",
    "Whoa whoa",
    "The evening is spread out...",
    "Like a patient etherized on a table..."
))