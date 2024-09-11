from db.db_conn import conn

class categoryrepository:
    def fetch_all_categories(self):
        try:    
            cur = conn.cursor()
            cur.execute('SELECT id, name FROM category')
            data = cur.fetchall()
            categories = [{"id": d[0], "name": d[1]} for d in data]
            return categories
        finally:
            cur.close()

    def fetch_category_by_id(self,category_id):
        try:
            cur = conn.cursor()
            cur.execute ('SELECT id,name FROM category WHERE id = %s', (category_id,))        
            data = cur.fetchone()
            if data:
                category = {
                "id":data[0],
                "name":data[1]
                }
                return category
            else:
                return None
        finally:
            cur.close() 

    def create_category(self,name):
        try:
            cur = conn.cursor()
            cur.execute ("INSERT INTO category (name) VALUES (%s) RETURNING id",(name,))
            data = cur.fetchone()
            conn.commit()
            return data[0]
        except Exception as e:
            raise e
            return None
        finally:
            conn.rollback()
            cur.close()  

    def update_category_by_id(self,new_name, category_id):
        try:
            cur = conn.cursor()
            cur.execute("UPDATE category SET name = %s WHERE id = %s", (new_name,category_id))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()

    def delete_category_by_id(self,category_id):
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM category WHERE id = %s",(category_id,))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()

