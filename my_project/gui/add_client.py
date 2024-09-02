import customtkinter as ctk
from my_project.models.client_model import Client

def add_client(refresh_function):
    add_window = ctk.CTkToplevel()
    add_window.geometry("400x300")
    add_window.title("Yeni Şirket/Kişi Ekle")

    def add_new_client():
        client_name = name_entry.get()
        client_type = type_entry.get()
        address = address_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()

        if client_name and client_type:
            client = Client(client_name, client_type, address, phone, email)
            client.save()
            refresh_function()
            add_window.destroy()
        else:
            ctk.CTkLabel(add_window, text="Lütfen zorunlu alanları doldurun!", text_color="red").pack(pady=10)

    ctk.CTkLabel(add_window, text="Yeni Şirket/Kişi Ekle", font=("Arial", 20)).pack(pady=20)

    name_entry = ctk.CTkEntry(add_window, placeholder_text="Şirket/Kişi Adı", width=300)
    name_entry.pack(pady=10)

    type_entry = ctk.CTkEntry(add_window, placeholder_text="Tipi (Firma/Bireysel)", width=300)
    type_entry.pack(pady=10)

    address_entry = ctk.CTkEntry(add_window, placeholder_text="Adres", width=300)
    address_entry.pack(pady=10)

    phone_entry = ctk.CTkEntry(add_window, placeholder_text="Telefon", width=300)
    phone_entry.pack(pady=10)

    email_entry = ctk.CTkEntry(add_window, placeholder_text="E-posta", width=300)
    email_entry.pack(pady=10)

    ctk.CTkButton(add_window, text="Ekle", command=add_new_client).pack(pady=20)
