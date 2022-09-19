import hashmap

# create a map of state to abbrevation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# print out some cities
print('-' * 10)
print("NY State has: {}".format(hashmap.get(cities, 'NY')))
print("OR State has: {}".format(hashmap.get(cities, 'OR')))

# print out some states
print('-' * 10)
print(f"Michigan's abbreviation is {hashmap.get(states, 'Michigan')}")
print(f"Florida's abbreviation is {hashmap.get(states, 'Florida')}")

# do it by using states then cities dict
print('-' * 10)
print("Michigan has: {}".format(hashmap.get(cities, hashmap.get(states, 'Michigan'))))
print("Florida has: {}".format(hashmap.get(cities, hashmap.get(states, 'Florida'))))

# print every state abbreviation
print('-' * 10)
hashmap.list(states)

# print every city in a state
print('-' * 10)
hashmap.list(cities)

print('-' * 10)
state = hashmap.get(states, 'Texas')

if not state:
    print("Sorry, no Texas.")

# default value using ||= with the nil result
# can you do this in one line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print("The city for the state 'TX' is: {}".format(city))