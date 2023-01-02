<h1 align="center"><b>Generar codis QR amb Python</b></h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank">
    <img alt="License: GPL--3+" src="https://img.shields.io/badge/License-GPL--3+-yellow.svg" />
  </a>
  <a href="https://twitter.com/miquelnebot" target="_blank">
    <img alt="Twitter: Miquel Nebot" src="https://img.shields.io/twitter/follow/miquelnebot.svg?style=social" />
  </a>
</p>
<div align="center"><img src="https://user-images.githubusercontent.com/57944755/210243959-bbdd9846-177d-4207-a481-7ac2510306f9.png"></div>


# 👁️‍🗨️ Introducció
Un dels elements més utilitzats per poder facilitar l'accés a pàgines web o recursos són els codis QR. Mitjançant aquest senzill projecte generat amb Python veuràs com és ben senzill.

# 💻 Escenari
Kubuntu 22.04

# 0️⃣ Abans de començar
1. Haurem de tenir instal·lat Python en el nostre ordinador. Verificarem si disposam d'ell i la seva versió mitjançant la comanda següent a dins el Terminal (Ctrl+Alt+T): 

```console
user@kubuntu-mnebot:~$ python3 -V
```
Si no el tenim instal·lat, el podem aconseguir fàcilment mitjançant la comanda:
```console
user@kubuntu-mnebot:~$ sudo apt install python3
```
2. Per a la importació del mòduls necessaris (**qrcode** i **time**) és imprescindible disposar al nostre ordinador de l'administrador de paquets **PIP**, per això, i si no ho hem fet amb anterioritat, l'instal·larem a través de la terminal de la següent maner
```console
user@kubuntu-mnebot:~$ sudo apt install python3-pip
```
3. Instal·larem finalment els mòduls necessaris responsables de generar el codi QR sol·licitat:
```console
user@kubunu-mnebot:~$ sudo pip install qrcode && sudo pip install time
```

# 👇 Descàrrega i execució
Copiarem el codi següent 👇 a un arxiu amb extensió **.py** al nostre ordinador (per exemple **generar_qr_python.py**) per a la seva posterior execució: 
<p></p>📝 Descàrrega de l'arxiu .py des d'<a href="https://github.com/miquelnebotaragon/generar_qr_python/blob/main/generar_qr_python.py" target="_blank">aquí</a>.

# ➕ Informació
1️⃣ L'arxiu **.py** ha estat comentat al detall (#) per tal de possibilitar l'anàlisi del seu funcionament.<p></p>
2️⃣ Aquesta aplicació ha estat creada únicament amb finalitat d'estudi i divulgació. No em faig responsable dels possibles problemes ni prejudicis que pugui provocar el seu ús.<p></p>
