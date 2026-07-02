@echo off
cd /d %~dp0
where node >nul 2>nul
if %errorlevel%==0 (
  node server.js
) else (
  where py >nul 2>nul
  if %errorlevel%==0 ( py server.py ) else ( python server.py )
)
pause
