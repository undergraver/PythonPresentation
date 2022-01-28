#!/usr/bin/env python3

import random
import time

max_num1=10
max_num2=10

def get_value_from_user(msg1,def_value):
    msg = msg1 + "(default:" + str(def_value) + ")"
    max_num=def_value
    try:
        val = input(msg)
        max_num=int(val)
    except:
        pass
    return max_num

max_num1 = get_value_from_user("Enter maximum value for first term or enter for default one",10)
max_num2 = get_value_from_user("Enter maximum value for second term or enter for default one",10)


start_time=time.perf_counter()

valid=0
counter=0
while True:
    f1 = random.randint(1,max_num1)
    f2 = random.randint(1,max_num2)
    prefix = '%05d' % (counter+1)
    mult_str=str(f1)+" x "+str(f2)+" ="
    msg = prefix + ": " + mult_str
    try:
        val = int(input(msg))
        expected = f1*f2
        if val == expected:
            valid+=1
        else:
            print("Bad answer. Correct one is:" + mult_str + str(expected))
        
        counter+=1
    except:
        break


end_time=time.perf_counter()
total_time=end_time - start_time
speed = float(counter)/total_time
accuracy = float(valid)/float(counter) * 100;
print("Speed is: %.2f per second" % (speed))
print("Accuracy is: %.2f%% (%d/%d)" % (accuracy,valid,counter))
