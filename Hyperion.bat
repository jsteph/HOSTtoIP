@echo off
color a
:main
echo Hyperion: Please Enter Domain name / URL
set /p option=
:findip
tracert %option%
