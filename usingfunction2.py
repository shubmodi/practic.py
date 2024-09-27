def greeting(name):
    return getDestination(input((f'Hello { name }, where do you want adventure, mountain or beach \n')))
def getDestination(destination):
    if (input(f'Are you sure you want to go to { destination } ? If sure then press y or press any key \n')).strip().lower() == 'y':
        return getBudgetCalculated(destination)
def getValidInput (valueFor):
    while True:
        try:
            value = int(input(f'Please enter the {valueFor}'))
            return value
        except:
            print('Invalid Input, please enter the correct value')
def getBudgetCalculated( destination ):
    days = getValidInput('no of days')
    budget = getValidInput('amount of budget you spend for one day')
    if budget > 1000:
        print( f'You can afford the luxary {destination} adventure trip and your have to spend ',+ days*budget)
    elif budget > 500:
        print(f'You can afford the good {destination} adventure trip and your have to spend ',+ days*budget)
    elif budget > 200 :
        print(f'You can afford the budget-friendly {destination} adventure trip and your have to spend ',+ days*budget ,+"\n")
    else :
        print('You can not afford the adenture trip')
        exit()
    return '\n Thanks for contacting us...'
print(greeting(input('Hello sir, please enter you name \n').strip().title()))




