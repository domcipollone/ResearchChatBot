import pandas as pd
from lxml import etree
import os


# Importing risk factor XML Files and loading them into pandas df
# path in xml is /records/record/


class ParseArticle:
    """ This class parses various elements of an xml file containing scientific articles and papers. Elements include
    the author, title, year, abstract, and keywords."""

    def __init__(self, parent, child, root, dataframe, df_column):
        self.parent = parent
        self.child = child
        self.root = root
        self.dataframe = dataframe
        self.df_column = df_column

    def parse_title(self):
        parent_search = './/' + str(self.parent)
        for index, child in enumerate(self.root.iterfind(parent_search)):
            variable_list = [child.text]

            self.dataframe[index, self.df_column] = variable_list

        self.dataframe[self.df_column] = self.dataframe[self.df_column].str[0]

        return self.dataframe


def parse_xml(parent_element, child_element, root, df_column, df):
    parent_search = './/' + str(parent_element)

    if child_element == '':
        for index, child in enumerate(root.iterfind(parent_search)):
            variable_list = [child.text]

            df.at[index, df_column] = variable_list

    else:
        for index, child in enumerate(root.iterfind(parent_search)):
            variable_list = []
            for subchild in child.iterfind(child_element):
                variable_list.append(subchild.text)

            df.at[index, df_column] = variable_list


article_info = pd.DataFrame(columns=['title', 'year', 'author', 'volume', 'abstract'])
# labels = ['asr', 'chloride', 'nitrate', 'sulfate']
path = 'IncomingData'

for count, filename in enumerate(os.listdir(path)):
    f = os.path.join(path, filename)
    print('Working on ', f)
    if os.path.isfile(f):

        tree = etree.parse(f)
        root_doc = tree.getroot()

        article_info = pd.DataFrame(columns=['title', 'year', 'author', 'volume', 'abstract'])

        parents = ['titles', 'dates', 'authors', 'volume', 'abstract']
        children = ['title', 'year', 'author', '', '']

        for i, value in enumerate(parents):
            assert len(parents) == len(children), 'Lengths of parent and children list must be identical.'

            parse_xml(parent_element=parents[i], child_element=children[i], df_column=article_info.columns[i],
                      root=root_doc, df=article_info)

        for i, column in enumerate(article_info.columns):
            article_info[column] = article_info[column].str[0]

    # article_info['rf_label'] = labels[count]
    # article_info_complete = pd.concat([article_info_complete, article_info])

article_info.reset_index(drop=True, inplace=True)
article_info.to_csv('ArticleData_og.csv')

tree2 = etree.parse('IncomingData/04.22.23_endnote.xml')
root2 = tree2.getroot()
article_info2 = pd.DataFrame(columns=['title', 'year', 'author', 'volume', 'abstract', 'rf_label'])

x = ParseArticle(parent='titles', child='title', root=root2, dataframe=article_info2, df_column='title').parse_title()
x.to_csv('class_test.csv')
