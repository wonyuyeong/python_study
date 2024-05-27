# 문자열 : 연속된 문자들의 나열, 큰따옴표, 작은따옴표,
# 여러줄 사용할 경우  : '''내용''', """내용"""

str = '헬로 python !'
print(str, type(str))

str = "헬로 python !"
print(str, type(str))

# 두개를 같이 사용하는 경우
str = "I'm OK !!"
print(str, type(str))

str = 'I"m OK !!'
print(str, type(str))

# 이스케이프 문자 사용 가능
str = "I\'m OK !!"
print(str, type(str))

str = 'I\"m OK !!'
print(str, type(str))

str = "안녕하세요 \n반갑습니다"
print(str, type(str))

str = '''
    안녕하세요
    반갑습니다
'''
print(str, type(str))

str = """
    안녕하세요
    반갑습니다
"""
print(str, type(str))