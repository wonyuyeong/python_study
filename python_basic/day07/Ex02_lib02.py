import random,os

# random : 난수 발생(0.0 ~ 1.0 미만)
print(random.random())
print(int(random.random()*5))   # 0~4
print(random.randint(1,10))     # 1~10 (끝자리포함됨)

# 리스트 항목을 무작위로 섞는다.
data = [1,2,3,4,5]
print(random.sample(data, len(data)))

# os : 환경변수나 디렉터리, 파일 등의 os 자원을 제어할 수 있게 해주는 모듈
"""
    os.environ : 시스템 환경 변수 값들을 보여주는 역할을 한다.
                 시스템 정보를 딕셔너리 객체로 반환
    
    os.chdir : 현재 디렉토리의 위치를 변경하는 함수
    os.getcwd : 자신의 현재 디렉토리의 위치를 반환
    os.system("명령어") : 시스템의 유틸리티나 dos 명령어들을 파이썬에서 호출
    os.popen : 시스템 명령어를 시킨 결과값을 읽기 모드의 파일 객체로 돌려준다.
    os.path.dirname(__file__) : 현재 위치 저장
    os.mkdir(디렉토리명) : 디렉토리 생성
    os.rmdir(디렉토리명) : 디렉토리 삭제(비어있을 때만 가능)
""" 

# shutil : 파일 복사해주는 모듈

print(os.environ)   # 시스템 정보가 딕셔너리로 나옴
print("-" * 50)

print(os.path.dirname(__file__))    # 현재위치
print(os.getcwd())
