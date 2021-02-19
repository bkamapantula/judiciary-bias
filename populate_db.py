import pandas as pd
from sqlalchemy import create_engine
import tqdm

engine_str = 'postgresql://{user}:{password}@{s}/{db}'.format(
    user='ENTER USERNAME',
    password='ENTER PASSWORD',
    s='SERVER',
    db='DATABASE NAME'
)
engine = create_engine(engine_str)


def keys_files():
    """
    expects keys/files structure.
    
    appends rows to existing tables.
    """
    files = {
        'keys': [
            {'file': 'act_key.csv', 'table': 'act_key'},
            {'file': 'cases_court_key.csv', 'table': 'cases_court_key'},
            {'file': 'disp_name_key.csv', 'table': 'disp_name_key'},
            {'file': 'judge_case_merge_key.csv', 'table': 'judge_case_merge_key'}
            {'file': 'purpose_name_key.csv', 'table': 'purpose_name_key'},
            {'file': 'section_key.csv', 'table': 'section_key'},
            {'file': 'type_name_key.csv', 'table': 'type_name_key'}
        ]
    }
    for file_mapping in files['keys']:
        df = pd.read_csv("keys/" + file_mapping['file'])
        print(file_mapping['file'], file_mapping['table'], df.shape)
        df.to_sql(file_mapping['table'], engine, if_exists='append', index=False)


def judges_file():
    """judges table."""
    judges = pd.read_csv('judges_clean.csv')
    judges.to_sql('judges', engine, if_exists='append', index=False)


def acts_sections_file():
    """acts and sections table."""
    for df in tqdm.tqdm(pd.read_csv('acts_sections.csv', chunksize=1000000), total=77):
        df.to_sql('acts_sections', engine, if_exists='append', index=False)


def cases_files():
    """cases by year."""
    # pass
    files = [
        'cases-unzipped/cases_2010.csv',
        'cases-unzipped/cases_2011.csv',
        'cases-unzipped/cases_2012.csv',
        'cases-unzipped/cases_2013.csv',
        'cases-unzipped/cases_2014.csv',
        'cases-unzipped/cases_2015.csv',
        'cases-unzipped/cases_2016.csv',
        'cases-unzipped/cases_2017.csv',
        'cases-unzipped/cases_2018.csv'
    ]
    for f in tqdm.tqdm(files):
        for df in pd.read_csv(f, chunksize=10000):
            df.to_sql('cases', engine, if_exists='append', index=False)


if __name__ == '__main__':
    keys_files()
    judges_file()
    acts_sections_file()
    cases_files()

