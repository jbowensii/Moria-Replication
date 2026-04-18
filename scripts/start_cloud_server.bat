@echo off
REM ============================================================================
REM  Start JsonAsAsset Cloud Server (Core.exe)
REM
REM  Reads Return to Moria game paks and serves asset data to JsonAsAsset plugin.
REM  Opens web UI at http://localhost:1500 for configuration.
REM
REM  First-time setup:
REM    1. Run this script
REM    2. Open http://localhost:1500 in your browser
REM    3. Click "Add Profile" or configure game path
REM    4. Set pak directory to: C:\Program Files\Epic Games\ReturnToMoria\Moria\Content\Paks
REM    5. Set project name to: Moria
REM    6. The server is now ready — JsonAsAsset plugin will auto-connect
REM
REM  Requirements:
REM    - .NET 8.0+ runtime (10.0 works via roll-forward)
REM ============================================================================

setlocal

REM Core.exe targets .NET 8 — requires ASP.NET Core 8.0 runtime (install via:
REM   winget install Microsoft.DotNet.AspNetCore.8)
REM Do NOT set DOTNET_ROLL_FORWARD=LatestMajor — it breaks ASP.NET Core HTTP pipeline.
set SERVER_DIR=%~dp0..\tools\JsonAsAssetServer
set SERVER_EXE=%SERVER_DIR%\Core.exe

if not exist "%SERVER_EXE%" (
    echo ERROR: Core.exe not found at %SERVER_EXE%
    echo Install JsonAsAsset Cloud Server to tools\JsonAsAssetServer\
    exit /b 1
)

echo ============================================
echo  JsonAsAsset Cloud Server
echo ============================================
echo  Server:  %SERVER_EXE%
echo  Web UI:  http://localhost:1500
echo  Status:  http://localhost:1500/api/status
echo ============================================
echo.
echo Starting server... (Ctrl+C to stop)
echo.

cd /d "%SERVER_DIR%"
"%SERVER_EXE%"

endlocal
