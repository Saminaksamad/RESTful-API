from db_conn import conn

cur = conn.cursor()

cur.execute ('CREATE TABLE Products (id SERIAL PRIMARY KEY,'
                                    'title VARCHAR(150) NOT NULL,'
                                    'price DECIMAL (10, 2) NOT NULL,'
                                    'description TEXT,'
                                    'category VARCHAR(255),'
                                    'image VARCHAR(255),'
                                    'rating_rate NUMERIC,'
                                    'rating_count INTEGER,'
                                    'CREATED_AT DATE DEFAULT CURRENT_TIMESTAMP);'
)

cur.execute ('CREATE TABLE category (id SERIAL PRIMARY KEY,'
                                    'name VARCHAR(150) NOT NULL,'
                                    'CREATED_AT DATE DEFAULT CURRENT_TIMESTAMP);'
                                    )

cur.execute ('CREATE TABLE brands (id SERIAL PRIMARY KEY,'
                                    'name VARCHAR(150) NOT NULL,'
                                    'CREATED_AT DATE DEFAULT CURRENT_TIMESTAMP);'
                                    )

conn.commit()
cur.close()
conn.close()
             