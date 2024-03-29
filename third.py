'''
Parse the below given xml data, store it as a suitable data structure(list, set,
tuple, dictionary and class).
'''
# import packages
import pprint
from xml.etree import cElementTree as ElementTree


# XML parnets having same child name or same tags 

class XmlListConfig(list):
    def __init__(self, aList):
        for element in aList:
            if element:
                if len(element) == 1 or element[0].tag != element[1].tag:
                    self.append(XmlDictConfig(element))

                elif element[0].tag == element[1].tag:
                    self.append(XmlListConfig(element))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)

# Converting to Dictionary

class  XmlDictConfig(dict):

    def __init__(self, parent_element):
        if parent_element.items():
            self.update(dict(parent_element.items()))

        for element in parent_element:
            if element:
                if len(element) == 1 or element[0].tag != element[1].tag:
                    aDict = XmlDictConfig(element)
                else:
                    aDict = {element[0].tag: XmlListConfig(element)}

                if element.items():
                    aDict.update(dict(element.items()))
                self.update({element.tag: aDict})
            elif element.items():
                self.update({element.tag: dict(element.items())})

            else:
                self.update({element.tag: element.text})



# Main code

tree = ElementTree.parse('movie.xml')
root = tree.getroot()
xmldict = XmlDictConfig(root)

# For displaying data
pprint.pprint(xmldict, sort_dicts = False)




