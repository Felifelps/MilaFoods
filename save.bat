@echo off
title Saving
git init
git add .

call :asking

:checking
if %branch%==1 call :saving main
if %branch%==2 call :saving async
echo Invalid answer!
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

:saving
git commit -m "%commit%"
git push https://github.com/Felifelps/MilaFoods %~1
echo %~1
echo Saved
pause
exit
EXIT /B 0

