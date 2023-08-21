# python3 /Users/vivycahyani/Desktop/Belajar/kaggle-python/4-lists.py

primes = [2, 3, 5, 7]

planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'],  # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

my_favourite_things = [32, 'raindrops on roses', help]
# (Yes, Python's help function is *definitely* one of my favourite things)

# Elements at the end of the list can be accessed with negative numbers, starting from -1
planets[0]
planets[1]
planets[-1]
planets[-2]
print(planets[-2])

# SLICING
# What are the first three planets? We can answer this question using slicing
planets[0:3]
print(planets[:3])

# All the planets except the first and last
planets[1:-1]
# The last 3 planets
planets[-3:]
planets[3] = 'Malacandra'
print(planets)
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# That was silly. Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars', ]

# How many planets are there?
len(planets)
# The planets sorted in alphabetical order
sorted(planets)

primes = [2, 3, 5, 7]
sum(primes)

max(primes)

x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)

# x.bit_length
# <function int.bit_length()>
# To actually call it, we add parentheses:
x.bit_length()

# Pluto is a planet darn it!
planets.append('Pluto')
print(planets)

# list.pop removes and returns the last element of a list:

planets.pop()
print(planets)

planets.index('Earth')
print(planets.index('Earth'))

# To avoid unpleasant surprises like this, we can use the in operator to determine whether a list contains a particular value:

# Is Earth a planet?
"Earth" in planets
# Is Calbefraques a planet?
print("Calbefraques" in planets)

t = (1, 2, 3)
t = 1, 2, 3  # equivalent to above
print(t)

x = 0.125
print(x.as_integer_ratio())

numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

a = 1
b = 0
a, b = b, a
print(a, b)
