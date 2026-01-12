@echo off
setlocal enabledelayedexpansion
if exist "%~dp0\lr2mods" (
	echo Please move this program into the lr2mods folder or game folder to continue.
	pause
	Exit 0
)
if exist "LR2.code-workspace" (
	echo Game found.
	if not exist .git (
		echo Game is found but it doesn't contain a .git folder. This script doesn't support non git distribution of the game.
		echo Please move this script into an empty folder for it to work, or run it again for it to create it.
		pause
		Exit 0
	)
) else (
	set /P INPUT=LR2R Game is not found. Would you like to install in this folder? [y/n]: 
	CALL :GameInstall
)
if exist "%~dp0\renpy" (
	echo Renpy found.
) else (
	echo.
	echo Renpy is not found. Please extract the newly created file named 'LR2R-Runtime.zip' into the same folder as this script.
	echo Run the script again after this step. This message will not appear if extraction is done correctly.
	echo Press any button to exit.
	echo.
	pause
	Exit 0
)
if exist .git (
	echo.
) else (
	echo This doesn't appear to be a local git repo, please run this program in a local git repo of LR2 or in an empty folder for install.
	echo Actually, it should be impossible to see this text in runtime. But I will keep it here in case of a cosmic ray bit flip or something.
	pause
	Exit 0
)
::This deletes the old VT replacer mod
if exist "%~dp0\game\VTcommit.txt" (
	CALL :VTUninstall
)
::This mess is the update code
if exist "%~dp0\lr2aio" (
	cd "%~dp0\lr2aio"
	git fetch > nul
	git pull > nul
	git reset --hard HEAD
	cd ..
	set file1="%~dp0\lr2aio\LR2_AIO_Script.bat"
	set file2="%~dp0\LR2_AIO_Script.bat"
	fc !file1! !file2! > nul
	if !errorlevel! equ 0 (
		echo AIO is up to date!
	) else (
		echo There is a new version of the AIO script.
		set /P INPUT=Would you like to update? [y/n]:
		if /I !INPUT!==y (
			xcopy "%~dp0\lr2aio\LR2_AIO_Script.bat" "%~dp0\" /Y > nul
			echo Update complete, please restart the script.
			pause
			Exit 0
		) else (
			echo Update skipped.
		)
		set INPUT=n
	)
) else (
	git clone https://gitgud.io/Krul/lr2aio.git
)

echo Updating base game...
git fetch
git pull
git reset --hard HEAD
echo.
echo Fair Warning, Installing or Uninstalling any mod will most likely break your game save.
echo.

cd "%~dp0\game\mods"

::Mod repo structure, folder name, branch, repo link
CALL :GitUpdate lr2-kina-mods develop https://gitgud.io/KiNASuki/lr2-kina-mods.git
CALL :GitUpdate lr2-mods_kaden develop https://gitgud.io/Kaden3701/lr2-mods_kaden.git
CALL :GitUpdate LR2R VTMod https://github.com/Elkrose/LR2R.git

CALL :Delrpyc
echo.
echo Everything is updated, have fun.
pause
goto :eof

:GitUpdate
	echo.
	set ModFolderName=%~1
	if exist !ModFolderName!/ (
		echo Updating !ModFolderName!...
		cd !ModFolderName!
		if exist .git (
			git fetch
			git pull
			git reset --hard HEAD
			cd ..
		)
	
	) else (
		set /P INPUT=/mods/!ModFolderName!/ folder not found. Would you like to install? [y/n]: 
		CALL :GitInstall %~2 %~3
	)
goto :eof

:GitInstall
	if /I !INPUT!==y (
		git clone -b %~1 %~2
	) else (
		echo Install skipped.
	)
	set INPUT=n
goto :eof

:GameInstall
	if /I !INPUT!==y (
		echo Installing LR2mods-develop branch in lr2mods folder.
		echo.
		echo Don't worry if it appears stuck, downloading images takes a while.
		echo.
		git clone -b develop https://gitgud.io/lab-rats-2-mods/lr2mods.git
		cls
		echo LR2R Game is installed in lr2mods folder.
		echo The AIO script has moved itself into newly created lr2mods folder.
		echo Please run the script again inside the lr2mods folder.
		xcopy "%~dp0\LR2_AIO_Script.bat" "%~dp0\lr2mods" /Y > nul
		del /F /Q "%~dp0\LR2_AIO_Script.bat"
		pause
		Exit 0
	) else (
		echo Exiting.
		pause
		Exit 0
	)
goto :eof

:Delrpyc
	echo.
	set /P INPUT=Would you like to delete all .rpyc files? Recommended to do when game updates, crashes or changing mods. [y/n]:
	if /I !INPUT!==y (
		del /F /Q /S "%~dp0\game\*.rpyc" > nul
		echo.
		echo All .rpyc files are deleted. Next game launch will take a longer than usual to recompile them.
		echo.
	) else (
		echo Delete skipped.
	)
	set INPUT=n
goto :eof

:VTUninstall
	del /F /Q "%~dp0\game\VTcommit.txt"
	rmdir /S /Q "%~dp0.\LR2-VT\"
	git reset --hard HEAD
	git fetch
	git pull
	echo.
	echo Replacer version of Virgin Tracker is uninstalled for your convenience, you can install the new version instead.
	echo.
	pause
goto :eof