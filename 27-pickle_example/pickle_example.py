'''
pickle example - you might use pickle to transfer data between servers, 
note - pickle has no security backing it
'''
import pickle

#### Example output - comment out for read ###
example_dict = { 1: "6", 2: "22", 3: "f"}

with open ('dict.pickle', 'wb') as pickle_out:  # write bytes
    pickle.dump(example_dict, pickle_out)

# pickle_out = open("dict.pickle", "wb")  # with extended form
# pickle_out.close()

#### Example input - comment out for read ###
# To read back to memory
with open("dict.pickle", "rb") as pickle_in:  # read bytes
    example_dictionary = pickle.load(pickle_in)
    
# pickle_in = open("dict.pickle", "rb")  # with extended form
# example_dictionary = pickle.load(pickle_in)

print(example_dictionary)
print(example_dictionary[2])
