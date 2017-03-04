#xml parser to read the stuff:
#!/usr/bin/python
from xml.dom import minidom

def read(file):

    xmldoc = minidom.parse(file)
    itemlist = xmldoc.getElementsByTagName('metric')
    print(len(itemlist))
    for s in itemlist:
        print(s.attributes['name'].value)