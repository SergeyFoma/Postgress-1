import sys
sys.path.append('./Postgress-1/venv/Lib/site-packages')
import customtkinter as ctk

# Настройка внешнего вида
ctk.set_appearance_mode("system") # Доступные режимы: "dark", "light", "system"
ctk.set_default_color_theme("green") # Темы: "blue", "green", "dark-blue"

# Создание окна приложения
app = ctk.CTk()
app.title("CustomTkinter Demo")
app.geometry("400x300")

# Добавление виджетов
label = ctk.CTkLabel(app, text="Пример приложения на CustomTkinter")
label.pack(pady=10)

entry = ctk.CTkEntry(app, width=300)
entry.pack(pady=10)

button = ctk.CTkButton(app, text="Нажми меня")
button.pack(pady=10)

# Запуск приложения
app.mainloop()

