# import customtkinter as ctk
# from my_project.models.user_model import User
# from gui.register_screen import register_screen
# from gui.main_screen import main_screen


# def login_screen():
#     app = ctk.CTk()
#     app.geometry("400x500")
#     app.title("Nakliyeci Otomasyon - Giriş")

#     def authenticate():
#         email = email_entry.get()
#         password = password_entry.get()
#         user = User.find_by_email_and_password(email, password)
#         if user:
#             main_screen(user)
#             app.destroy()
#         else:
#             ctk.CTkLabel(app, text="Geçersiz e-posta veya şifre!", text_color="red").pack(pady=10)

#     ctk.CTkLabel(app, text="Giriş Yap", font=("Arial", 24)).pack(pady=40)

#     email_entry = ctk.CTkEntry(app, placeholder_text="E-posta", width=300)
#     email_entry.pack(pady=10)
    
#     password_entry = ctk.CTkEntry(app, placeholder_text="Şifre", show="*", width=300)
#     password_entry.pack(pady=10)

#     ctk.CTkButton(app, text="Giriş Yap", width=300, command=authenticate).pack(pady=20)
#     ctk.CTkButton(app, text="Kayıt Ol", width=300, command=register_screen).pack(pady=10)

#     app.mainloop()

import customtkinter as ctk
from my_project.models.user_model import User
from gui.register_screen import register_screen
from gui.main_screen import main_screen

def login_screen():
    app = ctk.CTk()
    app.geometry("400x500")
    app.title("Nakliyeci Otomasyon - Giriş")

    def authenticate():
        email = email_entry.get()
        password = password_entry.get()
        user = User.find_by_email_and_password(email, password)
        if user:
            main_screen(user)
            app.destroy()
        else:
            ctk.CTkLabel(app, text="Geçersiz e-posta veya şifre!", text_color="red").pack(pady=10)

    ctk.CTkLabel(app, text="Giriş Yap", font=("Arial", 24)).pack(pady=40)

    email_entry = ctk.CTkEntry(app, placeholder_text="E-posta", width=300)
    email_entry.pack(pady=10)
    
    password_entry = ctk.CTkEntry(app, placeholder_text="Şifre", show="*", width=300)
    password_entry.pack(pady=10)

    ctk.CTkButton(app, text="Giriş Yap", width=300, command=authenticate).pack(pady=20)
    ctk.CTkButton(app, text="Kayıt Ol", width=300, command=register_screen).pack(pady=10)

    app.mainloop()
