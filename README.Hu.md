# megoldási terv
0. Projektállomány:
    - Projektek2023/BrightnessControlWithButton/BrightnessControlWithButton.py

1. A számláló program elkészítése
    - a bal nyomógomb: felfelé számol 100-ig 10-es lépésekben
    - a jobb nyomógomb: lefelé számol 0-ig 10-es lépésekben
    - a határokon megáll
    - minden gombnyomást kiír a képernyőre

2. A led PWM üzemmódba kapcsolása, fényerő szabályzás kipróbálása
    - Frekvrencia beállítása: 50Hz
    - Kitöltési tényező változtatása
    
3. A led a nyomógombok hatására működjön

# 1. A számláló program elkészítése
A megvalósítás:
```py
Első sorban a számlálót készítettük el és arra tudtuk írni a fényerő szabályzást.
Meg hívtuk a pinSwitchUp és a pinSwitchDown "gombunkat"amik majd 10 esével fogják számolni a gombnyomást.

def countUp(channel):
ebbe a függvénybe írtuk azt bele amivel a omb felfelé fog számolni (+10) minden gombnyomás

def countDown(channel):
ugyan az a függvény felépítése annyi a kivétel hogy itt (-10)-el dolgozunk hogy, ez a gomb minden gombnyomáskor -10 et vegyen el.

Mind két függvény végén ez a kif. szerepel
p.ChangeDutyCycle(fill)
Annyit jelent,hogy 0-100-ig fogja ez csak engedni a számlálást 100 tól felfelé nem megy és 0 alá sem fog menni akárhányszor is meg nyomnánk a gombot.

Ezután már a frekvrenciát(Hz) függvényt készítettük.
GPIO.setup
bemenetként vagy kimenetként, vagy mindkettőként használható, és szoftverrel vezérelhető. A GPIO-knak nincs előre meghatározott célja, és alapértelmezés szerint nincs használva csak akkor írják valamihez ha már van hozzán függvényünk.

Már csak be kérjük a Hz-t 
Meg a vílágítási erejét lehet(de nálunk most nulla marad hisz mi nyomógombbal szabályozzuk a fényerejét!)

ki printeljük a szöveget a végén ami majd ki irja hogy 
mekkora a frekvrenciája amin világít a Led és azt,hogy hány százalékosan vílágít.

a végére be szúrjuk az eseménykezelőt 2x hisz két db gombunk van egy Fel és egy Le nevű.

le zárjuk ctrl cvel az egészet ami majd ki írja,hogy pinek le kapcsolva.
```
