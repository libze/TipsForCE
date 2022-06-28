import pickle


def pickle_save(filename, dict):
    with open(filename, 'wb') as file:
        pickle.dump(dict, file)


def pickle_out(filename):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
    except:
        pickle_save('tips.pkl', {})
        pickle_out('tips.pkl')
    return data


def divide(people, total, dict):
    # Number of people
    N = len(people)
    per_person = total/N
    for person in people:
        dict[person] = dict[person] + per_person
        pickle_save('tips.pkl', dict)
    print('The money has now been divided')


def setup():
    with open("names.txt", "r") as files:
        dict = {}
        for readline in files:
            name = readline.strip()
            dict[name] = 0
    pickle_save('tips.pkl', dict)

    return dict


def setup_period():
    with open("names.txt", "r") as files:
        dict = {}
        for readline in files:
            name = readline.strip()
            dict[name] = 0
    pickle_save('tips for period.pkl', dict)

    return dict


def period_tracker():
    monthly = pickle_out('tips for period.pkl')
    weekly = pickle_out('tips.pkl')

    for name in weekly.keys():
        monthly[name] += weekly[name]

    monthly['total'] = sum(monthly.values())
    monthly['available'] = 0

    pickle_save('tips for period.pkl', monthly)
    print('The tracker for the period has been updated')
