import pgzrun
import time
from pgzhelper import *

WIDTH = 800 # Pencere Genişliği
HEIGHT = 500 # Pencere Yüksekliği

TITLE = "KORSAN AVI" # Oyun Adı
FPS = 30 # Saniyedeki Kare Sayısı
hiz = 0.1
hiz2 = 1
seviye = 1
seviye2 = 1
mod = "menü"
puan = 0
bombalar = []
can = 3
ses = True
dusman_sayisi = 4
new_image = "dusman1"
alinabilecek12 = False
alinabilecek22 = False
alinabilecek32 = False
alinabilecek42 = False
zorluk2 = False
super_patlama = False
dusman1_can = 3
dusman2_can = 3
dusman4_can = 3

benim_gemim = Actor("normal_gemi", (400, 340))
alinabilecek1= Actor("dusman1",(100,150))
alinabilecek2= Actor("dusman3",(300,250))
alinabilecek3= Actor("tas1",(500,150))
alinabilecek4= Actor("tas2",(700,250))
alinabilecek11= Actor("dusman1",(100,100))
alinabilecek111= Actor("dusman1",(700,350))
alinabilecek222= Actor("tas2",(100,350))
alinabilecek333= Actor("dusman4",(380,250))
alinabilecek26= Actor("dusman3",(300,100))
alinabilecek33= Actor("tas1",(500,100))
alinabilecek44= Actor("tas2",(700,100))
a_gemi = Actor("normal_gemi", (380, 420))
b_gemi = Actor("tas1", (380, 240))
arkaplan = Actor("adsiz3")
kaybettiniz = Actor("adsiz4")
menu = Actor("adsiz5")
kazandiniz = Actor("adsiz6")
dusman1 = Actor("dusman1", (100,-175))
dusman2 = Actor("dusman4", (300,-700))
dusman3 = Actor("dusman3", (500,-550))
dusman4 = Actor("dusman1", (700,-920))
oyna = Actor("bonus", (170, 250))
oyna2 = Actor("bonus", (400, 300))
dukkan = Actor("bonus", (170,400))
koleksiyon = Actor("bonus", (570,400))
geri_don = Actor("bonus", (400, 350))
bilgi = Actor("bonus", (570, 250))
mermi_topu = Actor("mermi_topu", (400, 290))
bomba2 = Actor("bomba")
hakkinda = Actor("adsiz7")
bomba2.pos = a_gemi.pos
carpi = Actor("carpi",(770,30))
ayar_arkaplan = Actor("adsiz3")
ayarlar = Actor("ayarlar", (750,50))
sesli = Actor("bonus", (170,250))
sessiz = Actor("bonus", (570, 250))
sifirla = Actor("bonus", (370,400))

def draw():
    global seviye, mod, puan, zorluk2, sesli, sessiz, sifirla, ses, seviye2

    if mod == "oyun":
        arkaplan.draw()
        benim_gemim.draw()
        dusman1.draw()
        dusman2.draw()
        dusman3.draw()
        dusman4.draw()
        mermi_topu.draw()
        # Füzelerin çizilmesi   
        for i in range(len(bombalar)):
            bombalar[i].draw()
        carpi.draw()
    
    if mod == "kaybettin":
        kaybettiniz.draw()
        geri_don.draw()
        carpi.draw()
        screen.draw.text("GERİ DÖN!", center= (400, 350), color="black", fontsize = 40)
        screen.draw.text(str(puan) + "\n", center=(370, 295), color = 'black', fontsize = 60)
        
        
    if mod == "kazandiniz":
        kazandiniz.draw()
        oyna2.draw()
        carpi.draw()
        screen.draw.text("DEVAM ET!", center= (400, 300), color="black", fontsize = 40)
        screen.draw.text(str(seviye) + "\n", center=(520, 80), color = 'black', fontsize = 70)
        screen.draw.text(str(seviye2) + "\n", center=(440, 250), color = 'black', fontsize = 85)
        
    if mod == "menü":
        menu.draw()
        oyna.draw()
        bilgi.draw()
        dukkan.draw()
        koleksiyon.draw()
        a_gemi.draw()
        b_gemi.draw()
        bomba2.draw()
        screen.draw.text("OYNA", center= (170, 250), color="black", fontsize = 30)
        screen.draw.text("HAKKINDA", center= (570, 250), color="black", fontsize = 30)
        screen.draw.text("DÜKKAN", center= (170, 400), color="black", fontsize = 30)
        screen.draw.text("KOLEKSİYON", center= (570, 400), color="black", fontsize = 30)
        screen.draw.text("Puan:", center= (50, 16), color="black", fontsize = 37)
        screen.draw.text(str(puan) + "\n", center=(120, 30), color = 'black', fontsize = 37)
        screen.draw.text("Seviye:", center= (60, 50), color="black", fontsize = 37)
        screen.draw.text(str(seviye) + "\n", center=(120, 65), color = 'black', fontsize = 37)
        screen.draw.text("Can:", center= (41, 80), color="black", fontsize = 37)
        screen.draw.text(str(can) + "\n", center=(90, 95), color = 'black', fontsize = 37)
        ayarlar.draw()
        

    if mod == "hakkinda":
        hakkinda.draw()
        carpi.draw()

    if mod == "dükkan":
        arkaplan.draw()
        carpi.draw()
        alinabilecek1.draw()
        alinabilecek2.draw()
        alinabilecek3.draw()
        alinabilecek4.draw()
        screen.draw.text("Ücret : 50 Puan", center=(100, 250), color="black", fontsize = 30)
        screen.draw.text("Ücret : 100 Puan", center=(300, 350), color="black", fontsize = 30)
        screen.draw.text("Ücret : 150 Puan", center=(500, 250), color="black", fontsize = 30)
        screen.draw.text("Ücret : 200 Puan", center=(700, 350), color="black", fontsize = 30)


    if mod == "koleksiyon":
        arkaplan.draw()
        carpi.draw()
        if alinabilecek12 == True:
            alinabilecek1.draw()
            screen.draw.text("Aldın!", center=(100, 250), color="black", fontsize = 30)
        if alinabilecek22 == True:
            alinabilecek2.draw()
            screen.draw.text("Aldın", center=(300, 350), color="black", fontsize = 30)
        if alinabilecek32 == True:
            alinabilecek3.draw()
            screen.draw.text("Aldın!", center=(500, 250), color="black", fontsize = 30)
        if alinabilecek42 == True:
            alinabilecek4.draw()
            screen.draw.text("Aldın!", center=(700, 350), color="black", fontsize = 30)

    if mod == "ayarlar":
        ayar_arkaplan.draw()
        sesli.draw()
        sessiz.draw()
        sifirla.draw()
        carpi.draw()
        screen.draw.text("SESLİ OYNA", center= (170, 250), color="black", fontsize = 30)
        screen.draw.text("SESSİZ OYNA", center= (570, 250), color="black", fontsize = 30)
        screen.draw.text("SIFIRLA", center= (370, 400), color="black", fontsize = 30)
        alinabilecek11.draw()
        alinabilecek26.draw()
        alinabilecek33.draw()
        alinabilecek44.draw()
        alinabilecek111.draw()
        alinabilecek222.draw()
        alinabilecek333.draw()

        


def carpismalar():
    global mod, puan, seviye, seviye2, zorluk2, dusman_sayisi, can, new_image, dusman1_can, dusman2_can, dusman4_can, sesli, sessiz, ses, sifirla

    for j in range(len(bombalar)):
        if seviye <= 9:
            if bombalar[j].colliderect(dusman1):
                if ses == True:
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman1.x = 100000
                puan = puan + 1
                dusman_sayisi -=1
                break
            if bombalar[j].colliderect(dusman2):
                if ses == True:
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman2.x = 100000
                puan = puan + 1
                dusman_sayisi -=1
                break
            
            if bombalar[j].colliderect(dusman3):
                if ses == True:
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman3.x = 100000
                puan = puan + 1
                dusman_sayisi -=1
                break

            if bombalar[j].colliderect(dusman4):
                if ses == True:
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman4.x = 100000
                puan = puan + 1
                dusman_sayisi -=1
                break

        if seviye >= 10:
            if bombalar[j].colliderect(dusman1):
                if ses == True:
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman1_can -= 1
                if dusman1_can == 0:
                    dusman1.x = 100000
                    puan = puan + 100
                    dusman_sayisi -=1
                break
            if bombalar[j].colliderect(dusman2):
                if ses == True:
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman2_can -= 1
                if dusman2_can == 0:
                    dusman2.x = 100000
                    puan = puan + 100
                    dusman_sayisi -=1
                break

            if bombalar[j].colliderect(dusman3):
                if ses == True:
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman3.x = 100000
                puan = puan + 1
                dusman_sayisi -=1
                break

            if bombalar[j].colliderect(dusman4):
                if ses == True:
                    sounds.patlama2.play()
                bombalar.pop(j)
                dusman4_can -= 1
                if dusman4_can == 0:
                    dusman4.x = 100000
                    puan = puan + 100
                    dusman_sayisi -=1
                break


def update(dt):
    global mod, puan, seviye, seviye2, zorluk2, dusman_sayisi, can, new_image, dusman1_can, dusman2_can, dusman4_can, sesli, sessiz, ses, sifirla
    carpismalar()
    if mod == "menü":
        bomba2.y -= 10
    if keyboard.left and benim_gemim.x > 40:
        benim_gemim.x -= 20
        mermi_topu.x -= 20
    if keyboard.right and benim_gemim.x < 760:
        benim_gemim.x += 20
        mermi_topu.x += 20
    for i in range(len(bombalar)):
            if bombalar[i].y < 0:
                bombalar.pop(i)
                break
            else:
                bombalar[i].y = bombalar[i].y - 10
    time.sleep(hiz)
    if mod == "oyun":
        dusman1.y = dusman1.y + 10 - hiz
        dusman2.y = dusman2.y + 10 - hiz
        dusman3.y = dusman3.y + 10 - hiz
        dusman4.y = dusman4.y + 10 - hiz

        if dusman1.y >= 500:
            dusman1.y = HEIGHT - 550
            
        if dusman2.y >= 500:
            dusman2.y = HEIGHT - 550
            
        if dusman3.y >= 500:
            dusman3.y = HEIGHT - 530
            
        if dusman4.y >= 500:
            dusman4.y = HEIGHT - 530

        if dusman_sayisi == 0:
            mod = "kazandiniz"
            seviye2 += 1

        if seviye <= 9:
            if benim_gemim.colliderect(dusman1):
                if ses == True:
                    sounds.patlama2.play()
                dusman1.x = 100000
                can -= 1
                dusman_sayisi -= 1
                puan += 1

            elif benim_gemim.colliderect(dusman2):
                if ses == True:
                    sounds.patlama2.play()
                dusman2.x = 100000
                can -= 1
                dusman_sayisi -= 1
                puan += 1

            elif benim_gemim.colliderect(dusman3):
                if ses == True:
                    sounds.patlama2.play()
                dusman3.x = 100000
                can -= 1
                dusman_sayisi -= 1
                puan += 1

            elif benim_gemim.colliderect(dusman4):
                if ses == True:
                    sounds.patlama2.play()
                dusman4.x = 100000
                can -= 1
                dusman_sayisi -= 1
                puan += 1

            if can == 0:
                mod = "kaybettin"

        if seviye >= 10:
            if benim_gemim.colliderect(dusman1):
                if ses == True:
                    sounds.patlama2.play()
                dusman1_can -= 1
                if dusman1_can == 0:
                    dusman1.x = 100000
                    dusman_sayisi -= 1
                    puan += 1
                can -= 1

            elif benim_gemim.colliderect(dusman2):
                if ses == True:
                    sounds.patlama2.play()
                dusman2_can -= 1
                if dusman2_can == 0:
                    dusman2.x = 100000
                    can -= 1
                    dusman_sayisi -= 1
                    puan += 1
                can -= 1

            elif benim_gemim.colliderect(dusman3):
                if ses == True:
                    sounds.patlama2.play()
                dusman3.x = 100000
                can -= 1
                dusman_sayisi -= 1
                puan += 1

            elif benim_gemim.colliderect(dusman4):
                if ses == True:
                    sounds.patlama2.play()
                dusman4_can -= 1
                if dusman4_can == 0:
                    dusman4.x = 100000
                    dusman_sayisi -= 1
                    puan += 1
                can -= 1
                

            if can == 0:
                mod = "kaybettin"

    if mod == "menü":
        if bomba2.colliderect(b_gemi):
            if ses == True:
                sounds.patlama2.play()
            b_gemi.image = "patlama"
            if bomba2.y == 270:
                time.sleep(0.5)
                b_gemi.image = "tas1"
                bomba2.y = 420

    if mod == "oyun" and seviye >= 10:
        zorluk2 = True

    if mod == "oyun" and zorluk2 == True:
        dusman1.image = "tas1"
        dusman2.image = "tas2"
        dusman4.image = "tas4"
        dusman1.y = dusman1.y + 10
        dusman2.y = dusman2.y + 10
        dusman4.y = dusman4.y + 10

    if seviye >= 20:
        dusman1.y = dusman1.y + 20
        dusman2.y = dusman2.y + 20
        dusman4.y = dusman4.y + 20
        
        

def on_mouse_down(button, pos):
    global mod, puan, seviye, dusman_sayisi, can, new_image, dusman1_can, dusman2_can, dusman4_can, sesli, sessiz, ses, sifirla, hiz
    global alinabilecek12, alinabilecek22, alinabilecek32, alinabilecek42

    if mod == 'oyun' and button == mouse.LEFT:
        bomba = Actor("bomba")
        bomba.pos = mermi_topu.pos
        bombalar.append(bomba)

    if mod == "menü" and oyna.collidepoint(pos):
        mod = "oyun"

    if mod == "menü" and bilgi.collidepoint(pos):
        mod = "hakkinda"

    if mod == "oyun" and carpi.collidepoint(pos):
        mod = "menü"

    if mod == "hakkinda" and carpi.collidepoint(pos):
        mod = "menü"

    if mod == "menü" and dukkan.collidepoint(pos):
        mod = "dükkan"

    if mod == "dükkan" and carpi.collidepoint(pos):
        mod = "menü"

    if mod == "menü" and koleksiyon.collidepoint(pos):
        mod = "koleksiyon"

    if mod == "kazandiniz" and carpi.collidepoint(pos):
        mod = "menü"

    
    if mod == "kaybettin" and carpi.collidepoint(pos):
        mod = "menü"

    if mod == "koleksiyon" and carpi.collidepoint(pos):
        mod = "menü"

    if mod == "dükkan" and alinabilecek1.collidepoint(pos):
        if puan >= 50:
            benim_gemim.image = "kullan1"
            alinabilecek12 = True
            puan -= 50
            alinabilecek1.y = 130
            animate(alinabilecek1, tween='bounce_end', duration=0.5, y=150)

    if mod == "dükkan" and alinabilecek2.collidepoint(pos):
        if puan >= 100:
            benim_gemim.image = "kullan2"
            alinabilecek22 = True
            puan -= 100
            alinabilecek2.y = 230
            animate(alinabilecek2, tween='bounce_end', duration=0.5, y=250)

    if mod == "dükkan" and alinabilecek3.collidepoint(pos):
        if puan >= 150:
            benim_gemim.image = "kullan3"
            alinabilecek32 = True
            puan -= 150
            alinabilecek3.y = 130
            animate(alinabilecek3, tween='bounce_end', duration=0.5, y=150)

    if mod == "dükkan" and alinabilecek4.collidepoint(pos):
        if puan >= 200:
            benim_gemim.image = "kullan4"
            alinabilecek42 = True
            puan -= 200
            alinabilecek4.y = 230
            animate(alinabilecek4, tween='bounce_end', duration=0.5, y=250)


    if mod == "kazandiniz" and oyna2.collidepoint(pos):
        mod = "oyun"
        if mod == "oyun" and seviye <= 9:
            benim_gemim.x = 400
            mermi_topu.x = 400
            seviye += 1
            dusman_sayisi = 4
            can = 3
            dusman1.y = HEIGHT - 175
            dusman1.x = 100
            dusman2.y = HEIGHT - 700
            dusman2.x = 300
            dusman3.y = HEIGHT - 550
            dusman3.x = 500
            dusman4.y = HEIGHT - 920
            dusman4.x = 700

        if mod == "oyun" and seviye >= 10:
            benim_gemim.x = 400
            mermi_topu.x = 400
            seviye += 1
            dusman_sayisi = 4
            can = 3
            dusman1_can = 3
            dusman2_can = 3
            dusman4_can = 3
            dusman1.y = HEIGHT - 175
            dusman1.x = 100
            dusman2.y = HEIGHT - 700
            dusman2.x = 300
            dusman3.y = HEIGHT - 550
            dusman3.x = 500
            dusman4.y = HEIGHT - 920
            dusman4.x = 700

    if mod == "kaybettin" and geri_don.collidepoint(pos):
        mod = "oyun"
        if mod == "oyun" and seviye <= 9:
            benim_gemim.x = 400
            mermi_topu.x = 400
            seviye += 1
            dusman_sayisi = 4
            can = 3
            dusman1_can = 3
            dusman2_can = 3
            dusman4_can = 3
            dusman1.y = HEIGHT - 175
            dusman1.x = 100
            dusman2.y = HEIGHT - 700
            dusman2.x = 300
            dusman3.y = HEIGHT - 550
            dusman3.x = 500
            dusman4.y = HEIGHT - 920
            dusman4.x = 700

        if mod == "oyun" and seviye >= 10:
            benim_gemim.x = 400
            mermi_topu.x = 400
            seviye += 1
            dusman_sayisi = 4
            can = 3
            dusman1_can = 3
            dusman2_can = 3
            dusman4_can = 3
            dusman1.y = HEIGHT - 175
            dusman1.x = 100
            dusman2.y = HEIGHT - 700
            dusman2.x = 300
            dusman3.y = HEIGHT - 550
            dusman3.x = 500
            dusman4.y = HEIGHT - 920
            dusman4.x = 700

    if mod == "koleksiyon" and alinabilecek1.collidepoint(pos):
        benim_gemim.image = "kullan1"
        alinabilecek12 = True
        alinabilecek1.y = 130
        animate(alinabilecek1, tween='bounce_end', duration=0.5, y=150)

    if mod == "koleksiyon" and alinabilecek2.collidepoint(pos):
        benim_gemim.image = "kullan2"
        alinabilecek22 = True
        alinabilecek2.y = 230
        animate(alinabilecek2, tween='bounce_end', duration=0.5, y=250)

    if mod == "koleksiyon" and alinabilecek3.collidepoint(pos):
        benim_gemim.image = "kullan3"
        alinabilecek32 = True
        alinabilecek3.y = 130
        animate(alinabilecek3, tween='bounce_end', duration=0.5, y=150)

    if mod == "koleksiyon" and alinabilecek4.collidepoint(pos):
        benim_gemim.image = "kullan4"
        alinabilecek42 = True
        alinabilecek4.y = 230
        animate(alinabilecek4, tween='bounce_end', duration=0.5, y=250)

    if mod == "ayarlar" and sesli.collidepoint(pos):
        ses = True
        sesli.y = 230
        animate(sesli, tween='bounce_end', duration=0.5, y=250)

    if mod == "ayarlar" and sessiz.collidepoint(pos):
        ses = False
        sessiz.y = 230
        animate(sessiz, tween='bounce_end', duration=0.5, y=250)

    if mod == "ayarlar" and sifirla.collidepoint(pos):
        mod = "menü"
        benim_gemim.x = 400
        mermi_topu.x = 400
        puan = 0
        seviye = 1
        dusman_sayisi = 4
        can = 3
        benim_gemim.image = "normal_gemi"
        dusman1_can = 3
        dusman2_can = 3
        dusman4_can = 3
        dusman1.y = HEIGHT - 175
        dusman1.x = 100
        dusman2.y = HEIGHT - 700
        dusman2.x = 300
        dusman3.y = HEIGHT - 550
        dusman3.x = 500
        dusman4.y = HEIGHT - 920
        dusman4.x = 700
        sifirla.y = 370
        alinabilecek12 = False
        alinabilecek22 = False
        alinabilecek32 = False
        alinabilecek42 = False
        animate(sifirla, tween='bounce_end', duration=0.5, y=400)

    if mod == "menü" and ayarlar.collidepoint(pos):
        mod = "ayarlar"

    if mod == "ayarlar" and carpi.collidepoint(pos):
        mod = "menü"

pgzrun.go()