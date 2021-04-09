import sys

class Metro():
    def __init__(self,dane):
        self.indeks = dane[len(dane) - 5]
        try:
            wejscie = open(dane, "r")
            self.ilosc_stacji = int(wejscie.read(1))
            self.odleglosc_dworzec = []
            self.odleglosc_lotnisko = []
            self.wynik=[]
            liczba = ""
            while (len(self.odleglosc_dworzec) != self.ilosc_stacji - 2):
                znak = wejscie.read(1)
                if (znak != " " and znak != "\n"):
                    liczba += znak
                elif (len(liczba) > 0):
                    self.odleglosc_dworzec.append(int(liczba))
                    liczba = ""
            liczba = ""
            while (len(self.odleglosc_lotnisko) != self.ilosc_stacji - 2):
                znak = wejscie.read(1)
                if (znak != " " and znak != "\n" and znak != ""):
                    liczba += znak
                elif (len(liczba) > 0):
                    self.odleglosc_lotnisko.append(int(liczba))
                    liczba = ""
            wejscie.close()
        except:
            wyjscie = open("out\wyjscie" + self.indeks + ".txt", "w")
            wyjscie.write("Źle zapisany plik wejscia.")
            wyjscie.close()
            exit()

    def dodanie_do_A(self,x, y, x2, y2, A, nowa, tab):
        if (x2 - x == y2 - y and x2 > x and y2 > y):
            tab.append([])
            tab[len(tab) - 1].append(A)
            tab[len(tab) - 1].append(nowa)
            tab[len(tab) - 1].append(x2 - x)

    def dodanie_do_D(self,odl, x2, y2, nowa, tab):
        if (x2 == y2 - odl and y2 > odl):
            tab.append([])
            tab[len(tab) - 1].append(1)
            tab[len(tab) - 1].append(nowa)
            tab[len(tab) - 1].append(x2)

    def dodanie_do_L(self,odl, x2, y2, nowa, tab):
        if (y2 == x2 - odl and x2 > odl):
            tab.append([])
            tab[len(tab) - 1].append(self.ilosc_stacji)
            tab[len(tab) - 1].append(nowa)
            tab[len(tab) - 1].append(y2)

    def dodanie_do_Psr(self,x, y, x2, y2, nowa, tab, dodane, dodane_s):
        if (y2 + x2 == x + y and x < x2 and y > y2 and x2 != x and dodane.count(y2) == 0):
            odl = 0
            for x in range(len(tab)):
                odl += tab[len(tab) - x - 1][2]
                if (odl > y2):
                    tab.insert(len(tab) - x - 1, [])
                    tab[len(tab) - x - 2].append(tab[len(tab) - x - 3][1])
                    tab[len(tab) - x - 2].append(nowa)
                    tab[len(tab) - x - 2].append(self.odleglosc_lotnisko[tab[len(tab) - x - 3][1] - 2] - y2)
                    tab.insert(len(tab) - x - 1, [])
                    tab[len(tab) - x - 2].append(nowa)
                    tab[len(tab) - x - 2].append(tab[len(tab) - x - 1][1])
                    if (x == 0):
                        tab[len(tab) - x - 2].append(y2)
                    else:
                        tab[len(tab) - x - 2].append(y2 - self.odleglosc_lotnisko[tab[len(tab) - x - 1][0] - 2])
                    tab.pop(len(tab) - x - 1)
                    dodane.append(y2)
                    dodane_s.append(nowa)
                    break

    def dodanie_do_Lsr(self,x, y, x2, y2, nowa, tab, dodane, dodane_s):
        if (y2 + x2 == x + y and x > x2 and y < y2 and x2 != x and dodane.count(x2) == 0):
            odl = 0
            for x in range(len(tab)):
                odl += tab[x][2]
                if (odl > x2):
                    tab.insert(x + 1, [])
                    tab[x + 1].append(nowa)
                    tab[x + 1].append(tab[x][1])
                    tab[x + 1].append(self.odleglosc_dworzec[tab[x][1] - 2] - x2)
                    tab.insert(x + 1, [])
                    tab[x + 1].append(tab[x][0])
                    tab[x + 1].append(nowa)
                    if (x == 0):
                        tab[x + 1].append(x2)
                    else:
                        tab[x + 1].append(x2 - self.odleglosc_dworzec[tab[x][0] - 2])
                    tab.pop(x)
                    dodane.append(x2)
                    dodane_s.append(nowa)
                    break

    def poczatek_A(self,i, tab):
        tab.append([])
        tab.append([])
        tab[0].append(1)
        tab[0].append(i + 2)
        tab[0].append(self.odleglosc_dworzec[i])
        tab[1].append(i + 2)
        tab[1].append(self.ilosc_stacji)
        tab[1].append(self.odleglosc_lotnisko[i])
        return self.odleglosc_dworzec[i] + self.odleglosc_lotnisko[i]

    def poczatek_L(self,i, tab):
        tab.append([])
        tab.append([])
        tab[0].append(1)
        tab[0].append(self.ilosc_stacji)
        tab[0].append(self.odleglosc_dworzec[i] - self.odleglosc_lotnisko[i])
        tab[1].append(self.ilosc_stacji)
        tab[1].append(i + 2)
        tab[1].append(self.odleglosc_lotnisko[i])
        return self.odleglosc_dworzec[i] - self.odleglosc_lotnisko[i]

    def poczatek_D(self,i, tab):
        tab.append([])
        tab.append([])
        tab[0].append(self.ilosc_stacji)
        tab[0].append(1)
        tab[0].append(self.odleglosc_lotnisko[i] - self.odleglosc_dworzec[i])
        tab[1].append(1)
        tab[1].append(i + 2)
        tab[1].append(self.odleglosc_dworzec[i])
        return self.odleglosc_lotnisko[i] - self.odleglosc_dworzec[i]

    def algorytm(self,i, dodane, odl, tab, dodane_D, dodane_L, d_stacje_D, d_stacje_L):
        if (len(tab) == self.ilosc_stacji - 1):
            self.wyjscie(tab)
            exit()
        tab1 = []
        tab2 = []
        tab3 = []
        tab4 = []
        tab5 = []
        tablica_dodatkowa_D = []
        tablica_dodatkowa_L = []
        for x in range(len(dodane_D)):
            tablica_dodatkowa_D.append([])
            for j in range(len(tab)):
                tablica_dodatkowa_D[x].append(tab[j])
        for x in range(len(dodane_L)):
            tablica_dodatkowa_L.append([])
            for j in range(len(tab)):
                tablica_dodatkowa_L[x].append(tab[j])
        for x in range(len(tab)):
            tab1.append(tab[x])
            tab2.append(tab[x])
            tab3.append(tab[x])
            tab4.append(tab[x])
            tab5.append(tab[x])
        licznik = len(tab)
        for j in range(self.ilosc_stacji - 2):
            if (dodane.count(j) == 0):
                self.dodanie_do_A(self.odleglosc_dworzec[i], self.odleglosc_lotnisko[i],
                             self.odleglosc_dworzec[j], self.odleglosc_lotnisko[j], i + 2, j + 2, tab1)
                for x in range(len(dodane_D)):
                    self.dodanie_do_A(self.odleglosc_dworzec[d_stacje_D[x] - 2], self.odleglosc_lotnisko[d_stacje_D[x] - 2],
                                 self.odleglosc_dworzec[j], self.odleglosc_lotnisko[j], d_stacje_D[x], j + 2,
                                 tablica_dodatkowa_D[x])
                for x in range(len(dodane_L)):
                    self.dodanie_do_A(self.odleglosc_dworzec[d_stacje_L[x] - 2], self.odleglosc_lotnisko[d_stacje_L[x] - 2],
                                 self.odleglosc_dworzec[j], self.odleglosc_lotnisko[j], d_stacje_L[x], j + 2,
                                 tablica_dodatkowa_L[x])
                self.dodanie_do_D(odl, self.odleglosc_dworzec[j], self.odleglosc_lotnisko[j], j + 2, tab2)
                self.dodanie_do_L(odl, self.odleglosc_dworzec[j], self.odleglosc_lotnisko[j], j + 2, tab3)
                if (tab[0][2] == self.odleglosc_dworzec[i] or len(dodane_D) > 0 or len(dodane_L) > 0):
                    self.dodanie_do_Lsr(self.odleglosc_dworzec[i], self.odleglosc_lotnisko[i],
                                   self.odleglosc_dworzec[j], self.odleglosc_lotnisko[j], j + 2, tab4, dodane_D, d_stacje_D)
                    self.dodanie_do_Psr(self.odleglosc_dworzec[i], self.odleglosc_lotnisko[i],
                                   self.odleglosc_dworzec[j], self.odleglosc_lotnisko[j], j + 2, tab5, dodane_L, d_stacje_L)
                if (len(tab1) > licznik):
                    dodane.append(j)
                    self.algorytm(i, dodane, odl, tab1, dodane_D, dodane_L, d_stacje_D, d_stacje_L)
                    tab1.pop(len(tab1) - 1)
                    licznik = len(tab)
                if (len(tab2) > licznik):
                    dodane.append(j)
                    self.algorytm(i, dodane, odl, tab2, dodane_D, dodane_L, d_stacje_D, d_stacje_L)
                    tab2.pop(len(tab2) - 1)
                    licznik = len(tab)
                if (len(tab3) > licznik):
                    dodane.append(j)
                    self.algorytm(i, dodane, odl, tab3, dodane_D, dodane_L, d_stacje_D, d_stacje_L)
                    tab3.pop(len(tab3) - 1)
                    licznik = len(tab)
                if (len(tab4) > licznik):
                    dodane.append(j)
                    self.algorytm(i, dodane, odl, tab4, dodane_D, dodane_L, d_stacje_D, d_stacje_L)
                    tab4.pop(len(tab4) - 1)
                    dodane_D.pop(len(dodane_D) - 1)
                    d_stacje_D.pop(len(d_stacje_D) - 1)
                    licznik = len(tab)
                if (len(tab5) > licznik):
                    dodane.append(j)
                    self.algorytm(i, dodane, odl, tab5, dodane_D, dodane_L, d_stacje_D, d_stacje_L)
                    tab5.pop(len(tab5) - 1)
                    dodane_L.pop(len(dodane_L) - 1)
                    d_stacje_L.pop(len(d_stacje_L) - 1)
                    licznik = len(tab)
                for x in range(len(dodane_D)):
                    if (len(tablica_dodatkowa_D[x]) > licznik):
                        dodane.append(j)
                        self.algorytm(i, dodane, odl, tablica_dodatkowa_D[x], dodane_D, dodane_L, d_stacje_D, d_stacje_L)
                        tablica_dodatkowa_D[x].pop(len(tablica_dodatkowa_D[x]) - 1)
                        licznik = len(tab)
                for x in range(len(dodane_L)):
                    if (len(tablica_dodatkowa_L[x]) > licznik):
                        dodane.append(j)
                        self.algorytm(i, dodane, odl, tablica_dodatkowa_L[x], dodane_D, dodane_L, d_stacje_D, d_stacje_L)
                        tablica_dodatkowa_L[x].pop(len(tablica_dodatkowa_L[x]) - 1)
                        licznik = len(tab)

    def plan(self):
        dodane_stacje = []
        wynik1 = []
        wynik2 = []
        dodane_D = []
        dodane_L = []
        dodane_stacje_D = []
        dodane_stacje_L = []
        for i in range(self.ilosc_stacji - 2):
            dodane_stacje.append(i)
            odleglosc_DL = self.poczatek_A(i, wynik1)
            self.algorytm(i, dodane_stacje, odleglosc_DL, wynik1, dodane_D, dodane_L, dodane_stacje_D, dodane_stacje_L)
            if (self.odleglosc_lotnisko[i] > self.odleglosc_dworzec[i]):
                odleglosc_DL = self.poczatek_D(i, wynik2)
                self.algorytm(i, dodane_stacje, odleglosc_DL, wynik2, dodane_D, dodane_L, dodane_stacje_D, dodane_stacje_L)
            else:
                odleglosc_DL = self.poczatek_L(i, wynik2)
                self.algorytm(i, dodane_stacje, odleglosc_DL, wynik2, dodane_D, dodane_L, dodane_stacje_D, dodane_stacje_L)
            wynik1.clear()
            wynik2.clear()
            dodane_stacje.clear()
        wyjscie = open("out\wyjscie"+self.indeks+".txt", "w")
        wyjscie.write("NIE")
        wyjscie.close()

    def wyjscie(self,wynik):
        wyjscie=open("out\wyjscie"+self.indeks+".txt","w")
        wyjscie.write("TAK\n")
        for i in range(len(wynik)):
            for j in range(len(wynik[i])):
                wyjscie.write(str(wynik[i][j]))
                if(j!=len(wynik[i])-1):
                    wyjscie.write(" ")
            if(i!=len(wynik)-1):
                wyjscie.write("\n")
        wyjscie.close()

if(len(sys.argv)==2):
    M=Metro(sys.argv[1])
    M.plan()
else:
    print("Błędne argumenty wejścia.")