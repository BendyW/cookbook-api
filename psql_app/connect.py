import psycopg2
from config import load_config

def connect(config):
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def createDatabase():
    cursor = conn.cursor()

    schema_sql = ("""CREATE TABLE IF NOT EXISTS user_data(
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_edited TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

    CREATE TABLE IF NOT EXISTS recipe(
        id SERIAL PRIMARY KEY,
        user_id integer REFERENCES user_data,
        content TEXT NOT NULL,
        source_url TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_edited TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
        """)

    cursor.execute(schema_sql)
    conn.commit()
    cursor.close()
    print("Database created successfully........")


if __name__ == '__main__':
    config = load_config()
    conn = connect(config)
    createDatabase()
    conn.close()
    print("Connection closed........")
# conn.autocommit = True