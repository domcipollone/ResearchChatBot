from lxml import etree
import pandas as pd
from datetime import date


def xml_to_dataframe(xml_file):
    
    # Parse the XML file
    tree = etree.parse(xml_file)

    # Get the root element
    root = tree.getroot()

    df = pd.DataFrame(columns=['title', 'author', 'year', 'abstract', 'keywords', 'issue', 'volume', 'journal', 'date_added'])

    # Iterate through the records
    for count, record in enumerate(root.iter('record')):
        # Get the values of the elements
        
        title = record.find('titles/title')
        authors = record.find('contributors/authors/author')
        year = record.find('dates/year')
        abstract = record.find('abstract')
        keywords = record.findall('keywords/keyword')
        issue = record.find('issue')
        volume = record.find('volume')
        journal = record.find('periodical/full-title')

        if title is None:
            title_text = ''
        else:
            title_text = title.text

        if authors is None:
            authors_text = ''
        else:
            authors_text = authors.text

        if year is None:
            years_text = ''
        else:
            years_text = year.text

        if abstract is None:
            abstract_text = ''
        else:
            abstract_text = abstract.text

        if keywords is None:
            keyword_text = []
        else:
            keyword_text = []
            for subelements in keywords:
                keyword_text.append(subelements.text) 

        if issue is None:
            issue_text = ''
        else: 
            issue_text = issue.text

        if volume is None:
            volume_text = ''
        else: 
            volume_text = volume.text

        if journal is None:
            journal_text = ''
        else: 
            journal_text = journal.text 

        df.loc[count, 'title'] = title_text
        df.loc[count, 'year'] = years_text
        df.loc[count, 'author'] = authors_text.strip()
        df.loc[count, 'abstract'] = abstract_text
        df.loc[count, 'keywords'] = keyword_text
        df.loc[count, 'issue'] = issue_text
        df.loc[count, 'volume'] = volume_text
        df.loc[count, 'journal'] = journal_text
        df.loc[count, 'date_added'] = date.today().isoformat()

    df.sort_values(by='author', ascending=True, inplace=True)
    df.reset_index(inplace=True, drop=True)

    return df


f = 'IncomingData/04.22.23_endnote.xml'

testing = xml_to_dataframe(xml_file=f)
testing.to_csv("testing.csv")
testing.to_pickle(path='diw.pkl')
print(testing.head())
