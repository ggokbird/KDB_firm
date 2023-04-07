AlPath := "C:\Program Files (x86)\ESTsoft\ALZip\ALZip.exe" ; Al-Zip 실행 파일 경로. 설치 위치에 맞게 변경하세요.

^!z::
{
    ; 선택된 파일 목록을 가져옵니다.
    Send, ^c
    Sleep, 100
    Clipboard := Clipboard

    ; 현재 선택된 파일이 있는 폴더의 경로를 가져옵니다.
    SplitPath, Clipboard, , dir

    ; 현재 날짜와 시간을 가져옵니다.
    FormatTime, nowDateTime,, yyyyMMdd_HHmmss

    ; 압축 파일 이름을 현재 날짜와 시간으로 설정합니다.
    zipFileName := dir . "\" . nowDateTime . "_compressed_files.zip"

    ; 7-Zip을 사용하여 선택된 파일들을 압축합니다.
    Run, %AlPath% a "%zipFileName%" "%Clipboard%"

    ; 압축이 완료되었음을 알리는 메시지 창을 표시합니다.
    MsgBox, 압축이 완료되었습니다: %zipFileName%
}
return