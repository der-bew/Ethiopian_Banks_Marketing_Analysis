from sqlalchemy import create_engine
import pandas as pd

def get_connection(db_url):
    """
    Create and return a SQLAlchemy engine connected to the database.

    Params:
    db_url (str): The database URL.

    Returns:
    sqlalchemy.engine.Engine: A SQLAlchemy engine connected to the database.
    """
    engine = create_engine(db_url)
    return engine

def write_df_to_db(df, table_name, db_url, if_exists='replace', index=False, chunksize=None):
    """
    Write a DataFrame to a SQL database table.

    Params:
    df (pd.DataFrame): The DataFrame to write to the database.
    table_name (str): The name of the table to write to.
    db_url (str): The database URL.
    if_exists (str, optional): What to do if the table already exists. Default is 'replace'.
    index (bool, optional): Whether to write DataFrame index as a column. Default is False.
    chunksize (int, optional): Number of rows to write at a time. Default is None.
    """
    # Get the database connection
    engine = get_connection(db_url)
    
    # Write the DataFrame to the specified table
    df.to_sql(
        table_name,
        engine,
        if_exists=if_exists,
        index=index,
        chunksize=chunksize,
    )
    print(f"DataFrame written to table '{table_name}' in the database '{db_url}'.")
