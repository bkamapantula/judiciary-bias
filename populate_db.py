import pandas as pd
from sqlalchemy import create_engine

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


if __name__ == '__main__':
    keys_files()
