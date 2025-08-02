@echo off
cd /d D:\CODIN\python\Python-notes-and-practice
git add .
git commit -m "Auto commit at %date% %time%"
git push
echo.
echo === Push complete! ===
pause