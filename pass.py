import re
import tkinter as tk
from tkinter import ttk

class PasswordStrengthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Şifre Güçlülük Ölçer")

        self.label = ttk.Label(root, text="Güçlü bir şifre oluşturun:")
        self.label.pack(pady=10)

        self.password_entry = ttk.Entry(root, show='*')
        self.password_entry.pack(pady=5)

        self.calculate_button = ttk.Button(root, text="Hesapla", command=self.calculate_strength)
        self.calculate_button.pack(pady=5)

        self.result_label = ttk.Label(root, text="", font=('Helvetica', 12, 'bold'))
        self.result_label.pack(pady=10)

    def calculate_strength(self):
        password = self.password_entry.get()
        strength = self.calculate_password_strength(password)
        self.display_strength(strength)

    def calculate_password_strength(self, password):
        score = 0
        
        # Uzunluk değerlendirmesi
        length = len(password)
        if length >= 12:
            score += 30
        elif length >= 8:
            score += 15
        
        # Büyük harf kontrolü
        if re.search(r'[A-Z]', password):
            score += 15
        
        # Küçük harf kontrolü
        if re.search(r'[a-z]', password):
            score += 15
        
        # Rakam kontrolü
        if re.search(r'[0-9]', password):
            score += 15
        
        # Özel karakter kontrolü
        special_chars = re.findall(r'[!@#$%^&*()?":{}|<>]', password)
        score += len(special_chars) * 10
        
        # Boşluk kontrolü
        spaces = password.count(' ')
        score += spaces * 10
        
        return score

    def display_strength(self, strength):
        self.result_label.config(text=f"Parola skorunuz : {strength}")

def main():
    root = tk.Tk()
    app = PasswordStrengthApp(root)
    root.geometry("300x200")
    root.mainloop()

if __name__ == "__main__":
    main()
