from lxml import etree

f = 'ExampleXML_files/endnote.xml'
tree = etree.parse(f)
root = tree.getroot()
print(root.tag)

title_list = []
for child in root.iterfind('.//titles'):
    for subchild in child.iterfind('title'):
        print(subchild.text)
        title_list.append(subchild.text)
print(title_list)

# variable_list = []
# for child in root.iterfind('.//abstract'):
#     """ Abstract is a child of record. Since abstract has no other parent aside from roots first child, it will
#     print the text directly."""
#
#     variable_list.append(child.text)
#
# print(variable_list)
