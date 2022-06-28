from Functions import *
# Setup
running = True
tips = 'tips.pkl'
dict = pickle_out(tips)
people_at_work = []
test = False

# interface
print('To get out of any loop type "done"')
print('Type "Options" to see available commands')
while running:

    decision = input('What do you want to do? ').lower()
    if decision == 'done':
        break
    elif decision == 'clear':
        sure = input('Are you sure you want to clear? ')
        if sure == 'yes' or 'y':
            pickle_save(tips, {})
            dict = pickle_out(tips)
            print('The data has been cleared')

            dict = setup()
        else:
            print('The clear has been stopped')

    elif decision == 'declare':
        people = []
        person = ''
        if len(people_at_work):
            peopleWork = input('Wanna use the list of people at work? ').lower()
            if peopleWork == 'yes' or 'y':
                people = people_at_work

        else:
            print('What are the names of the people at work today? (Enter one name at a time)')

            while not person == 'Done':
                person = input().lower().capitalize()
                if not person == 'Done':
                    people.append(person)
        total = float(input('What is the total that needs to be divided? '))
        divide(people, total, dict)

    elif decision == "people at work":
        print('Name all the people at work today (one at a time): ')
        while True:
            name = input().lower().capitalize()
            if name == 'Done':
                break
            people_at_work.append(name)

    elif decision == 'person':
        name = input('Name of the person in question: ')
        print(f'There should be {dict[name]}kr for {name.capitalize()}')

    elif decision == 'setup':
        if test:
            for i in range(5):
                name = "test " + str(i)
                dict[name] = 0
            pickle_save(tips, dict)
        else:
            dict = setup()
            print('The program has been setup')

    elif decision == 'status':
        if len(dict) == 0:
            print('No data available')
            continue
        for (person, money) in zip(dict.keys(), dict.values()):
            print(str(person).capitalize() + ':', str(money) +  'kr')

    elif decision == 'setup the period':
        setup_period()

    elif decision == 'status for the period':
        if len(dict) == 0:
            print('No data available')
            continue
        data = pickle_out('tips for period.pkl')
        print(data)
        for (person, money) in zip(data.keys(), data.values()):
            print(str(person).capitalize() + ':', str(money) + 'kr')

    elif decision == 'clear the period':
        sure = input('Are you sure you want to clear? ')
        if sure == 'yes' or 'y':
            setup_period()
            print('The tracker for the period has been stopped')
        else:
            print('The clear has been stopped')

    elif decision == 'add':
        name = input("Name of the person you'd like to add").lower()
        dict[name] = 0

    elif decision == 'update period':
        period_tracker()

    elif decision == 'options':
        print('You can type:\n' +
              'Status\n' +
              'Clear\n' +
              'Declare\n' +
              'Person\n' +
              'People at work\n' +
              'Done\n' +
              'Update period\n' +
              'Clear the period')


