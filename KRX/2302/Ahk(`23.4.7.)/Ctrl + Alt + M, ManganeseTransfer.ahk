^!m::
{
    ; 현재 선택된 파일의 확장자를 가져옵니다.
    Send, ^c
    Sleep, 500
    Clipboard := Clipboard
    SplitPath, Clipboard, , , ext
    
    Click right  ; 마우스 오른쪽 클릭을 시뮬레이션합니다.
    Sleep 500  ; 명령어 실행 간 지연시간을 추가합니다. 필요한 경우 지연시간을 조절하세요.

    ; 확장자에 따라 다른 메뉴 항목을 선택합니다.
    if (ext == "pdf")  ; pdf 파일의 경우
    {
        SendInput, {Down 12}  ; 12번 아래로 이동합니다. 목록에서 원하는 동작이 있는 위치에 맞게 숫자를 조절하세요.
    }
    else if (ext == "docx")  ; docx 파일의 경우
    {
        SendInput, {Down 13}  ; 13번 아래로 이동합니다. 목록에서 원하는 동작이 있는 위치에 맞게 숫자를 조절하세요.
    }
     else if (ext == "zip")  ; zip 파일의 경우
    {
        SendInput, {Down 11}  ; 11번 아래로 이동합니다. 목록에서 원하는 동작이 있는 위치에 맞게 숫자를 조절하세요.
    }
    ; 추가 확장자를 처리하려면 위의 if문에 더 많은 조건을 추가하세요.

    Sleep 500  ; 명령어 실행 간 지연시간을 추가합니다. 필요한 경우 지연시간을 조절하세요.
    SendInput, {Enter}  ; Enter 키를 눌러 선택한 메뉴 항목을 실행합니다.
}
return
