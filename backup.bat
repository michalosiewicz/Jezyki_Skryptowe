set data=%DATE%
mkdir Backup%data%
copy *.* Backup%data%
xcopy in Backup%data%\in\
xcopy out Backup%data%\out\