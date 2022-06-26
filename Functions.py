import pickle

def pickle_save(filename, dict):
    with open(filename, 'wb') as file:
        pickle.dump(dict, file)

def pickle_out(filename):
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    return data

def divide(people, total, dict):
    #Number of people
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
