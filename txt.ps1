Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing


if(-not("Mouse" -as [type])){
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Mouse {
    [DllImport("user32.dll")]
    public static extern bool SetCursorPos(int x, int y);
    [DllImport("user32.dll", CharSet = CharSet.Auto, CallingConvention = CallingConvention.StdCall)]
    public static extern void mouse_event(uint dwFlags, uint dx, uint dy, uint cButtons, uint dwExtraInfo);
    public const int MOUSEEVENTF_LEFTDOWN = 0x02;
    public const int MOUSEEVENTF_LEFTUP = 0x04;
    public static void ClickLeftMouseButton(int x, int y) {
        SetCursorPos(x, y);
        mouse_event(MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP, (uint)x, (uint)y, 0, 0);
    }
}
"@
}
function Start-AntiscreenSaver {
    Write-Host "Anti-screensaver script running from 10:00 to 22:59..." -ForegroundColor Green
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing

    $currentPolicy = Get-ExecutionPolicy
    Set-ExecutionPolicy RemoteSigned -Scope Process

    while ($true) {
        $currentTime = Get-Date -Format "HH:mm:ss"
        $randomMinute = Get-Random -Minimum 49 -Maximum 59
        # Start-Sleep -Seconds (Get-Random -Minimum 1 -Maximum 100)
        $randomDelay = Get-Random -Minimum 1 -Maximum 100
        Write-Host "Sleeping for $randomDelay seconds..." -ForegroundColor Yellow
        Start-Sleep -Seconds $randomDelay



        if (($currentTime -gt "10:00:00") -and ($currentTime -lt "22:" + $randomMinute + ":00")) {
            Start-MoveIfSamePosition
        }
    }

    Set-ExecutionPolicy $currentPolicy -Scope Process
}

function Start-MoveIfSamePosition {
    $screenWidth = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Width
    $screenHeight = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Height
    $randX = Get-Random -Minimum 0 -Maximum $screenWidth
    $randY = Get-Random -Minimum 0 -Maximum $screenHeight

    Write-Host "Moving mouse to X:$randX Y:$randY" -ForegroundColor Cyan
    [Mouse]::SetCursorPos($randX, $randY)
    Start-Sleep -Seconds 2
    [Mouse]::ClickLeftMouseButton($randX, $randY)
}

Start-AntiscreenSaver
