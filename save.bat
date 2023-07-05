@echo off
title Saving
git init
git add .
git commit -m %1
git push https://github.com/Felifelps/MilaFoods async
echo Saved
pause


