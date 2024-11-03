import sys

def count_votes(file_name):
    f = open(file_name,"rt")
    buf = f.read() # this reads the entire file and put it into buf
    f.close() # we close the file as we no longer need it

    split_integers_as_strings = buf.split()
    # after this operation we have a list of integers each as string

    #print(split_integers_as_strings)

    total = 0
    for int_str in split_integers_as_strings:
        int_value = int(int_str) # convert from string to int
        total = total + int_value

    return total

total_votes = 0
file_list = sys.argv[1:] # eliminate the first element
for fname in file_list:
    total_votes += count_votes(fname)

print("Total votes in:"+str(file_list)+":"+str(total_votes))
