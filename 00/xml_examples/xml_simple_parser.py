import xml.etree.ElementTree as ET

# Sample XML string
xml_data = """
<note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body at1="1" at2="2">Don't forget me this weekend!<subbody>This is a child of body</subbody></body>
</note>
"""

# NOTE: We can use parse method to load data from a file but for
# simplicity we use the above string - see the """ way of declaring string
# which makes life easier in case you want to put entire file contents inside
# your python script


# Parse the XML string
root = ET.fromstring(xml_data)

# Access elements
print(root.tag)  # Output: 'note'
for child in root:
    print(child.tag, child.text)  # Print tag and text content
    if child.tag == 'body':
        print(child.attrib) # we can access this way the attributes as a dictionary
        print(child.attrib['at1'])
        for bc in child: # we can go deeper for children of body, if required
            print("subchild of body:"+bc.tag)
