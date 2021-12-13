import pandas as pd
import sqlite3
from datetime import datetime

def export_as_spreadsheet(tablename = 'cap_matrix', db = 'cap_blog.db'):
    """
    Exports a table as a spreadsheet.
    """
    # Connect to the database
    conn = sqlite3.connect(db)
    # Get the data
    tabledata = pd.read_sql_query("SELECT * FROM " + tablename, conn)
    # Export to a spreadsheet
    tabledata.to_excel(f'output/{tablename}-{datetime.now()}.xlsx', index = False)
    # Close the connection
    conn.close()