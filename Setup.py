from Functions import *
filename = 'tips.pkl'

#Testing the code
test = True


if test == True:
    dict = {}
    for i in range(5):
        name = "test " + str(i)
        dict[name] = 0
    pickle_save(filename, dict)
# Real names

print(pickle_out('tips.pkl'))
divide(['test 1', 'test 3'], 100, dict)
print(pickle_out(filename))