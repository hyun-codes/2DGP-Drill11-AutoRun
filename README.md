# Drill #11 AutoRun

`grass.py`, `boy.py`, `main.py`와 기존 PNG 두 개로 구성한 과제입니다.
Python 3.13 64비트를 사용합니다.

새로 내려받은 저장소 폴더에서는 다음과 같이 실행합니다.

```powershell
py -3.13 -m venv .venv
& .\.venv\Scripts\python.exe -m pip install pico2d==1.5.1 transitions==0.9.3
& .\.venv\Scripts\python.exe .\main.py
```

현재 PC의 과제 폴더는 `D:\2DGP_homework\2DGP-Drill11-AutoRun`입니다.
이 폴더 안에 코드, 이미지, `.venv`, `.vscode`가 함께 있습니다.
상위 폴더의 가상환경을 참조하지 않습니다.

VS Code에서 이 과제 폴더 자체를 열고 `main.py`를 실행하거나 **F5**를 누릅니다.
`boy.py`와 `grass.py`는 `main.py`가 사용하는 클래스 파일입니다.

좌우 방향키로 달리고, 키를 놓으면 대기합니다. 대기 중 **a**를 누르면
5초 동안 2배 속도와 1.5배 크기로 자동 이동하며 양쪽 끝에서 방향을 바꿉니다.
자동 이동 중 방향키를 누르면 해당 방향의 일반 달리기로 전환합니다.
**ESC** 또는 창 닫기로 종료합니다.

이미지는 실행 파일 폴더에서 상대 경로로 읽으므로 이 폴더를 작업 디렉터리로 사용하세요.
