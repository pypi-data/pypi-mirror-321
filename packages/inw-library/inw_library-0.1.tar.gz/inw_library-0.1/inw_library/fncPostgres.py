import pandas as pd
import psycopg2
import io
import csv

# import fncString as fnStr
def generate_create_table_script(df, table_name, use_index=False):
    '''
    เช็กว่าตารางมีอยู่ในฐานข้อมูลหรือไม่

    Parameters:
    df (dataframe): dataframe ที่ต้องการ
    table_name (str): table name
    use_index (bool): use index

    Returns:
    str: script create table
    '''
    # 
    # check_exists_query = f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}');"
    
    # สร้างคำสั่ง SQL สำหรับการสร้างตาราง
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ( "
    
    # กำหนดชนิดข้อมูล
    data_types = {
        'int64': 'INTEGER',
        'float64': 'REAL',
        'object': 'VARCHAR(255)',#'TEXT',
        'bool': 'BOOLEAN',
        'datetime64[ns]': 'TIMESTAMP',
        'datetime64[ns, Asia/Bangkok]': 'TIMESTAMP',
        'str' : 'VARCHAR(255)'
    }
    
    # สร้างคอลัมน์สำหรับคำสั่ง SQL
    columns = []
    
    # ถ้าใช้ index มาสร้างคอลัมน์
    if use_index and df.index.name is not None:
        index_col_name = df.index.name
        columns.append(f"    \"{index_col_name}\" SERIAL PRIMARY KEY")  # ใช้ SERIAL สำหรับ Primary Key

    for i, column in enumerate(df.columns):
        if column:  # ถ้ามีชื่อคอลัมน์
            col_name = column
        else:  # ถ้าไม่มีชื่อคอลัมน์
            col_name = f'col{i+1:03}'  # col001, col002, ...
        
        dtype = str(df[column].dtype)
        sql_type = data_types.get(dtype, 'TEXT')  # ใช้ TEXT ถ้าไม่พบชนิดข้อมูล

        col_name = col_name.replace(" ", "")

        columns.append(f"    {col_name} {sql_type}")
    
    create_table_query += ", ".join(columns) + " );"
    
    return  create_table_query #check_exists_query,


def dataframe_to_csv_stringio(df, use_index=False):
    """Convert DataFrame to a CSV format in memory."""
    buffer = io.StringIO()
    df.to_csv(buffer, header=False, index=use_index, sep='\t', na_rep='NULL', quoting=csv.QUOTE_NONE)#csv.QUOTE_NONNUMERIC
    buffer.seek(0)
    return buffer

def copy_from_stringio(buffer, table_name, connection):
    """Copy data from StringIO buffer to PostgreSQL table."""
    with connection.cursor() as cur:
        cur.copy_from(buffer, table_name, sep="\t", null='NULL')
    connection.commit()

def bulk_copy_dataframe_to_postgres(df, table_name, db_args, use_index=False):
    """Bulk copy DataFrame to PostgreSQL table."""
    
    # Connect to the database
    conn = psycopg2.connect(**db_args)

    try:
        # Convert DataFrame to CSV format in memory
        buffer = dataframe_to_csv_stringio(df, use_index=use_index)
        print(buffer)
        # Perform the copy operation
        copy_from_stringio(buffer, table_name, conn)
        print(f"Data copied successfully to {table_name}.")
        
    except Exception as e:
        print(f"Error occurred: {e}")
    
    finally:
        conn.close()
