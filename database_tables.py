import psycopg2

environments = 'local'

# creating the database connection
if environments == 'docker':
    DATABASE_URL = 'postgresql://postgres:postgres@db:5432/postgres'
    conn = psycopg2.connect(DATABASE_URL)
else:
    conn = psycopg2.connect(database="logistics",
                            user='postgres', password='pass',
                            host='127.0.0.1', port='5432'
                            )
conn.autocommit = True
cursor = conn.cursor()
conn.commit()

def create_tables():
    sql = """
                CREATE TABLE IF NOT EXISTS email_inference (
                last_email_datetime varchar(1000),
                email_datetimes varchar(1000),
                domain_name varchar(1000)
                    ); """
    cursor.execute(sql)
create_tables()