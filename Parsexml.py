import pandas as pd
from lxml import etree

# Importing risk factor XML Files and loading them into pandas df
# path in xml is /records/record/


def append_to_dataframe(parsed_info, dataframe, df_column):
    """ Appends a pandas series row wise - adds a new column with title 'df_column' to an existing dataframe."""
    dataframe[df_column] = pd.concat([dataframe, parsed_info], axis=1)
    pass


class ParseArticle:
    """ This class parses various elements of an xml file containing scientific articles and papers. Elements include
    the author, title, year, abstract, and keywords."""

    def __init__(self, root, dataframe):
        self.root = root
        self.dataframe = dataframe

    def parse_title(self, parent, child, df_column):

        parent_search = './/' + str(parent)
        variable_list = []

        for count, childs in enumerate(self.root.iterfind(parent_search)):
            for subchild in childs.iterfind(child):

                print(subchild.text)
                variable_list.append(subchild.text)
        print(variable_list)

        self.dataframe[df_column] = variable_list

        return self.dataframe


f = 'ExampleXML_files/endnote.xml'
tree = etree.parse(f)
root2 = tree.getroot()

article_info = pd.DataFrame(columns=['title', 'year', 'author', 'volume', 'abstract', 'rf_label'])

xml_file = ParseArticle(root=root2, dataframe=article_info)
x = xml_file.parse_title(parent='titles', child='title', df_column='title')
print(x)
