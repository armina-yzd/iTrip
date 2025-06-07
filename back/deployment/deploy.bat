@echo off
REM Stop and remove existing containers
docker compose -f docker-compose.yml ^
               -f ..\api_gateway\docker-compose.yml ^
               -f ..\services\IAM\docker-compose.yml ^
               down

REM Rebuild and start fresh
docker compose -f docker-compose.yml ^
               -f ..\api_gateway\docker-compose.yml ^
               -f ..\services\IAM\docker-compose.yml ^
               up -d --build


REM Check status
if %ERRORLEVEL% EQU 0 (
    echo Deployment succeeded.
) else (
    echo Deployment failed with error code %ERRORLEVEL%.
)

echo.
echo Press any key to exit...
pause >nul