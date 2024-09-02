import logging
from database.connection import get_connection

logging.basicConfig(filename='logs/app.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

class Photo:
    def __init__(self, transaction_id, photo_data, photo_type):
        self.transaction_id = transaction_id
        self.photo_data = photo_data
        self.photo_type = photo_type
        
    def save(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Photos (TransactionId, Photo, PhotoType)
                VALUES (?, ?, ?)
            """, (self.transaction_id, self.photo_data, self.photo_type))
            conn.commit()
        except Exception as e:
            logging.error(f"An error occurred while saving photo: {e}")
            return "Beklenmeyen bir hata nedeniyle fotoğraf kaydedilemedi."
        finally:
            conn.close()
            
    @staticmethod
    def get_all():
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT PhotoId, TransactionId, Photo, PhotoType FROM Photos")
            rows = cursor.fetchall()
            return [Photo(row[1], row[2], row[3]) for row in rows]  
        except Exception as e:
            logging.error(f"Bir hata oluştu!: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def find_by_id(photo_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT PhotoId, TransactionId, Photo, PhotoType FROM Photos WHERE PhotoId = ?", (photo_id,))
            row = cursor.fetchone()
            if row:
                return Photo(row[1], row[2], row[3]) 
            return None 
        except Exception as e:
            logging.error(f"Bir hata oluştu!: {e}")
            return None
        finally:
            conn.close()
            
    def update(self, photo_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Photos SET TransactionId = ?, Photo = ?, PhotoType = ?
                WHERE PhotoId = ?
            """, (self.transaction_id, self.photo_data, self.photo_type, photo_id))
            conn.commit()
        except Exception as e:
            logging.error(f"Bir hata oluştu: {e}")
            return "Fotoğraf güncellenemedi"
        finally:
            conn.close()

    @staticmethod
    def delete(photo_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Photos WHERE PhotoId = ?", (photo_id,))
            conn.commit()
        except Exception as e:
            logging.error(f"Bir hata oluştu: {e}")
            return "Bir hata oluştu"
        finally:
            conn.close()
