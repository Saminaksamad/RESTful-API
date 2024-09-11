import psycopg2

conn = psycopg2.connect(
    dsn = 'postgresql://postgres:sami@localhost:5432/e-commerce'
)