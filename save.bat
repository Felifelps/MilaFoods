@echo off
title Saving
git init
git add .
:: set /p "commit=Enter commit: "
git commit -m %1
::"%commit%"
git push https://github.com/Felifelps/MilaFoods async
echo Saved
pause


