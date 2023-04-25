from lxml import etree
import pandas as pd

f = 'IncomingData/04.22.23_endnote.xml'
tree = etree.parse(f)
root = tree.getroot()
print(root.tag)

title_list = []
for child in root.iterfind('.//titles'):
    for subchild in child.iterfind('title'):
        title_list.append(subchild.text)



variable_list = []
for child in root.iterfind('.//abstract'):
    """ Abstract is a child of record. Since abstract has no other parent aside from roots first child, it will
    print the text directly."""
    if child.text is None:
        variable_list.append('')
    else:
        variable_list.append(child.text)

# print [element.text if element.text is not None else ''for element in tree.xpath('//td[@headers="h1"]')]
print(f'Title list length is {len(title_list)}')
print(f'Abstract list length is {len(variable_list)}')

df = pd.DataFrame(columns=['title', 'abstract'])
df.title = title_list
df.abstract = variable_list

df.to_csv('testing_null.csv')

# assert len(title_list) == len(variable_list), "Somethings missing."
