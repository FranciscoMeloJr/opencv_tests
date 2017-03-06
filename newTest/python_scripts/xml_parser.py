#xml parser to read the stuff:
#!/usr/bin/python
from xml.dom import minidom

def read_metrics(file):

    xmldoc = minidom.parse(file)
    itemlist = xmldoc.getElementsByTagName('metric')
    print(len(itemlist))
    values = []
    for s in itemlist:
        values.append(s.attributes['name'].value)

    return values

def read_max(file):

    xmldoc = minidom.parse(file)
    itemlist = xmldoc.getElementsByTagName('max')
    print(len(itemlist))
    values = []
    for s in itemlist:
        values.append(s.attributes['name'].value)

    return values

def read_times(file):

    xmldoc = minidom.parse(file)
    itemlist = xmldoc.getElementsByTagName('times')
    print(len(itemlist))
    values = []
    for s in itemlist:
        values.append(s.attributes['name'].value)

    return values

def read_file(file):

    xmldoc = minidom.parse(file)
    itemlist = xmldoc.getElementsByTagName('file')
    print(len(itemlist))
    values = []
    for s in itemlist:
        values.append(s.attributes['name'].value)

    return values

def read_ext(file):

    xmldoc = minidom.parse(file)
    itemlist = xmldoc.getElementsByTagName('path')
    print(len(itemlist))
    values = []
    for s in itemlist:
        values.append(s.attributes['name'].value)

    return values


def read_type(file):

    xmldoc = minidom.parse(file)
    itemlist = xmldoc.getElementsByTagName('type')
    print(len(itemlist))
    values = []
    for s in itemlist:
        values.append(s.attributes['name'].value)

    return values

def read_program(file):

    xmldoc = minidom.parse(file)
    itemlist = xmldoc.getElementsByTagName('program')
    print(len(itemlist))
    values = []
    for s in itemlist:
        values.append(s.attributes['name'].value)

    return values