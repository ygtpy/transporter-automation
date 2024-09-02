
# import tkinter as tk  
# import customtkinter as ctk
# from my_project.models.client_model import Client
# from gui.detail_screen import detail_screen
# from gui.add_client import add_client

# def main_screen(user):
#     main_window = ctk.CTk()
#     main_window.geometry("800x600")
#     main_window.title("Nakliyeci Otomasyon - Ana Ekran")

#     ctk.CTkLabel(main_window, text=f"Hoşgeldiniz, {user.username}", font=("Arial", 20)).pack(pady=20)
#     ctk.CTkLabel(main_window, text="Şirketler ve Kişiler", font=("Arial", 24)).pack(pady=20)

    
#     scrollable_frame = ctk.CTkScrollableFrame(main_window, width=400, height=300)
#     scrollable_frame.pack(pady=20)

#     def load_clients():
#         for widget in scrollable_frame.winfo_children():
#             widget.destroy()

#         clients = Client.get_all()
#         for client in clients:
#             client_button = ctk.CTkButton(scrollable_frame, text=client.client_name, 
#                                           command=lambda c=client: view_details(c))
#             client_button.pack(pady=5, padx=5)

#     def view_details(client):
#         detail_screen(client)

#     load_clients()

#     ctk.CTkButton(main_window, text="Detayları Görüntüle", command=lambda: view_details(Client.get_all()[0])).pack(pady=10)
#     ctk.CTkButton(main_window, text="Yeni Şirket/Kişi Ekle", command=lambda: add_client(load_clients)).pack(pady=10)

#     main_window.mainloop()

import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
import requests
import time
import threading
from my_project.models.client_model import Client
from gui.detail_screen import detail_screen
from gui.add_client import add_client

def main_screen(user):
    main_window = ctk.CTk()
    main_window.geometry("1000x700")
    main_window.title("Nakliyeci Otomasyon - Ana Ekran")

    ctk.CTkLabel(main_window, text=f"Hoşgeldiniz, {user.username}", font=("Arial", 20)).pack(pady=20)
    ctk.CTkLabel(main_window, text="Şirketler ve Kişiler", font=("Arial", 24)).pack(pady=20)

    profile_button = ctk.CTkButton(main_window, text="Profil Fotoğrafı Yükle", command=lambda: upload_photo(profile_label))
    profile_button.place(x=20, y=20)

    profile_label = ctk.CTkLabel(main_window, text="Profil Fotoğrafı")
    profile_label.place(x=20, y=60)

    clock_label = ctk.CTkLabel(main_window, text="", font=("Arial", 12))
    clock_label.place(x=800, y=650)
    update_clock(clock_label)

    weather_label = ctk.CTkLabel(main_window, text="Hava Durumu", font=("Arial", 12))
    weather_label.place(x=180, y=60)
    get_weather("Istanbul", weather_label)

    open_page_button = ctk.CTkButton(main_window, text="Boş Sayfa Aç", command=open_empty_page)
    open_page_button.place(x=20, y=150)

    scrollable_frame = ctk.CTkScrollableFrame(main_window, width=400, height=300)
    scrollable_frame.pack(pady=20)

    def load_clients():
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        clients = Client.get_all()
        for client in clients:
            client_button = ctk.CTkButton(scrollable_frame, text=client.client_name, 
                                          command=lambda c=client: view_details(c))
            client_button.pack(pady=5, padx=5)

    def view_details(client):
        detail_screen(client)

    load_clients()

    ctk.CTkButton(main_window, text="Detayları Görüntüle", command=lambda: view_details(Client.get_all()[0])).pack(pady=10)
    ctk.CTkButton(main_window, text="Yeni Şirket/Kişi Ekle", command=lambda: add_client(load_clients)).pack(pady=10)

    main_window.mainloop()

def upload_photo(profile_label):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((100, 100))
        profile_image = ImageTk.PhotoImage(image)
        profile_label.configure(image=profile_image)
        profile_label.image = profile_image

def update_clock(clock_label):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    clock_label.configure(text=now)
    clock_label.after(1000, lambda: update_clock(clock_label))

def get_weather(city, weather_label):
    def fetch_weather():
        api_key = "b6addf9a907fdc1bdef4e389e8e55912"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url)
            data = response.json()
            if 'main' in data:
                temperature = data['main']['temp']
                description = data['weather'][0]['description']
                weather_info = f"{city}: {temperature}°C, {description.capitalize()}"
                weather_label.configure(text=weather_info)
            else:
                weather_label.configure(text="Hava durumu alınamadı.")
        except Exception as e:
            weather_label.configure(text="Hava durumu alınamadı.")
            print(f"Hata: {e}")

    threading.Thread(target=fetch_weather).start()

def open_empty_page():
    empty_window = ctk.CTkToplevel()
    empty_window.geometry("400x300")
    empty_window.title("Boş Sayfa")
    ctk.CTkLabel(empty_window, text="Bu sayfaya daha sonra içerik eklenecek.", font=("Arial", 16)).pack(pady=20)


