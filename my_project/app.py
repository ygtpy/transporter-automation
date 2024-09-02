from my_project.models.user_model import User
from my_project.models.client_model import Client
from my_project.models.transaction_model import Transaction
from my_project.models.photo_model import Photo

def test_user_crud():
    print("\n--- User CRUD Test ---")
    
    user = User(national_id="12345678901", username="janedoe", password="securepassword", email="jane.doe@example.com")
    user.save()
    print("User created!")

    
    users = User.get_all()
    print("All users:")
    for user in users:
        print(f"Username: {user.username}, Email: {user.email}")

    
    user_to_update = User.find_by_id(1)  
    if user_to_update:
        user_to_update.username = "janedoe_updated"
        user_to_update.update()
        print("User updated!")

    
    User.delete(1)
    print("User deleted!")

def test_client_crud():
    print("\n--- Client CRUD Test ---")
    
    client = Client(client_name="ABC Corp", client_type="Company", address="123 Main St", phone="555-1234", email="contact@abccorp.com")
    client.save()
    print("Client created!")

    
    clients = Client.get_all()
    print("All clients:")
    for client in clients:
        print(f"Client Name: {client.client_name}, Email: {client.email}")

    
    client_to_update = Client.find_by_id(1)  
    if client_to_update:
        client_to_update.client_name = "ABC Corp Updated"
        client_to_update.update()
        print("Client updated!")

    
    Client.delete(1) 
    print("Client deleted!")

def test_transaction_crud():
    print("\n--- Transaction CRUD Test ---")
    
    transaction = Transaction(client_id=1, transaction_date="2024-01-01", debit=1000, credit=0, invoice_number="INV123", dispatch_note_number="DN123")
    transaction.save()
    print("Transaction created!")
    
    transactions = Transaction.get_all()
    print("All transactions:")
    for trans in transactions:
        print(f"Transaction ID: {trans.transaction_id}, Transaction Date: {trans.transaction_date}, Debit: {trans.debit}, Credit: {trans.credit}")
    
    transaction_to_update = Transaction.find_by_id(1)
    if transaction_to_update:
        transaction_to_update.debit = 2000
        transaction_to_update.update(transaction_id=1)
        print("Transaction updated!")
    
    Transaction.delete(1)
    print("Transaction deleted!")

def test_photo_crud():
    print("\n--- Photo CRUD Test ---")
    
    photo_data = b"photo_data_bytes_here"
    photo = Photo(transaction_id=1, photo_data=photo_data, photo_type="Invoice")
    photo.save()
    print("Photo created!")

    
    photos = Photo.get_all()
    print("All photos:")
    for photo in photos:
        print(f"Transaction ID: {photo.transaction_id}, Photo Type: {photo.photo_type}")

    
    photo_to_update = Photo.find_by_id(1)
    if photo_to_update:
        photo_to_update.photo_type = "Dispatch Note"
        photo_to_update.update()
        print("Photo updated!")

    
    Photo.delete(1)
    print("Photo deleted!")


def main():
    test_user_crud()
    test_client_crud()
    test_transaction_crud()
    test_photo_crud()

if __name__ == "__main__":
    main()




    

