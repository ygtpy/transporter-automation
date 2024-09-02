import logging
from database.connection  import get_connection

class Transaction:
    def __init__(self, client_id, transaction_date, debit, credit, invoice_number=None, dispatch_note_number=None, transaction_id=None):
        self.transaction_id = transaction_id
        self.client_id = client_id
        self.transaction_date = transaction_date
        self.debit = debit
        self.credit = credit
        self.invoice_number = invoice_number
        self.dispatch_note_number = dispatch_note_number 

    def save(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Transactions (ClientId, TransactionDate, Debit, Credit, InvoiceNumber, DispatchNoteNumber)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (self.client_id, self.transaction_date, self.debit, self.credit, self.invoice_number, self.dispatch_note_number))
            conn.commit()
        except Exception as e:
            logging.error(f"An error occurred while saving the transaction: {e}")
            return "Beklenmedik bir hata oluştu (save). Lütfen tekrar dene."
        finally:
            conn.close()
        
    @staticmethod
    def get_all():
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT TransactionId, ClientId, TransactionDate, Debit, Credit, InvoiceNumber, DispatchNoteNumber FROM Transactions")
            rows = cursor.fetchall()
            transactions = []
            for row in rows:
                transaction = Transaction(
                    transaction_id=row.TransactionId,
                    client_id=row.ClientId,
                    transaction_date=row.TransactionDate,
                    debit=row.Debit,
                    credit=row.Credit,
                    invoice_number=row.InvoiceNumber,
                    dispatch_note_number=row.DispatchNoteNumber
                )
                transactions.append(transaction)
            return transactions
        except Exception as e:
            logging.error(f"An error occurred while fetching transactions: {e}")
            return []
        finally:
            conn.close()
            
    @staticmethod
    def find_by_id(transaction_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Transactions WHERE TransactionId = ?", (transaction_id,))
            row = cursor.fetchone()
            if row:
                return Transaction(row[1], row[2], row[3], row[4], row[5], row[6])
            return None
        except Exception as e:
            logging.error(f"An error occurred while finding transaction by ID: {e}")
            return "Beklenmedik bir hata oluştu (find). Lütfen tekrar dene."
        finally:
            conn.close()
    
    def update(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Transactions SET ClientId = ?, TransactionDate = ?, Debit = ?, Credit = ?, InvoiceNumber = ?, DispatchNoteNumber = ?
                WHERE TransactionId = ?
            """, (self.client_id, self.transaction_date, self.debit, self.credit, self.invoice_number, self.dispatch_note_number, self.transaction_id))
            conn.commit()
        except Exception as e:
            logging.error(f"An error occurred while updating the transaction: {e}")
            return "Beklenmedik bir hata oluştu (update). Lütfen tekrar dene."
        finally:
            conn.close()
        
    @staticmethod
    def delete(transaction_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Transactions WHERE TransactionId = ?", (transaction_id,))
            conn.commit()
        except Exception as e:
            logging.error(f"An error occurred while deleting the transaction: {e}")
            return "Beklenmedik bir hata oluştu (delete). Lütfen tekrar dene."
        finally:
            conn.close()
