f = open("vote_count.txt","rt")
buf = f.read() # this reads the entire file and put it into bug
f.close() # we close the file as we no longer need it

split_integers_as_strings = buf.split()
# after this operation we have a list of integers each as string

#print(split_integers_as_strings)

sum = 0
for int_str in split_integers_as_strings:
    int_value = int(int_str) # convert from string to int
    sum = sum + int_value

print(sum)