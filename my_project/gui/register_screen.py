import customtkinter as ctk
from my_project.models.user_model import User


def register_screen():
    register_window = ctk.CTkToplevel()
    register_window.geometry("400x500")
    register_window.title("Nakliyeci Otomasyon - Kayıt Ol")

    def register_user():
        national_id = national_id_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()

        user = User(national_id, username, password, email)
        save_status = user.save()

        if save_status:
            ctk.CTkLabel(register_window, text="Kayıt başarılı!", text_color="green").pack(pady=10)
            register_window.destroy()
        else:
            ctk.CTkLabel(register_window, text="E-posta zaten kayıtlı!", text_color="red").pack(pady=10)

    ctk.CTkLabel(register_window, text="Kayıt Ol", font=("Arial", 24)).pack(pady=40)

    national_id_entry = ctk.CTkEntry(register_window, placeholder_text="Kimlik No", width=300)
    national_id_entry.pack(pady=10)

    username_entry = ctk.CTkEntry(register_window, placeholder_text="Kullanıcı Adı", width=300)
    username_entry.pack(pady=10)
    
    password_entry = ctk.CTkEntry(register_window, placeholder_text="Şifre", show="*", width=300)
    password_entry.pack(pady=10)

    email_entry = ctk.CTkEntry(register_window, placeholder_text="E-posta", width=300)
    email_entry.pack(pady=10)

    ctk.CTkButton(register_window, text="Kayıt Ol", width=300, command=register_user).pack(pady=20)
