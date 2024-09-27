def get_user_name(name):
    return name

# Name = get_user_name()
name = get_user_name(input('hello, user enter your name : '))
msg = f' hello, { name }, where you want to travel'
print(msg)

def user_destination(destination):
    return destination

Destination = user_destination(input(f'hello, {name} enter your destination : '))
msg = f'{name} are you sure you want to go {Destination} '
print(msg)








