import os
import logging
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from database.connection import get_connection

# logging.basicConfig(filename='logs/app.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
log_dir = os.path.join(project_root, 'logs')
log_file = os.path.join(log_dir, 'app.log')
logging.basicConfig(filename=log_file, level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

class User:
    def __init__(self, national_id, username, password, email):
        self.national_id = national_id
        self.username = username
        self.password = password
        self.email = email

    def save(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Users (NationalId, Username, Password, Email)
                VALUES (?, ?, ?, ?)
            """, (self.national_id, self.username, self.password, self.email))
            conn.commit()
        except Exception as e:
            logging.error(f"An error occurred while saving user: {e}")
            return "Beklenmeyen bir hata nedeniyle kullanıcı kaydedilemedi."
        finally:
            conn.close()
    
    @staticmethod
    def get_all():
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT UserId, NationalId, Username, Password, Email FROM Users")
            rows = cursor.fetchall()
            return [User(row[1], row[2], row[3], row[4]) for row in rows]
        except Exception as e:
            logging.error(f"An error occurred while fetching all users: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def find_by_id(user_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT UserId, NationalId, Username, Password, Email FROM Users WHERE UserId = ?", (user_id,))
            row = cursor.fetchone()
            if row:
                return User(row[1], row[2], row[3], row[4])
            return None
        except Exception as e:
            logging.error(f"An error occurred while finding user by ID: {e}")
            return None
        finally:
            conn.close()

    def update(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Users SET NationalId = ?, Username = ?, Password = ?, Email = ?
                WHERE UserId = ?
            """, (self.national_id, self.username, self.password, self.email, self.user_id))
            conn.commit()
            print("Kullanıcı başarıyla güncellendi!")
        except Exception as e:
            logging.error(f"An error occurred while updating the user: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete(user_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Users WHERE UserId = ?", (user_id,))
            conn.commit()
        except Exception as e:
            logging.error(f"An error occurred while deleting user: {e}")
            return "Beklenmeyen bir hata nedeniyle kullanıcı silinemedi."
        finally:
            conn.close()
    
    @staticmethod
    def find_by_email_and_password(email, password):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Users WHERE Email = ? AND Password = ?", (email, password))
            row = cursor.fetchone()
            if row:
                return User(row[1], row[2], row[3], row[4])  # Sınıfınıza göre uyarlayın
            return None
        except Exception as e:
            logging.error(f"An error occurred while finding user by email and password: {e}")
            return None
        finally:
            conn.close()