@echo off
title Saving
git init
git add .

call :asking

:checking
if %branch%==1 call :saving_main
if %branch%==2 call :saving_async
echo Branch inválido!
pause
cls
call: asking
EXIT /B 0

:asking
set /p "commit=Enter commit: "
echo 1.main
echo 2.async
set /p "branch=Enter branch: "
call :checking
EXIT /B 0

:saving_main
git commit -m "%commit%"
git push https://github.com/Felifelps/MilaFoods main
echo Saved
pause
exit
EXIT /B 0

:saving_async
git commit -m "%commit%"
git push https://github.com/Felifelps/MilaFoods async
echo Saved
pause
exit
EXIT /B 0
