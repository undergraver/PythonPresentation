my_string = "apples,organges,figs,mushrooms"
fruits = my_string.split(',') # we split after "," separator

# it iterates through a list
for f in fruits:
    print(f)

# we can also iterate based on a counter

counter = 0
# while the condition is true this repeats
while counter < 10:
    print(counter)
    # failure to increment the value results in an infinite loop; try it
    counter = counter + 1

# isn't it cool you can multiply strings?
print('+'*80)

for n in range(10):
    print(n)
