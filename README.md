# Drill #11 AutoRun

`grass.py`, `boy.py`, `main.py`와 기존 PNG 두 개로 구성한 과제입니다.
Python 3.13 64비트를 사용합니다.

새로 내려받은 저장소 폴더에서는 다음과 같이 실행합니다.

```powershell
py -3.13 -m venv .venv
& .\.venv\Scripts\python.exe -m pip install pico2d==1.5.1 transitions==0.9.3
& .\.venv\Scripts\python.exe .\main.py
```

현재 PC에서는 이 과제 폴더로 이동한 후 이미 설치한 상위 가상환경을 사용합니다.

```powershell
& ..\.venv\Scripts\python.exe .\main.py
```

좌우 방향키로 달리고, 키를 놓으면 대기합니다. 대기 중 **a**를 누르면
5초 동안 2배 속도와 1.5배 크기로 자동 이동하며 양쪽 끝에서 방향을 바꿉니다.
자동 이동 중 방향키를 누르면 해당 방향의 일반 달리기로 전환합니다.
**ESC** 또는 창 닫기로 종료합니다.

이미지는 실행 파일 폴더에서 상대 경로로 읽으므로 이 폴더를 작업 디렉터리로 사용하세요.
