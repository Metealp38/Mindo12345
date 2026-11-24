import random

# Yapay Zekanın Hafızası ve Öğrenme Motoru
class KendiYapayZekam:
    def __init__(self):
        self.hafiza = {}

    def ogren(self, metin):
        kelimeler = metin.lower().split()
        for i in range(len(kelimeler) - 1):
            su_anki = kelimeler[i]
            sonraki = kelimeler[i + 1]
            if su_anki not in self.hafiza:
                self.hafiza[su_anki] = []
            self.hafiza[su_anki].append(sonraki)

    def cevap_ver(self, soru):
        kelimeler = soru.lower().split()
        baslangic = random.choice(kelimeler) if kelimeler else ""
        if baslangic not in self.hafiza:
            if not self.hafiza:
                return "Henüz hiçbir şey bilmiyorum, bana bir şeyler öğret!"
            baslangic = random.choice(list(self.hafiza.keys()))
        
        cumle = [baslangic]
        for _ in range(10):
            son_kelime = cumle[-1]
            if son_kelime in self.hafiza:
                cumle.append(random.choice(self.hafiza[son_kelime]))
            else:
                break
        return " ".join(cumle).capitalize()

bot = KendiYapayZekam()

# Başlangıç Eğitimi
baslangic_bilgisi = """
merhaba ben syal bot senin kişisel yapay zekanım
yapay zeka geleceğin en güçlü teknolojisidir
seninle sohbet etmeyi ve yeni şeyler öğrenmeyi çok seviyorum
bana ne öğretirsen onu aklımda tutarım ve seninle konuşurum
"""
bot.ogren(baslangic_bilgisi)

print("=== SYAL-BOT AKTİF (Şifresiz & Bağımsız Yapay Zeka) ===")
print("Komutlar: 'öğret: [cümle]' yazarak yeni bilgi öğret, 'çıkış' yazarak kapat.\n")

while True:
    girdi = input("Sen: ")
    if girdi.lower() == "çıkış":
        break
    elif girdi.lower().startswith("öğret:"):
        yeni_bilgi = girdi[6:].strip()
        bot.ogren(yeni_bilgi)
        print("SYAL-BOT: Harika! Bu bilgiyi sinir ağıma kaydettim.\n")
    else:
        print("SYAL-BOT:", bot.cevap_ver(girdi), "\n")
