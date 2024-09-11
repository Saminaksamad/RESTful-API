
import json
from db_conn import conn

cur = conn.cursor()

categories = ["electronics","jewelery","men's clothing","women's clothing","footwear","home appliances","books and media","beauty and personal care"]
for c in categories:
    cur.execute ("INSERT INTO category (name) VALUES (%s)",(c,))


brands = ["apple","puma","zara","nike","whirlpool","adidas","panasonic","LG"]
for b in brands:
    cur.execute ("INSERT INTO brands (name) VALUES (%s)",(b,))


def load_products_data(file_name):
    with open (file_name,'r',encoding="UTF-8")as file:
        return json.load(file)
    
json_file_path = 'db/products.json'    
products = load_products_data(json_file_path)
insert_query = """
INSERT INTO products (title, price, description, category, image, rating_rate, rating_count) VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
try:    
    for p in products:
        values = (
                p.get('title'),
                p.get('price'),
                p.get('description'),
                p.get('category'),
                p.get('image'),
                p.get('rating', {}).get('rate'),
                p.get('rating', {}).get('count')
            )
        cur.execute(insert_query, values)        
    conn.commit()    
except Exception as e:
    conn.rollback()
    print (f"error : {e}")                     

conn.commit()
cur.close()
conn.close()
            

