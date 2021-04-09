import os
import datetime

lista_plikow_in=list(os.listdir("in"))
lista_plikow_out=list(os.listdir("out"))
data=datetime.datetime.now()

html="<html>\n<head>\n<title>Raport projektu</title>\n<style>\n#ekran\n{\nwidth: 500px;\nmargin-left:auto;\n"
html+="margin-right:auto;\n}\n#wstep\n{\npadding: 10px;\n}\n#wejscie\n{\nfloat: left;\nwidth: 230px;\n"
html+="padding: 10px;\n}\n#wyjscie\n{\nfloat: left;\nwidth: 230px;\npadding: 10px;\n}\n</style>\n</head>\n"
html+='<body>\n<div id="ekran">\n<div id="wstep">\n<h1>Raport projektu Plan Metra</h1>\n'
html+='Liczba plików wejścia: '+str(len(lista_plikow_in))+'<br /><br />\nData wykonania raportu: '+str(data)+'\n'
html+='<br /><br />\nAutor: Michał Osiewicz\n</div>\n<div id="wejscie">\n<h2>Wejścia:</h2>\n'
html_in=""
html_out=""
for i in range(len(lista_plikow_in)):
    html_in+="<h3>"+lista_plikow_in[i]+"</h3>\n"
    html_out+="<h3>"+lista_plikow_out[i]+"</h3>\n"
    plik_in=open("in/"+lista_plikow_in[i],"r")
    plik_out=open("out/"+lista_plikow_out[i],"r")
    linie_in=plik_in.readlines()
    linie_out=plik_out.readlines()
    plik_in.close()
    plik_out.close()
    x=0
    while(x<len(linie_in) or x<len(linie_out)):
        if(x<len(linie_in)):
            html_in+=linie_in[x]
        if (x < len(linie_out)):
            html_out+=linie_out[x]
        html_in+="<br />\n"
        html_out+="<br />\n"
        x+=1
html+=html_in+'</div>\n<div id="wyjscie">\n<h2>Wyjścia:</h2>\n'+html_out+'</div>\n</div>\n</body>\n</html>'

strona=open("raport.html","w")
strona.write(html)
