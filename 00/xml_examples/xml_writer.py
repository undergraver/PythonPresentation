import xml.etree.ElementTree as ET
import sys
import datetime

tree = ET.parse('prices_wrong.xml')
root = tree.getroot()
root_tag_name = "prices"
if root.tag != root_tag_name:
    print("Expected {0} as root tree but got {1}".format(root_tag_name,root.tag))
    sys.exit(1)

to_remove = []
for product in root:
    if product.tag != "product":
        print("Ignoring unexpected tag:%s" % (product.tag))
        continue
    #name = product.attrib['name']
    name = product.get('name') # same as above
    price = 0
    expiration = None
    
    pricetag = product.find('price')
    price = int(pricetag.text)
    expirationTag = product.find('expiration')
    yyyymmdd = expirationTag.text
    y,m,d = yyyymmdd.split('-')
    expiration = datetime.date(int(y),int(m),int(d))

    # check the date, if expired via timedelta
    delta = datetime.timedelta(days=10)
    today = datetime.date.today()
    if expiration <= today:
        print("Product %s should be removed as it expired on %s" % (name,str(expiration)))
        to_remove.append(product)
        # we can remove it from here also
    elif today + delta >= expiration:
        discount_percent = 60
        print("Product {0} will expire on {1}. Applying {2}% discount".format(name,str(expiration),discount_percent))
        old_price = price
        new_price = price * (100-discount_percent)//100;
        print("Old price %d; new price %d." % (old_price,new_price))
        # changing the node in the loaded xml tree
        pricetag.text = str(new_price)

for elem in to_remove:
    root.remove(elem)

# now we write the modified XML
tree.write("prices_updated.xml")
