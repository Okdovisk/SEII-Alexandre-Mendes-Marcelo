message = 'Hello World'

print(message.upper())

print(len(message))

print(message.lower())

print(message[:11])

print(message.count('l'))
print(message.find('World'))

new_message = message.replace('World', 'Universe')

print(new_message)

greetings = 'Hello'

name = 'Michael'

#message = greetings + ', ' + name + '. Welcome!'
#message = '{}, {}. Welcome!'.format(greetings, name)
message = f'({greetings}, {name}. Welcome!)'

print(message)
#print(dir(name))
#print(help(str.lower))