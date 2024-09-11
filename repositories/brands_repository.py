from db.db_conn import conn

class brandrepository():
    def fetch_all_brands(self):
        try:    
            cur = conn.cursor()
            cur.execute('SELECT id, name FROM brands')
            data = cur.fetchall()
            brands = [{"id": d[0], "name": d[1]} for d in data]
            return brands
        finally:
            cur.close()

    def fetch_brand_by_id(self,brand_id):
        try:
            cur = conn.cursor()
            cur.execute ('SELECT id,name FROM brands WHERE id = %s', (brand_id,))        
            data = cur.fetchone()
            if data:
                brand = {
                "id":data[0],
                "name":data[1]
                }
                return brand
            else:
                return None
        finally:
            cur.close() 

    def create_brand(self, name):
        try:
            cur = conn.cursor()
            cur.execute ("INSERT INTO brands (name) VALUES (%s) RETURNING id",(name,))
            data = cur.fetchone()
            conn.commit()
            return data[0]
        except Exception as e:
            raise e
            return None
        finally:
            conn.rollback()
            cur.close()  

    def update_brand_by_id(self, new_name, brand_id):
        try:
            cur = conn.cursor()
            cur.execute("UPDATE brands SET name = %s WHERE id = %s", (new_name,brand_id))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()

    def delete_brand_by_id(self, brand_id):
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM brands WHERE id = %s",(brand_id,))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
