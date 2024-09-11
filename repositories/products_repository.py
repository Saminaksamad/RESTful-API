from collections import OrderedDict
import json
from db.db_conn import conn

def serialize_product(product):
    ordered_product = OrderedDict([
        ("id", product[0]),
        ("title", product[1]),
        ("price", product[2]),
        ("description", product[3]),
        ("category", product[4]),
        ("image", product[5]),        
        ("rating", OrderedDict([
            ("rate", product[6]),
            ("count", product[7])
        ]))
    ])
    return (ordered_product)

class productrepository():
    def fetch_all_products(self):
        try:    
            cur = conn.cursor()
            cur.execute('SELECT id, title, price, description, category, image, rating_rate, rating_count FROM products')
            data = cur.fetchall()
            products = [serialize_product(d) for d in data]        
            return (products)
        except Exception as e:
            print (f"error : {e}")
        finally:
            cur.close()

    def fetch_product_by_id(self,product_id):
        try:
            cur = conn.cursor()
            cur.execute ('SELECT id,title, price, description, category, image, rating_rate, rating_count FROM products WHERE id = %s', (product_id,))        
            data = cur.fetchone()
            if data:
                return serialize_product(data)            
            else:
                return None
        finally:
            cur.close()

    def create_product(self,new_product):
        cur = conn.cursor()
        insert_query = """
        INSERT INTO products (title, price, description, category, image, rating_rate, rating_count) 
        VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id
        """
        values = (
                new_product.get('title'),
                new_product.get('price'),
                new_product.get('description'),
                new_product.get('category'),
                new_product.get('image'),
                new_product.get('rating', {}).get('rate'),
                new_product.get('rating', {}).get('count')
                )
        try: 
            cur.execute(insert_query, values)        
            conn.commit()
            data = cur.fetchone()
            return data[0]    
        except Exception as e:
            conn.rollback()
            print (f"error : {e}")
        finally:
            cur.close()

    def update_product_by_id(self,new_product,product_id):
        update_query = """
        UPDATE products SET title = %s, price = %s, description = %s, category = %s, image = %s,
        rating_rate = %s, rating_count = %s WHERE id = %s
        """
        values = (
                new_product.get('title'),
                new_product.get('price'),
                new_product.get('description'),
                new_product.get('category'),
                new_product.get('image'),
                new_product.get('rating', {}).get('rate'),
                new_product.get('rating', {}).get('count'),
                product_id
                )
        try:
            cur = conn.cursor()
            cur.execute(update_query, values)
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            print (f"error : {e}")
        finally:
            cur.close()

    def delete_product_by_id(self,product_id):
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM products WHERE id = %s",(product_id,))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
            