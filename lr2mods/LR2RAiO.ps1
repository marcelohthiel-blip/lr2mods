$global:root_drive = "C:"
$global:working_folder = "LR2-Reformulate"
$global:branch_name = "develop"
$global:repository_url = "https://gitgud.io/lab-rats-2-mods/lr2mods.git"
$global:mods = @{
    Kaden    = "https://gitgud.io/Kaden3701/lr2-mods_kaden.git";
    KiNASuki = "https://gitgud.io/KiNASuki/lr2-kina-mods.git";
}

function GetGitBranch() {
    return &git rev-parse --abbrev-ref HEAD
}

function UpdateBranchAndWorkFolder {
    $current_folder = $MyInvocation.PSScriptRoot
    $git_folder = Join-Path -Path $current_folder -ChildPath ".git"
    if (Test-Path -Path $git_folder) {
        $global:root_drive = Split-Path -Path $current_folder -Qualifier
        $global:working_folder = Split-Path -Path $current_folder -NoQualifier

        $global:branch_name = GetGitBranch
    }
}

function InstallationDirectory {
    return Join-Path -Path $global:root_drive -ChildPath $global:working_folder
}

function IsGitInstalled {
    $gitInstalled = Get-Command -ErrorAction SilentlyContinue git
    return $null -ne $gitInstalled
}

function Get-UrlStatusCode([string] $url)
{
    try
    {
        (Invoke-WebRequest -Uri $url -UseBasicParsing -DisableKeepAlive).StatusCode
    }
    catch [Net.WebException]
    {
        [int]$_.Exception.Response.StatusCode
    }
    catch
    {
        return 0
    }
}

function IsRemoteUrlAvailable($url){
    if ((Get-UrlStatusCode $url) -ne 200) {
        Write-Error -Message "Unable to communicate with remote origin '$url', check if your internet connection is working."
        return $false
    }
    return $true
}

function ExecutPullFromGIT($branch) {
    $originURL = ((git.exe remote -v) -match '^origin.*fetch\)$' -replace '^origin\s*|\s*\(fetch\)$')
    if ($null -eq $originURL) {
        Write-Error "No remote origin found, the repository is not configured to sync with remote."
        return $false
    }

    if ((IsRemoteUrlAvailable($($originURL))) -eq $false) {
        return $false
    }

    $lfs_version = ((git lfs version) -match 'git-lfs/(\d+\.\d+\.\d+)')
    if ($lfs_version -eq $false) {
        Write-Error "Git LFS is not installed or not configured correctly. Please install Git LFS from https://git-lfs.github.com/ and try again."
        return $false
    }

    $changed_files = $(git status --porcelain | Measure-Object | Select-Object -expand Count)
    if ($changed_files -gt 0) {
        $choice = Read-Host "Some files have been changed, please confirm that you want to reset the changes and continue with the update (y/n)"
        if ($choice -ne "y") {
            Write-Host "Update aborted."
            return $false
        }
    }

    git fetch --all -q

    $current_branch = GetGitBranch
    if ($current_branch -ne $branch) {
        Write-Host "Switching branch..."
        git reset --hard -q
        git switch $branch -q
        Write-Host "to $(VersionString) version."
    }

    ($localCommit = git rev-parse $branch)
    ($remoteCommit = (git ls-remote origin $branch) -replace '\s.*$')
    if ($localCommit -ne $remoteCommit) {
        Write-Host "Pulling changes..."
        git reset --hard -q
        git pull
        Write-Host "Completed"

        return $true
    }
    Write-Host "Already up to date. No changes made."
    return $false
}


function CloneRepository($url, $branch, $target_folder) {
    if ((IsRemoteUrlAvailable($url)) -eq $false) {
        return $false
    }
    CreateTargetFolder $target_folder

    Write-Host ""
    Write-Host "Clone remote repository" $branch "to" $target_folder
    Write-Host "This can take up to several hours, depending on the speed of your internet connection."
    Write-Host "GIT progress will stall on Filtering Content, but the download will continue, just be patient."
    Write-Host ""

    git lfs install
    git clone -b $branch $url $target_folder

    Write-Host "Retrieval of repository is complete."
    Set-Location -Path $target_folder

    Write-Host "LabRats 2 - Reformulate has been installed in $target_folder. Game version" (VersionString) "is ready."
    Write-Host "If you want to update the game in the future, run this script again."
}

function CloneModRepository($url, $branch, $target_folder) {
    if ((IsRemoteUrlAvailable($url)) -eq $false) {
        return $false
    }
    CreateTargetFolder $target_folder

    Write-Host ""
    Write-Host "Clone remote repository" $branch "to" $target_folder

    git clone -b $branch $url $target_folder
    Write-Host "Retrieval mod is complete."
}

function ExtractRuntime($target_folder) {
    $check_file = Join-Path $target_folder -ChildPath "LabRats2-Reformulate.exe"
    $target_file = Join-Path $target_folder -ChildPath "LR2R-Runtime.zip"

    if (Test-Path $check_file -PathType Leaf) {
        $overwrite = Read-Host "The game executable already exists, do you want to overwrite it (y/n)"
        if ($overwrite -ne "y") {
            return
        }
    }

    if (Test-Path $target_file -PathType Leaf) {
        Write-Host "Extract Runtime to" $target_folder
        Expand-Archive $target_file -DestinationPath $target_folder -Force
    }
    else {
        Write-Warning "Compressed runtime not found, you won't be able to run the game without it."
    }
}

function CheckoutModRepository($url, $branch, $target_folder) {
    Set-Location -Path $target_folder
    Write-Host "Clone remote repository $branch to $target_folder"

    $updated = ExecutPullFromGIT($branch)
    if ($updated -eq $true) {
        CleanupGameFolder
    }

    Write-Host "Checkout mod from $url complete."
    Write-Host ""
}

function CheckOutRepository($url, $branch, $target_folder) {
    Set-Location -Path $target_folder

    Write-Host "Checkout branch: " $branch

    $updated = ExecutPullFromGIT($branch)
    if ($updated -eq $true) {
        CleanupGameFolder
    }

    Write-Host "Operations complete ($(VersionString))."
    Write-Host ""
}

function CleanupGameFolder() {
    Write-Host "Cleanup game directory"
    $target_folder = InstallationDirectory
    $game_folder = Join-Path $target_folder -ChildPath "game"
    Get-ChildItem -Path $game_folder *.rpyc -Recurse | ForEach-Object { Remove-Item -Path $_.FullName }
}

function CreateTargetFolder($path) {
    If (!(test-path -PathType container $path)) {
        Write-Host "Creating target folder" $path
        New-Item -ItemType Directory -Path $path
    }
}

function GetChoiceNumber {
    $choice = Read-Host "Enter choice"
    return $choice
}
function ChooseGitBranch {
    Write-Host ""
    Write-Host "1. Stable Release"
    Write-Host "2. Beta Version"

    $choice = Read-Host "Which version do you want to install"

    $current_branch = $global:branch_name

    # default is master
    $global:branch_name = "master"
    if ($choice -eq 2) {
        $global:branch_name = "develop"
    }

    return ($global:branch_name -ne $current_branch)
}

function PressAnyKeyToContinue {
    if ($psISE) {
        Read-Host 'Press enter key to continue...';
    }
    else {
        Write-Host -NoNewLine 'Press any key to continue...';
        $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');
    }
}

function VersionString {
    if ($global:branch_name -eq "master") {
        return "Stable"
    }
    return "Beta"
}

function GameInstalled {
    $target_folder = InstallationDirectory
    return (Test-Path -Path (Join-Path -Path $target_folder -ChildPath "LR2.code-workspace") -PathType Leaf)
}

function UpdateGameFromGIT {
    $installation_folder = InstallationDirectory

    CheckOutRepository $global:repository_url $global:branch_name $installation_folder

    ExtractRuntime $installation_folder
}

function UnInstallMod($name, $target_folder) {
    $root_folder = InstallationDirectory
    Set-Location -Path $root_folder

    Write-Host "Uninstalling mod" $name
    $succes = DeleteFolder $target_folder
    if ($succes -eq $false) {
        Write-Host "Failed to delete MOD folder $target_folder"
        return
    }
    Write-Host "Uninstall complete."
    Write-Warning "Uninstalling a mod will prevent game saves made with the mod installed from working."
}

function DeleteFolder($target_folder) {
    $err = @()
    Remove-Item -Path $target_folder -Recurse -Force -Confirm:$false -ErrorAction SilentlyContinue -WarningAction SilentlyContinue -ErrorVariable err

    if ($err.count -ne 0) {
        return $false
    }
    return $true
}

function InstallGameFromGIT {
    $installation_folder = InstallationDirectory

    if (!(Test-Path -Path $installation_folder)) {
        CreateTargetFolder $installation_folder
    }
    else {
        $directoryInfo = Get-ChildItem $installation_folder | Measure-Object
        if ($directoryInfo.Count -ne 0) {
            Write-Host "Installation folder $installation_folder is not empty."
            $force_install = Read-Host "Do you want to force installation to that folder (y/n)"
            if ($force_install -ne "y") {
                return
            }

            $succes = DeleteFolder $installation_folder
            if ($succes -eq $false) {
                Write-Host "Failed to delete folder $installation_folder"
                return
            }

            # continue installation by creating new empty folder
            CreateTargetFolder $installation_folder
        }
    }

    CloneRepository $global:repository_url $global:branch_name $installation_folder

    ExtractRuntime $installation_folder
}

function MenuHeader {
    $target_folder = InstallationDirectory
    $target_version = VersionString

    Clear-Host

    Write-Host "LabRats 2 - Main Installation Menu"
    Write-Host ""
    Write-Host "Installation Folder:" $target_folder
    Write-Host "Version:" $target_version
    Write-Host ""
}

function BuildFolder($base_folder, $path_array) {
    $path_array | ForEach-Object {
        $base_folder = Join-Path -Path $base_folder -ChildPath $_
    }
    return $base_folder
}

function ModInstallMenu {
    $continue = $true
    while ($continue) {
        MenuHeader

        $actions = @()
        $global:mods.GetEnumerator() | ForEach-Object {
            $installation_folder = InstallationDirectory
            $path = @("game", "mods", $_.Key)
            $target_folder = BuildFolder $installation_folder  $path
            $count = $actions.Count + 1

            if (Test-Path -Path $target_folder) {
                Write-Host "$count. Update $($_.Key)'s mod"
                $actions += , @("CheckOutModRepository", $_.Value, $target_folder)
                $count = $actions.Count + 1
                Write-Host "$count. Remove $($_.Key)'s mod"
                $actions += , @("UninstallMod", $($_.Key), $target_folder)
            }
            else {
                Write-Host "$count. Install $($_.Key)'s mod"
                $actions += , @("CloneModRepository", $_.Value, $target_folder)
            }
        }

        Write-Host ""
        Write-Host "Other choice or enter key returns to main installer menu"

        $choice = GetChoiceNumber
        if ($choice -in 1..$actions.Count) {
            $execute = $actions[$choice - 1]

            if ($execute[0] -eq "UninstallMod") {
                &$execute[0] $execute[1] $execute[2]
            }
            else {
                &$execute[0] $execute[1] $global:branch_name $execute[2]
            }
            PressAnyKeyToContinue
        }
        else {
            $continue = $false
        }
    }
}

function MainInstallMenu {
    $continue = $true
    while ($continue) {
        MenuHeader

        Write-Host "1. Change Installation Folder"
        Write-Host "2. Change Version"
        Write-Host "3. Install Game"
        Write-Host ""
        Write-Host "Other choice or enter key quits installer"

        $choice = GetChoiceNumber
        $continue = $true
        $action_executed = $true
        if ($choice -eq 1) {
            Write-Host "For changing the drive, modify this scripts first line in a text editor and change the 'root_drive' parameter."
            Write-Host "For changing the installation folder, modify this scripts second line in a text editor and change the 'working_folder' parameter."
        }
        elseif ($choice -eq 2) {
            ChooseGitBranch
            $action_executed = $false
        }
        elseif ($choice -eq 3) {
            InstallGameFromGIT
            $continue = $false
        }
        else {
            $action_executed = $false
            $continue = $false
        }

        if ($action_executed) {
            PressAnyKeyToContinue
        }
    }
}

function MainUpdateMenu {
    $continue = $true
    while ($continue) {
        MenuHeader

        Write-Host "1. Change Version"
        Write-Host "2. Update Game"
        Write-Host "3. Install/Update Mods"
        Write-Host ""
        Write-Host "Other choice or enter key quits installer"

        $choice = GetChoiceNumber
        $continue = $true
        $action_executed = $false
        if ($choice -eq 1) {
            $swith = ChooseGitBranch
            if ($swith -eq $true) {
                UpdateGameFromGIT
                $continue = $false
                $action_executed = $true
            }
        }
        elseif ($choice -eq 2) {
            UpdateGameFromGIT
            $continue = $false
            $action_executed = $true
        }
        elseif ($choice -eq 3) {
            ModInstallMenu
            $action_executed = $false
        }
        else {
            $action_executed = $false
            $continue = $false
        }
        if ($action_executed) {
            PressAnyKeyToContinue
        }
    }
}


function InstallBaseMenu {
    UpdateBranchAndWorkFolder

    if (!(GameInstalled)) {
        MainInstallMenu
    }
    else {
        MainUpdateMenu
    }
}

if (IsGitInstalled) {
    InstallBaseMenu
    exit
}

Write-Host "Unable to locate a git installation on your system."
Write-Host "Please download and install git from https://git-scm.com/downloads for your OS and try again."
