@echo off
color a
:main
echo Please Enter Domain name / URL
set /p option=
:findip
tracert %option%
