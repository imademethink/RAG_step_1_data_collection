import re
import psycopg2
from psycopg2.extras import RealDictCursor


# database processing

# 1.    Schema-Aware Metadata Extraction is the process of retrieving structural and descriptive information
#       about a database—such as table names, column data types, primary/foreign keys, and
#       natural language descriptions—to provide semantic context to a Large Language Model (LLM)

db_params = {"dbname": "shop_db", "user": "admin", "password": "password123", "host": "localhost"}

def raise_query(conn_params, sql_query):
    """
    Raise query on given DB
    """
    results = []

    try:
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                # Query to get tables, columns, types, and descriptions
                query = sql_query
                cur.execute(query)
                results = cur.fetchall()
    except Exception as e:
        return f"Error during database interaction: {e}"
    return  results

def extract_schema_context(conn_params):
    """
    Extracts table names, column types, and descriptions from PostgreSQL.
    """
    context = []

    try:
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                # Query to get tables, columns, types, and descriptions
                query = """
                SELECT 
                    t.table_name,
                    c.column_name,
                    c.data_type,
                    pg_catalog.col_description(format('%I.%I', t.table_schema, t.table_name)::regclass::oid, c.ordinal_position) as column_description
                FROM 
                    information_schema.tables t
                JOIN 
                    information_schema.columns c ON t.table_name = c.table_name
                WHERE 
                    t.table_schema = 'public' 
                    AND t.table_type = 'BASE TABLE';
                """
                results = raise_query(conn_params, query)

                # Group by table for cleaner LLM prompting
                schema_map = {}
                for row in results:
                    table = row['table_name']
                    if table not in schema_map:
                        schema_map[table] = []
                    schema_map[table].append(
                        f"- {row['column_name']} ({row['data_type']}): {row['column_description'] or 'No description'}"
                    )

                for table, cols in schema_map.items():
                    context.append(f"Table: {table}\n" + "\n".join(cols))

    except Exception as e:
        return f"Error extracting metadata: {e}"

    return "\n\n".join(context)

def clean_product_data(product_row):
    """
    Cleans a database row for AI embedding.
    Input: {'name': 'Trash-Item-a1b2', 'description': 'Description: f9...'}
    """
    name = product_row['name']
    description = product_row['description']

    # 1. Remove specific boilerplate prefixes (De-noising)
    name = re.sub(r'^Trash-Item-', '', name)
    description = re.sub(r'^Description: ', '', description)

    # 2. Remove Hexadecimal strings (Internal/Garbage noise)
    # This removes random md5 hashes like 'a1b2c3d4e5'
    description = re.sub(r'[a-f0-9]{12,}', '[ID]', description)

    # 3. Format as a clean string for the LLM
    clean_string = f"Product: {name}. Description: {description}."

    return clean_string.strip()

# extract DB schema
print(extract_schema_context(conn_params=db_params))
print("=================================================")
print("=================================================")
raw_data = {'name': 'Trash-Item-x88z', 'description': 'Description: 5f4dcc3b5aa765d'}
print(clean_product_data(raw_data))
# output: "Product: x88z. Description: [ID]."
print("=================================================")
print("=================================================")
# raise simple query
my_query =  "select * from products where price > 78 and price < 100;"
all_results = raise_query(conn_params=db_params, sql_query=my_query)
for one_result in all_results:
    print(one_result)

