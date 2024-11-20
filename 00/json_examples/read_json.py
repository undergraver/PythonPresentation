import json

# this reads json from file directly
#with open('example.json', 'r') as file:
#    data = json.load(file)

# this will read the file contents and use loads
# to load the json contents

f = open('example.json','r')
buf = f.read()
f.close()

data = json.loads(buf)

print("Name:"+data['first_name'])
print('Age:'+str(data['age']))
print('Height:'+str(data['height']))
print('Children:'+str(data['children']))

print(data['phone_numbers'][0]['number'])

phoneNumbers = data['phone_numbers']
print("Phone numbers:")
for phone_number in phoneNumbers:
    print("{0} number is {1}".format(phone_number['type'],phone_number['number']))


# Print the data
#print(data)
