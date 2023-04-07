#SingleInstance, Force
#NoEnv

; 핫키 설정 (이 예에서는 Ctrl + Alt + Z)
^!z::
{
    ; 선택한 파일이나 폴더의 경로를 클립보드에 저장합니다.
    Send, ^c
    ClipWait, 1
    SelectedFiles := StrSplit(Clipboard, "`n")
    
    ; 현재 시간을 YYMMDDHHMM 형식으로 가져옵니다.
    FormatTime, CurrentTime,, yyMMddHHmm

    ; 새 ZIP 파일의 경로를 설정합니다.
    NewZipFile := A_Desktop . "\" . "download" . CurrentTime . ".zip"

    ; 로그 파일의 경로를 설정합니다.
    LogFile := A_Desktop . "\" . "log" . CurrentTime . ".txt"

    ; 압축 프로세스를 실행합니다.
    Loop, % SelectedFiles.Length()
    {
        SelectedFile := SelectedFiles[A_Index]
        if (SelectedFile != "")
        {
            ; 선택한 파일이나 폴더의 이름을 가져옵니다.
            SplitPath, SelectedFile, name, dir, ext, name_no_ext, drive

            ; 파일 경로에 있는 공백 문자를 유지하기 위해 큰따옴표를 사용합니다.
            RunWait, % "powershell.exe -NoProfile -ExecutionPolicy Bypass -Command ""Add-Type -A 'System.IO.Compression.FileSystem'; try { $source = ('""" SelectedFile """' -replace '\\s+', ' ').trim(); $destination = ('""" NewZipFile """' -replace '\\s+', ' ').trim(); $entryName = ('""" name """' -replace '\\s+', ' ').trim(); $zip = [IO.Compression.ZipFile]::Open($destination, 'Update'); $fileStream = [System.IO.File]::OpenRead($source); $entry = $zip.CreateEntry($entryName); $entryStream = $entry.Open(); $fileStream.CopyTo($entryStream); $entryStream.Close(); $fileStream.Close(); $zip.Dispose(); } catch { $ErrorMessage = $_.Exception.Message; Add-Content -Path '" LogFile "' -Value ('Failed to process: """ SelectedFile """ - Error: ' + $ErrorMessage); }""",,Hide
            
            ; 처리 후 지연 시간 추가 (2000밀리초, 즉 2초)
            Sleep, 2000
        }
    }
}
Return
