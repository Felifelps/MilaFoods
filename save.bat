@echo off
title Saving
git init
git add .
set /p "commit=Enter commit: "
git commit -m "%commit%"
git push https://github.com/Felifelps/LabSoft main
echo Saved
pause