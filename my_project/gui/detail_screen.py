
import customtkinter as ctk
from tkinter import filedialog
from my_project.models.transaction_model import Transaction
from my_project.models.photo_model import Photo

def detail_screen(client):
    detail_window = ctk.CTk()
    detail_window.geometry("800x600")
    detail_window.title(f"{client.client_name} - Detaylar")

    ctk.CTkLabel(detail_window, text=f"{client.client_name} Detayları", font=("Arial", 24)).pack(pady=20)

    transaction_combobox = ctk.CTkComboBox(detail_window, width=300)
    transaction_combobox.pack(pady=20)

    photo_combobox = ctk.CTkComboBox(detail_window, width=300)
    photo_combobox.pack(pady=20)

    def load_details():
        
        transaction_combobox.configure(values=[])
        transactions = Transaction.get_all()
        client_transactions = [f"{t.transaction_date} - {t.debit}/{t.credit}" for t in transactions if t.client_id == client.client_id]
        if client_transactions:
            transaction_combobox.configure(values=client_transactions)
            transaction_combobox.set(client_transactions[0])  

        
        photo_combobox.configure(values=[])
        photos = Photo.get_all()
        client_photos = [f"Photo Type: {p.photo_type}" for p in photos if p.transaction_id in [t.transaction_id for t in transactions]]
        if client_photos:
            photo_combobox.configure(values=client_photos)
            photo_combobox.set(client_photos[0])

    def add_new_transaction():
        transaction_date = date_entry.get()
        debit = float(debit_entry.get())
        credit = float(credit_entry.get())
        invoice_number = invoice_entry.get()
        dispatch_note_number = dispatch_entry.get()

        transaction = Transaction(client.client_id, transaction_date, debit, credit, invoice_number, dispatch_note_number)
        transaction.save()
        load_details()

    def add_photo():
        file_path = filedialog.askopenfilename(title="Fotoğraf Seç", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            transaction_index = transaction_combobox.current()
            if transaction_index >= 0:
                selected_transaction = transactions[transaction_index]
                photo = Photo(transaction_id=selected_transaction.transaction_id, photo_data=file_path, photo_type="Invoice")
                photo.save()
                load_details()
            else:
                ctk.CTkLabel(detail_window, text="Lütfen bir işlem seçin!", text_color="red").pack(pady=10)

    
    ctk.CTkLabel(detail_window, text="Yeni İşlem Ekle", font=("Arial", 18)).pack(pady=10)

    date_entry = ctk.CTkEntry(detail_window, placeholder_text="Tarih (YYYY-MM-DD)", width=300)
    date_entry.pack(pady=5)

    debit_entry = ctk.CTkEntry(detail_window, placeholder_text="Borç (Debit)", width=300)
    debit_entry.pack(pady=5)

    credit_entry = ctk.CTkEntry(detail_window, placeholder_text="Alacak (Credit)", width=300)
    credit_entry.pack(pady=5)

    invoice_entry = ctk.CTkEntry(detail_window, placeholder_text="Fatura No", width=300)
    invoice_entry.pack(pady=5)

    dispatch_entry = ctk.CTkEntry(detail_window, placeholder_text="İrsaliye No", width=300)
    dispatch_entry.pack(pady=5)

    ctk.CTkButton(detail_window, text="İşlem Ekle", command=add_new_transaction).pack(pady=10)

    
    ctk.CTkButton(detail_window, text="Fotoğraf Ekle", command=add_photo).pack(pady=10)

    load_details()

    detail_window.mainloop()
