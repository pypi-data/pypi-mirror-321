import customtkinter as ctk
from gpt4all import GPT4All
import os
import sys
from tkinter import filedialog

# Функция для загрузки модели
def load_model(model_path):
    return GPT4All(model_path, allow_download=False)

# Функция для генерации текста
def generate_text(model_path, prompt, max_tokens):
    model = load_model(model_path)
    with model.chat_session():
        response = model.generate(prompt, max_tokens=max_tokens)

    # Разделение текста и кода
    parts = response.split('```python')
    text_parts = []
    code_parts = []

    for i, part in enumerate(parts):
        if i == 0:
            text_parts.append(part)
        else:
            code, text = part.split('```', 1)
            code_parts.append(code.strip())
            text_parts.append(text.strip())

    return "\n".join(text_parts), "\n".join(code_parts)

# Определение пути к временной директории PyInstaller
if getattr(sys, 'frozen', False):
    # Если скрипт запущен из исполняемого файла
    application_path = sys._MEIPASS
else:
    # Если скрипт запущен из исходного кода
    application_path = os.path.dirname(os.path.abspath(__file__))

# Создание интерфейса
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Графический интерфейс для GPT4All")
        self.geometry("1000x800")

        # Левая панель
        self.left_frame = ctk.CTkFrame(self, width=200, corner_radius=10)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.model_path_label = ctk.CTkLabel(self.left_frame, text="Выберите модель нейросети")
        self.model_path_label.pack(pady=10)

        self.model_path_button = ctk.CTkButton(self.left_frame, text="Выбрать модель", command=self.select_model)
        self.model_path_button.pack(pady=10)

        self.model_path_display = ctk.CTkLabel(self.left_frame, text="", wraplength=180)
        self.model_path_display.pack(pady=10)

        self.prompt_label = ctk.CTkLabel(self.left_frame, text="Введите текст для генерации")
        self.prompt_label.pack(pady=10)

        self.prompt = ctk.CTkTextbox(self.left_frame, width=180, height=100)
        self.prompt.pack(pady=10)

        self.max_tokens_label = ctk.CTkLabel(self.left_frame, text="Максимальное количество токенов")
        self.max_tokens_label.pack(pady=10)

        self.max_tokens = ctk.CTkEntry(self.left_frame)
        self.max_tokens.insert(0, "4096")
        self.max_tokens.pack(pady=10)

        self.generate_button = ctk.CTkButton(self.left_frame, text="Сгенерировать текст", command=self.generate_text)
        self.generate_button.pack(pady=10)

        # Правая панель
        self.right_frame = ctk.CTkFrame(self, corner_radius=10)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.text_output_label = ctk.CTkLabel(self.right_frame, text="Сгенерированный текст")
        self.text_output_label.pack(pady=10)

        self.text_output = ctk.CTkTextbox(self.right_frame, width=700, height=300)
        self.text_output.pack(pady=10)

        self.code_output_label = ctk.CTkLabel(self.right_frame, text="Сгенерированный код")
        self.code_output_label.pack(pady=10)

        self.code_output = ctk.CTkTextbox(self.right_frame, width=700, height=300)
        self.code_output.pack(pady=10)

    def select_model(self):
        self.model_path = filedialog.askopenfilename(filetypes=[("GPT4All Models", "*.gguf")])
        if self.model_path:
            self.model_path_display.configure(text=os.path.basename(self.model_path))

    def generate_text(self):
        prompt = self.prompt.get("1.0", ctk.END).strip()
        max_tokens = int(self.max_tokens.get())

        if hasattr(self, 'model_path') and self.model_path:
            text, code = generate_text(self.model_path, prompt, max_tokens)

            self.text_output.delete("1.0", ctk.END)
            self.text_output.insert(ctk.END, text)

            self.code_output.delete("1.0", ctk.END)
            self.code_output.insert(ctk.END, code)
        else:
            self.text_output.delete("1.0", ctk.END)
            self.text_output.insert(ctk.END, "Пожалуйста, выберите модель.")

def run():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    run()