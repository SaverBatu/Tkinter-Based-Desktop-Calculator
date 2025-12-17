import tkinter as tk # Görsel arayüz kütüphanesi

def hesapla():
    try:
        s1 = float(sayi1_giris.get())
        s2 = float(sayi2_giris.get())
        islem = islem_turu.get()
        
        if islem == "+": sonuc = s1 + s2
        elif islem == "-": sonuc = s1 - s2
        elif islem == "*": sonuc = s1 * s2
        elif islem == "/": sonuc = s1 / s2 if s2 != 0 else "Hata!"
        
        label_sonuc.config(text=f"Sonuç: {sonuc}", fg="blue")
    except ValueError:
        label_sonuc.config(text="Lütfen sayı girin!", fg="red")

# 1. Ana Pencere
pencere = tk.Tk()
pencere.title("ASLIYI ÇOK SEVİYORUM")
pencere.geometry("300x250")

# 2. Giriş Kutuları ve Yazılar
tk.Label(pencere, text="Birinci Sayı:").pack(pady=3)
sayi1_giris = tk.Entry(pencere)
sayi1_giris.pack()

tk.Label(pencere, text="İkinci Sayı:").pack(pady=3)
sayi2_giris = tk.Entry(pencere)
sayi2_giris.pack()

# 3. İşlem Seçimi (Açılır Menü)
islem_turu = tk.StringVar(pencere)
islem_turu.set("+") # Varsayılan değer
islem_menu = tk.OptionMenu(pencere, islem_turu, "+", "-", "*", "/")
islem_menu.pack(pady=10)

# 4. Hesapla Butonu
buton = tk.Button(pencere, text="HESAPLA", command=hesapla, bg="green", fg="white")
buton.pack(pady=10)

# 5. Sonuç Yazısı
label_sonuc = tk.Label(pencere, text="Sonuç burada görünecek")
label_sonuc.pack()

pencere.mainloop() # Pencerenin ekranda kalmasını sağlar