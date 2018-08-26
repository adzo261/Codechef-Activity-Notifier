Set oShell = CreateObject ("Wscript.Shell")
Dim strArgs
strArgs = "cmd /c stop.bat"
oShell.Run strArgs, 0, false