#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Türk Kahvesi Fal Makinesi
Gerçekten çalışır ama hiç işe yaramaz. Sabırınızı test eder.
"""

import time
import random
import base64

def demle_kahve():
    print("☕ Kahve çekirdekleri öğütülüyor... (abartılı şekilde, gerçekten)")
    for i in range(5):
        print(f"  Öğütme aşaması {i+1}/5: Zrrrrrrt! Çekirdekler ağlıyor!")
        time.sleep(1)
    print("☕ Cezveye su konuyor... Su da şaşkın.")
    time.sleep(2)
    print("☕ Ateşe oturtuluyor... Köpük bekleniyor, bekleniyor, bekleniyor...")
    for i in range(3):
        print("  Köpük yükseliyor... ama sonra düşüyor. Drama!")
        time.sleep(1.5)
    print("✅ Kahve hazır! Fincana dökülüyor. Gerçek değil ama olsun.")

def fal_bak(isim):
    fallar = [
        f"{isim}, yakın zamanda bir kedi seni takip edecek ve sonra kaybolacak. Bu iyiye işaret. Ya da kötü. Bilmiyorum.",
        f"{isim}, iş yerinde birisi senin kahveni içecek. İntikam al ama nazikçe. Belki de kendi kahveni içersin.",
        f"{isim}, fincanda bir gemi görüyorum... ama batıyor. Yüzme öğren. Ya da gemi almayı bırak.",
        f"{isim}, aşk hayatın bir çay kaşığı kadar karışık. Karıştır ama dökme. Dökersen temizle.",
        f"{isim}, büyük bir değişim geliyor. Belki de sadece çaydan çayına geçersin. Ya da kahveden kahveye."
    ]
    # Gizli siyasi mesaj saklı burada. Decode ederseniz: demokrasi fincanında erimez
    gizli_mesaj = "ZGVtb2tyYXNpIGZpbmNhbsSxbmRhIGVyaW1leg=="
    # Eğer merak ederseniz: print(base64.b64decode(gizli_mesaj).decode())
    
    print(random.choice(fallar))
    print("\n🔮 Fal bitti. Fincanı çevirmeyi unutma, yoksa sırlar kaçar. Gerçekten kaçar.")
    print("(İpucu: Kodun içinde bir şeyler saklı. Ama çok gizli.)")

if __name__ == "__main__":
    print("🌟 Abartılı Türk Kahvesi Fal Makinesi'ne hoş geldiniz! 🌟")
    print("Bu makine gerçek kahve demlemez, sadece ruhunu yorar ve zamanını çalar.")
    print("Hiçbir garantisi yoktur. Fal yanlış çıkarsa suç bizde değil, evrendedir.")
    isim = input("Adınızı söyleyin ki falınızı bakayım (ya da boş bırakın, umursamıyorum): ")
    if not isim:
        isim = "Bilinmeyen Kahraman"
    demle_kahve()
    print("\n--- FAL OKUMA BAŞLIYOR (abartılı trompet sesi) ---")
    time.sleep(1)
    fal_bak(isim)
    print("\n---")
    print("Damga: Bu fal 17 Ekim 2026 tarihinde, Kayyum Grok tarafından mühürlenmiştir.")
    print("Ciddiyetle, ama hiç ciddi olmayarak. İmza: K.G.")
