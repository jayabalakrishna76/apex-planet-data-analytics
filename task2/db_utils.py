import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:Sai%40506637@localhost/intership_sql"
    )
def run_query(query):
    df = pd.read_sql(query,engine)
    return df