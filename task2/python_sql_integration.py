import pandas as pd
from sqlalchemy import create_engine

# MySQL connection
engine = create_engine(
    "mysql+pymysql://root:Sai%40506637@localhost/intership_sql"
)
query = """
SELECT Category,
       COUNT(*) AS Orders
FROM processed_data
GROUP BY Category
ORDER BY Orders DESC;
"""

df = pd.read_sql(query, engine)
print(df)