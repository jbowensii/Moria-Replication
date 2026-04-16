@echo off
REM ============================================================================
REM  Phase 3: Batch Import FModel JSON Exports via JsonAsAsset
REM
REM  Usage:
REM    batch_import.bat                      Import all assets
REM    batch_import.bat DataTable            Import only DataTables
REM    batch_import.bat DataTable save       Import DataTables and auto-save
REM ============================================================================

setlocal

set UE4EDITOR="C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\Win64\UE4Editor-Cmd.exe"
set PROJECT="%~dp0..\project\Moria.uproject"
set EXPORTS="%~dp0..\tools\fmodel-export\Exports"

REM Parse arguments
set FILTER=%~1
set SAVE_FLAG=

if /i "%~2"=="save" set SAVE_FLAG=-save
if /i "%~1"=="save" (
    set FILTER=
    set SAVE_FLAG=-save
)

echo ============================================
echo  JsonAsAsset Batch Import
echo ============================================
echo  Project:  %PROJECT%
echo  Exports:  %EXPORTS%
if defined FILTER (
    echo  Filter:   %FILTER%
) else (
    echo  Filter:   (none - all assets)
)
if defined SAVE_FLAG (
    echo  Save:     Yes
) else (
    echo  Save:     No (use 'save' argument to auto-save)
)
echo ============================================
echo.

REM Build the command
set CMD=%UE4EDITOR% %PROJECT% -run=BatchImport -dir=%EXPORTS% -project=Moria
if defined FILTER set CMD=%CMD% -filter=%FILTER%
if defined SAVE_FLAG set CMD=%CMD% -save

echo Running: %CMD%
echo.

%CMD%

set EXITCODE=%ERRORLEVEL%

echo.
if %EXITCODE%==0 (
    echo [SUCCESS] Batch import completed successfully.
) else (
    echo [WARNING] Batch import completed with some failures. Check log above.
)

endlocal
exit /b %EXITCODE%
