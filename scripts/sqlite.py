# ---
# jupyter:
#   jupytext:
#     formats: notebooks//ipynb,rmd//Rmd,scripts//py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Database Inspection and Migration

# ! cp ../backend/main.db ../data/sensitive/main.db

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import os.path

db = create_engine('sqlite:///../data/sensitive/main.db')

query = """
SELECT * FROM churches
"""

pd.read_sql(query, db)

qry2 = """
SELECT * FROM sqlite_master
"""

pd.read_sql(qry2, db)

qr3 = """
SELECT * FROM users
"""

pd.read_sql(qr3, db)

qry4 = """
PRAGMA table_info(churches)
"""

pd.read_sql(qry4, db)

# +
# # ! cp ../data/sensitive/main.db ../backend/main.db
