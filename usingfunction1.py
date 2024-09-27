def get_user_name(name):
    return name
name = get_user_name(input('hello sir, enter your name :\n '))
msg = f' hello, { name }, where you want to travel \n'
print(msg) 
def user_destination(destination):
    return destination
Destination = user_destination(input(f'hello, {name} enter your destination :\n '))
msg =input (f'are you sure you want to go {Destination} :\n ')
if msg.lower() == 'yes' :
    print(f'Thankyou for choosing {Destination}\n')
else:
    print(f'thankyou for coming \n')
def user_budget(budget):
    try:
        return int(budget)
    except ValueError:
        return 'please enter in numeric/n'   
Budget = user_budget(int(input("Enter your budget :\n ")))
msg = f'your budget is {Budget} \n '
print(msg)
def no_of_days(days):
    try:
        return int(days)
    except ValueError:
        return 'please enter in numeric \n'   
Days= no_of_days(int(input("enter the no of days you want to stay :\n ")))
msg = f'your budget is \n', + Budget* Days 
print(msg)
Budget = Budget*Days
if Budget <= 500:
    print(f'you have not enough budget to acquire trip to {Destination}')
elif Budget <=1000:
    print(f'you have budget to acquire trip to {Destination} ')
else:
    print(f"you unlock the facilities in {Budget}")
     