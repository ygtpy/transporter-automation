import logging
from database.connection import get_connection

logging.basicConfig(filename='logs/app.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

class Client:
    def __init__(self, client_name, client_type, address=None, phone=None, email=None, client_id=None):
        self.client_name = client_name
        self.client_type = client_type
        self.address = address
        self.phone = phone
        self.email = email
        self.client_id = client_id

    def save(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Clients (ClientName, ClientType, Address_, Phone, Email)
                VALUES (?, ?, ?, ?, ?)
            """, (self.client_name, self.client_type, self.address, self.phone, self.email))
            conn.commit()
            print("Client saved successfully!")  
        except Exception as e:
            logging.error(f"An error occurred while saving client: {e}")
            print(f"Error: {e}")
            return "Beklenmeyen bir hata nedeniyle istemci kaydedilemedi."
        finally:
            conn.close()


    @staticmethod
    def get_all():
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT ClientId, ClientName, ClientType, Address_, Phone, Email FROM Clients")
            rows = cursor.fetchall()
            return [Client(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows] 
        except Exception as e:
            logging.error(f"An error occurred while fetching all clients: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def find_by_id(client_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT ClientId, ClientName, ClientType, Address_, Phone, Email FROM Clients WHERE ClientId = ?", (client_id,))
            row = cursor.fetchone()
            if row:
                return Client(row[1], row[2], row[3], row[4], row[5], row[0])
            return None
        except Exception as e:
            logging.error(f"An error occurred while finding client by ID: {e}")
            return None
        finally:
            conn.close()

    def update(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Clients SET ClientName = ?, ClientType = ?, Address_ = ?, Phone = ?, Email = ?
                WHERE ClientId = ?
            """, (self.client_name, self.client_type, self.address, self.phone, self.email, self.client_id))
            conn.commit()
            print("başarılı")
        except Exception as e:
            logging.error(f"An error occurred while updating client: {e}")
            return "Beklenmeyen bir hata nedeniyle istemci güncellenemedi."
        finally:
            conn.close()

    @staticmethod    
    def delete(client_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Clients WHERE ClientId = ?", (client_id,))
            conn.commit()
            print("başarılı")
        except Exception as e:
            logging.error(f"An error occurred while deleting client: {e}")
            return "Beklenmeyen bir hata nedeniyle istemci güncellenemedi."
        finally:
            conn.close()
