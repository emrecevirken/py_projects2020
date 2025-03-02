import tkinter as tk
from tkinter import messagebox
import math

# Hesaplama fonksiyonu
def hesapla(islem):
    try:
        sayi1 = float(entry1.get())
        sayi2 = float(entry2.get()) if islem not in ["sqrt"] else None

        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        elif islem == "/":
            if sayi2 == 0:
                messagebox.showerror("Hata", "Sıfıra bölme hatası!")
                return
            sonuc = sayi1 / sayi2
        elif islem == "^":
            sonuc = sayi1 ** sayi2
        elif islem == "%":
            sonuc = sayi1 % sayi2
        elif islem == "sqrt":
            if sayi1 < 0:
                messagebox.showerror("Hata", "Negatif sayıların karekökü alınamaz!")
                return
            sonuc = math.sqrt(sayi1)
        else:
            messagebox.showerror("Hata", "Geçersiz işlem!")
            return

        # Sonucu ekrana yazdır
        sonuc_label.config(text=f"Sonuç: {sonuc}")

    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin!")

# Tkinter arayüzü
window = tk.Tk()
window.title("Hesap Makinesi")
window.geometry("300x400")
window.config(bg="#f4f4f4")

# Sayı girişleri
tk.Label(window, text="1. Sayı:", bg="#f4f4f4").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="2. Sayı:", bg="#f4f4f4").pack()
entry2 = tk.Entry(window)
entry2.pack()

# İşlem butonları
button_frame = tk.Frame(window, bg="#f4f4f4")
button_frame.pack(pady=10)

operations = ["+", "-", "*", "/", "^", "%", "sqrt"]
for op in operations:
    tk.Button(button_frame, text=op, width=5, command=lambda o=op: hesapla(o)).pack(side="left", padx=5)

# Sonuç etiketi
sonuc_label = tk.Label(window, text="Sonuç: ", bg="#f4f4f4", font=("Arial", 12, "bold"))
sonuc_label.pack(pady=10)

# Çıkış butonu
tk.Button(window, text="Çıkış", command=window.quit, bg="red", fg="white").pack(pady=10)

# Arayüzü başlat
window.mainloop()
