@ echo off
:MENU
echo -----------MENU-----------
echo 1. Uruchom projekt
echo 2. Informacje o projekcie
echo 3. Backup
echo 4. Wyjscie

set /p wybor=Wybierz opcje:

if %wybor%==1 (
goto START
)
if %wybor%==2 (
goto INFO
)
if %wybor%==3 (
goto BACK
)
if %wybor%==4 (
goto WY
) else (
echo Niepoprawna wartosc.
pause
cls
goto MENU
)
:START
for %%X in (in\wejscie*.txt) do (call program.py %%X)
call raport.py
pause
cls
goto MENU
:INFO
echo Projekt Plan Metra. Autor: Michal Osiewicz
pause
cls
goto MENU
:BACK
call backup.bat
pause
cls
goto MENU
:WY
exit