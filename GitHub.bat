@echo off
cd /d "%PROJECT_PATH%"
git init
git add .
git commit -m "Initial commit"
git remote add origin %REMOTE_URL%
git branch -M main
git push -u origin main
pause