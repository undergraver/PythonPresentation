#!/usr/bin/env python3

import random
import time

max_num=10

msg = "Enter maximum multiplication factor or enter for default one (default: 10):"
try:
    val = input(msg)
    max_num=int(val)
except:
    pass

print("Maximum value is 10")

start_time=time.perf_counter()

valid=0
counter=0
while True:
    f1 = random.randint(1,max_num)
    f2 = random.randint(1,max_num)
    prefix = '%05d' % (counter+1)
    msg = prefix + ": " + str(f1)+" x "+str(f2)+" ="
    try:
        val = int(input(msg))
        if val == f1*f2:
            valid+=1
        counter+=1
    except:
        break


end_time=time.perf_counter()
total_time=end_time - start_time
speed = float(counter)/total_time
accuracy = float(valid)/float(counter) * 100;
print("Speed is: %.2f per second" % (speed))
print("Accuracy is: %.2f%% (%d/%d)" % (accuracy,valid,counter))
