import json
import os
import glob

def load_json_info(filename):
    print("*"*40)
    print("Analyzing:"+filename)
    f = open(filename,'r')
    buf = f.read()
    f.close()

    data = json.loads(buf)

    print("Name:"+data['first_name'])
    print('Age:'+str(data['age']))
    print('Height:'+str(data['height']))

    print(data['phone_numbers'][0]['number'])

    phoneNumbers = data['phone_numbers']
    print("Phone numbers:")
    for phone_number in phoneNumbers:
        print("{0} number is {1}".format(phone_number['type'],phone_number['number']))



files = os.listdir('json_dir')
print("No filter - with listdir")
print(files)
print("Filtering listdir output")
# dumb filter
for name in files:
    if name.find('.json') >= 0:
        print(name)

print("Smarter filter with glob")
# smarter filter
files = glob.glob("json_dir/*.json")
for file in files:
    load_json_info(file)


