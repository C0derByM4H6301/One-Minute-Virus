import time
import tkinter as tk
import os

def shutdown():
    # Pencereyi kapat
    window.destroy()
    window.quit()

    # Bilgisayarı kapat
    os.system("shutdown /s /t 1")

# 60 saniye bekle
time.sleep(60)

# Pencereyi oluştur
window = tk.Tk()
window.geometry("300x200+500+300")
window.title("Bilgisayar Kapatılacak")

# Pencere içine bir etiket ekle
label = tk.Label(window, text="Bilgisayar 2 saniye içinde kapanacak.")
label.pack()

# Pencereyi göster
window.update()

# 2 saniye bekle
time.sleep(2)

# Bilgisayarı kapat
shutdown()
