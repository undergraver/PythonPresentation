import random

lab = random.randint(3,10) # an integer between 3 and 10, including 3 and 10
exam = random.randint(3,10)

# NOTE: Comments with multiple # are here to show how indentation works

if lab >= 5:
    if exam >= 5:
        print("You passed.")
        
####
    #### - under this if

    else:
        print("You qualified for the exam but failed.")

####
    #### - under this else


#### - under the first if
    s = "Lab grade was {0} and exam grade was {1}.".format(lab, exam)
    print(s)

else:
    print("You failed to qualify for the exam.")
    # see https://docs.python.org/3/library/string.html#formatstrings
    # for more information about formatting strings (quite a lot of reading)
    dynamicString = "Your lab grade was {0} which is below 5.".format(lab)
    print(dynamicString)
