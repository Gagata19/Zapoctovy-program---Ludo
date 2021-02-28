from tkinter import *
from random import *


class Hrac:
    def __init__(self):
        self.kocka = 0
        self.farba = None
        self.p = [0, 0, 0, 0]
        self.v_dome = 0


hp = [None] * 84

hrac1 = Hrac()
hrac2 = Hrac()
hrac3 = Hrac()
hrac4 = Hrac()

hraci = [hrac1, hrac2, hrac3, hrac4]
a = 0


def vytvor_hp():
    # globálne pole hrací plán, ktoré uchováva súradnice políčka, jeho farbu a panáčikov, ktorí sú naňom
    global hp
    a = 0
    x = 140
    y = 340
    for _ in range(4):
        hp[a] = [x, y, "white", None]
        a += 1
        x += 50
    for _ in range(5):
        hp[a] = [x, y, "white", None]
        a += 1
        y -= 50
    for _ in range(2):
        hp[a] = [x, y, "white", None]
        a += 1
        x += 50
    for _ in range(5):
        hp[a] = [x, y, "white", None]
        a += 1
        y += 50
    for _ in range(5):
        hp[a] = [x, y, "white", None]
        a += 1
        x += 50
    for _ in range(2):
        hp[a] = [x, y, "white", None]
        a += 1
        y += 50
    for _ in range(5):
        hp[a] = [x, y, "white", None]
        a += 1
        x -= 50
    for _ in range(5):
        hp[a] = [x, y, "white", None]
        a += 1
        y += 50
    for _ in range(2):
        hp[a] = [x, y, "white", None]
        a += 1
        x -= 50
    for _ in range(5):
        hp[a] = [x, y, "white", None]
        a += 1
        y -= 50
    for _ in range(5):
        hp[a] = [x, y, "white", None]
        a += 1
        x -= 50
    for _ in range(3):
        hp[a] = [x, y, "white", None]
        a += 1
        y -= 50
    x = 140
    y = 390
    for _ in range(5):
        hp[a] = [x, y, "light blue", None]
        a += 1
        x += 50
    x = 390
    y = 140
    for _ in range(5):
        hp[a] = [x, y, "yellow", None]
        a += 1
        y += 50
    x = 640
    y = 390
    for _ in range(5):
        hp[a] = [x, y, "light green", None]
        a += 1
        x -= 50
    x = 390
    y = 640
    for _ in range(5):
        hp[a] = [x, y, "red", None]
        a += 1
        y -= 50
    return hp


farby = ["light blue", "yellow", "light green", "red"]
vytvor_hp()

for g in range(4):
    dd = hp[g*12]
    dd[2] = farby[g]
    hp[g*12] = dd

# vytvorenie canvasu
master = Tk()
w = Canvas(master, width=780, height=780)
w.pack()
rozmer = 50
w.create_rectangle(0, 0, 780, 780, outline="white", fill="white")


def vytvor_dom(px, py, kx, ky, farba):
    global rozmer
    w.create_rectangle(px, py, kx, ky, fill=farba, outline="black", width="2")
    w.create_line(px+rozmer, py, kx-rozmer, ky, fill="black", width="2")
    w.create_line(px, py+rozmer, kx, ky-rozmer, fill="black", width="2")


vytvor_dom(65, 65, 165, 165, "light blue")
vytvor_dom(615, 65, 715, 165, "yellow")
vytvor_dom(65, 615, 165, 715, "red")
vytvor_dom(615, 615, 715, 715, "light green")


def domy_do_hp(z, x, y, farba):
    # pridanie východzích domov do pola hrací plán (hp)
    lk = [(0, 0), (0, 1), (1, 0), (1, 1)]
    d = z
    for i in lk:
        s = i[0]
        f = i[1]
        hp[d] = [(x + 25) + s*50, (y + 25) + f*50, farba, None]
        d += 1


domy_do_hp(68, 65, 65, "light blue")
domy_do_hp(72, 615, 65, "yellow")
domy_do_hp(76, 615, 615, "light green")
domy_do_hp(80, 65, 615, "red")

# nakreslenie hracieho plánu 
px, py, kx, ky = 65, 315, 115, 365
for _ in range(3):
    for i in range(13):
        w.create_rectangle(px, py, kx, ky, outline="black", width="2")
        px += rozmer
        kx += rozmer
    py += rozmer
    ky += rozmer
    px = 65
    kx = 115

px, py, kx, ky = 315, 65, 365, 115
for _ in range(3):
    for i in range(13):
        w.create_rectangle(px, py, kx, ky, outline="black", width="2")
        py += rozmer
        ky += rozmer
    px += rozmer
    kx += rozmer
    py = 65
    ky = 115


def vytvor_cielv(px, py, kx, ky, farba):
    global rozmer
    w.create_rectangle(px, py, kx+4*rozmer, ky, outline="black", width="2")
    for _ in range(5):
        w.create_rectangle(px, py, kx, ky, fill=farba, outline="black", width="2")
        px += rozmer
        kx += rozmer


def vytvor_cielz(px, py, kx, ky, farba):
    global rozmer
    w.create_rectangle(px, py, kx, ky+4*rozmer, outline="black", width="2")
    for _ in range(5):
        w.create_rectangle(px, py, kx, ky, fill=farba, outline="black", width="2")
        py += rozmer
        ky += rozmer


def panacik(a, por, farba, farbap="white"):
    # nakreslenie panáčika; a je kam, por je jeho číslo
    global hp
    x, y = hp[a-1][0], hp[a-1][1]
    w.create_oval(x + 8, y + 8, x - 8, y - 8, fill=farba, outline="black")
    w.create_text(x, y, text=str(por))

# vyfarbenie štartových políčok
w.create_rectangle(115, 315, 165, 365, fill="light blue", outline="black", width="2")
w.create_rectangle(615, 415, 665, 465, fill="light green", outline="black", width="2")
w.create_rectangle(415, 115, 465, 165, fill="yellow", outline="black", width="2")
w.create_rectangle(315, 615, 365, 665, fill="red", outline="black", width="2")

vytvor_cielv(115, 365, 165, 415, "light blue")
vytvor_cielv(415, 365, 465, 415, "light green")
vytvor_cielz(365, 115, 415, 165, "yellow")
vytvor_cielz(365, 415, 415, 465, "red")

# vyfarbenie stredu
w.create_rectangle(364, 364, 416, 416, fill="black", outline="black")

na_tahu = 1

# pre väčšiu pravdepodobnosť padnutia niektorých čísiel
hody = [1, 2, 3, 4, 5, 6, 1, 3, 4, 5, 6, 3, 5, 6]


def hod_kocku(event):
    # simulovanie háadzania kockou
    global na_tahu, hody, kocka, poistka
    poistka = True
    nt = na_tahu
    if kocka > 0:
        return
    x = hody[randint(0, 13)]
    kocka = x
    hraci[na_tahu-1].kocka = x
    if hraci[nt-1].p[0] > 67 and hraci[nt-1].p[1] > 67 and hraci[nt-1].p[2] > 67 and hraci[nt-1].p[3] > 67 and x != 6:
        kocka = 0
        poistka = False
    if na_tahu == 1:
        w.create_rectangle(214, 649, 281, 716, fill="white", outline="white")
        w.create_rectangle(215, 65, 280, 130, fill="white", outline="black")
        """hraci[na_tahu-1].kocka = x  """
        if x == 6:
            na_tahu += 0
        else:
            na_tahu = 2
        w.create_text(248, 97, font="Times 50 bold", text=str(x))
        return na_tahu
    elif na_tahu == 2:
        w.create_rectangle(214, 64, 281, 131, fill="white", outline="white")
        w.create_rectangle(565, 65, 500, 130, fill="white", outline="black")
        if x == 6:
            na_tahu += 0
        else:
            na_tahu = 3  
        w.create_text(532, 97, font="Times 50 bold", text=str(x))
        return na_tahu
    elif na_tahu == 3:
        w.create_rectangle(499, 64, 566, 131, fill="white", outline="white")
        w.create_rectangle(565, 650, 500, 715, fill="white", outline="black")
        if x == 6:
            na_tahu += 0
        else:
            na_tahu = 4
        w.create_text(532, 682, font="Times 50 bold", text=str(x))
        return na_tahu
    elif na_tahu == 4:
        w.create_rectangle(499, 649, 566, 716, fill="white", outline="white")
        w.create_rectangle(215, 650, 280, 715, fill="white", outline="black")
        if x == 6:
            na_tahu += 0
        else:
            na_tahu = 1
        w.create_text(248, 682, font="Times 50 bold", text=str(hrac4.kocka))
        return na_tahu


w.bind("<Button-1>", hod_kocku)
kocka = 0
poistka = True
pole_farieb = ["modrý", "žltý", "zelený", "červený"]

# definovanie konkrétnych hráčov a ich panáčikov
hrac1.farba = "light blue"
hrac1.p = [69, 70, 71, 72]
hrac2.farba = "yellow"
hrac2.p = [73, 74, 75, 76]
hrac3.farba = "light green"
hrac3.p = [77, 78, 79, 80]
hrac4.farba = "red"
hrac4.p = [81, 82, 83, 84]

for i in range(4):
    # postavenie panáčikov do východzích domov
    panacik(hrac1.p[i], i+1, hrac1.farba)
    panacik(hrac2.p[i], i+1, hrac2.farba)
    panacik(hrac3.p[i], i+1, hrac3.farba)
    panacik(hrac4.p[i], i+1, hrac4.farba)


def policko(j):
    # funkcia na prekreslenie políčka po odchode panáčika; j je poradie políčka v hracom poli
    global hp
    w.create_rectangle(hp[j-1][0] - 25, hp[j-1][1] - 25, hp[j-1][0] + 25, hp[j-1][1] + 25, fill=hp[j-1][2], outline="black", width="2")
    if hp[j-1][3]:
        h, p = hp[j-1][3][0]
        panacik(j, p, hraci[h].farba)
        if len(hp[j-1][3]) > 1:
            pocet = ""
            for i in range(len(hp[j-1][3])):
                pocet += str(hp[j-1][3][i][1]) + ","
            w.create_text(hp[j-1][0], hp[j-1][1] - 15, fill="black", text=pocet[:-1])


def postav_panacika(poradie, b, j, nt):
    # funkcia na postavenie panáčika, ktorá rozhoduje o vyhodení; j je odkial a b je kam, poradie je číslo panáčika, nt hovorí ktorý hráč je na ťahu
    global hraci, hp, kocka
    #  print(len(hp), hp[68])
    if hp[j-1][3] is None:
        pass
    elif len(hp[j-1][3]) == 1:
        hp[j-1][3] = None
    else:
        if nt == -1:
            nt = 3
        hp[j-1][3].pop(hp[j-1][3].index((nt, poradie)))
    if hp[j-1][3] == []:
        hp[j-1][3] = None
    if hp[b-1][3] is None:
        hp[b-1][3] = [(nt, poradie)]
        hraci[nt].p[poradie-1] = b
        panacik(b, poradie, hraci[nt].farba)
        policko(j)
    elif hp[b-1][3][0][0] == nt:
        policko(j)
        hp[b-1][3].append((nt, poradie))
        hraci[nt].p[poradie-1] = b
        policko(b)
        pocet = ""
        for i in range(len(hp[b-1][3])):
            pocet += str(hp[b-1][3][i][1]) + ","
        w.create_text(hp[b-1][0], hp[b-1][1] - 15, fill="black", text=pocet[:-1])
    else:
        if len(hp[b-1][3]) == 1:
            h, p = hp[b-1][3][0]
            hp[b-1][3] = [(nt, poradie)]
            hraci[nt].p[poradie-1] = b
            panacik(b, poradie, hraci[nt].farba)
        else:
            h, p = nt, poradie
        if h < 0:
            h = 3
        hraci[h].p[p-1] = 68+(h)*4+p
        hp[67+(h)*4+p][3] = [(nt, poradie)]
        panacik(68+(h)*4+p, p, hraci[h].farba)
        policko(j)
    hraci[nt].kocka = 0
    kocka = 0


def klik(poradie):
    # funkcia na posun panáčikov, prípadne stavanie z východzieho domu podľa hodu
    global kocka, poistka, pole_farieb
    if poistka == False:
        print("nemáš nič vonku")
        return
    nt = na_tahu - 1
    if hraci[nt].kocka == 0:
        pass
    if hraci[nt].kocka == 6:
        j = hraci[nt].p[poradie - 1]
        b = j
        if b > 68:
            b = 1 + 12*nt
            postav_panacika(poradie, b, j, nt)
            hraci[nt].p[poradie - 1] = b
        else:
            nt += 1
            j = hraci[nt-1].p[poradie - 1]
            if j < 48:
                b = j + hraci[nt-1].kocka
                print(nt, j, b)
                if nt == 1 and b > 47:
                    b += 1
                    hraci[nt-1].v_dome += 1
                elif nt == 2 and j < 12 and b > 11:
                    b += 42
                    hraci[nt-1].v_dome += 1
                elif nt == 3 and j < 24 and b > 23:
                    b += 35
                    hraci[nt-1].v_dome += 1
                elif (nt == 0 or nt == 4) and j < 36 and b > 35:
                    b += 28
                    hraci[nt-1].v_dome += 1
                elif b > 48:
                    b = b - 48
                postav_panacika(poradie, b, j, nt-1)
                nt -= 1
            else:
                print("iný panák")
                kocka = 0           
        nt += 1
    else:
        j = hraci[nt-1].p[poradie - 1]
        if j < 48:
            b = j + hraci[nt-1].kocka
            if nt == 1 and b > 47:
                b += 1
                hraci[nt-1].v_dome += 1
            elif nt == 2 and j < 12 and b > 11:
                b += 42
                hraci[nt-1].v_dome += 1
            elif nt == 3 and j < 24 and b > 23:
                b += 35
                hraci[nt-1].v_dome += 1
            elif (nt == 0 or nt == 4) and j < 36 and b > 35:
                b += 28
                hraci[nt-1].v_dome += 1
            elif b > 48:
                b = b - 48
            postav_panacika(poradie, b, j, nt-1)
        elif j > 48:
            b = j + hraci[nt-1].kocka
            if nt == 0:
                nt = 4
            if b <= 53 + 5*(nt-1):
                postav_panacika(poradie, b, j, nt-1)
            else:
                print("iný panák")
                kocka = 0
        else:
            print("iný panák")
            kocka = 0
    if hraci[nt-1].v_dome == 4:
        cap = pole_farieb[nt-1] + " hráč vyhral"
        w.create_rectangle(0, 300, 780, 500, fill="magenta")
        w.create_text(390, 390, font="Times 80 bold", text= cap)
        w.create_text(390, 450, text="pre ukončenie stlač Esc")

# výber hráča, ktorého panáčika posunie
master.bind("<a>", lambda key: klik(1))
master.bind("<b>", lambda key: klik(2))
master.bind("<c>", lambda key: klik(3))
master.bind("<d>", lambda key: klik(4))

master.bind("<q>", lambda key: klik(1))
master.bind("<w>", lambda key: klik(2))
master.bind("<e>", lambda key: klik(3))
master.bind("<r>", lambda key: klik(4))

master.bind("<Escape>", lambda key: exit(0))

w.mainloop()
