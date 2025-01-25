import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, inspect, Table, Column, String, MetaData, Index, text

from shining_brain.logger_setup import setup_logger

log = setup_logger('ETL')


def test_extract():
    directory_path = Path(os.path.expanduser('~')) / ".shining-brain" / "ds"
    data_1 = {}
    try:
        for file_path in directory_path.iterdir():
            (basename, extension) = os.path.splitext(file_path.name)
            table_name = basename.split("__")[0]
            safety_path = str(file_path)
            if table_name not in data_1:
                data_1[table_name] = [safety_path]
            else:
                data_1[table_name].append(safety_path)
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' was not found.")
    # print("\n")
    # print(json.dumps(data_1, sort_keys=True, indent=2))
    data_2 = []
    for table_name in data_1:
        dfs = []
        for file in data_1[table_name]:
            df = pd.read_excel(file, header=0)
            dfs.append(df)
        combined_df = pd.concat(dfs, ignore_index=True)
        # combined_df.to_excel(directory_path / f"{table_name}.xlsx")
        data_2.append((table_name, combined_df))
    for d in data_2:
        load_data_into_mysql("ds", d[0], d[1])


def test_load_data_into_mysql():
    df = pd.read_excel(r"C:\Users\Store\.shining-brain\ds\work_order_bill_browse__100.xlsx")
    load_data_into_mysql("ds", "work_order", df)


def load_data_into_mysql(schema, table_name, df):
    schema_name = schema
    index_columns = ["work_order"]
    table_name = table_name  # Extract table name from file name
    engine = create_engine(create_schema(schema_name))

    # Convert column names to snake_case
    df.columns = df.columns.str.lower().str.replace(r"[^a-z0-9]", "_", regex=True)
    # Create a metadata object
    metadata = MetaData(schema=schema_name)
    # Create the table dynamically
    max_lengths = df.astype(str).apply(lambda x: x.str.len()).max()
    table = Table(
        table_name,
        metadata,
        *[Column(col_name, String(length=200)) for col_name in df.columns],
    )
    # Create indices
    for col_name in index_columns:
        Index(f'idx_{table_name}_{col_name}', table.c[col_name])
    inspector = inspect(engine)
    table_exists = inspector.has_table(table_name, schema=schema_name)
    with engine.connect() as conn:
        if not table_exists:
            table.create(conn)
            df.to_sql(table_name, conn, if_exists='append', index=False)
            conn.commit()
        else:
            df.to_sql(table_name, conn, if_exists='append', index=False)


def test_create_schema():
    print("\n")
    print(create_schema("test_schema_4"))
    print(create_schema("test_schema_5"))


def create_schema(schema):
    log.debug("Create Schema: %s.", schema)
    url_without_schema = "mysql+pymysql://root:root@127.0.0.1:3306"
    log.debug("URL without schema: %s.", url_without_schema)
    engine = create_engine(url_without_schema)
    inspector = inspect(engine)
    exists = inspector.has_schema(schema)
    connect = engine.connect()
    if not exists:
        with connect as conn:
            conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema}"))
        log.debug("The creation of schema %s was successful.", schema)
    else:
        log.debug("Schema %s exists.", schema)

    url_with_schema = f"{url_without_schema}/{schema}"
    log.debug("URL with schema: %s.", url_with_schema)
    return url_with_schema
