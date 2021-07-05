'''
지역번호에 대한 패턴에서 시작괄호 ( 가 0 혹은 1개 있다
지역번호는 2~3자리이다
지역번호 끝 괄호 ) 가 0개 혹은 1개 있다
지역번호와 다음자리 숫자간 공백이 0개 혹은 1개 있다.
지역번호와 가운데 번호 사이에 대시(-)가 0개 혹은 1개가 있다
가운데 번호는 3~4자리 숫자이다
가운데번호와 마지막 번호 사이 공백이 0개 혹은 1개가 있다
가운데 번호와 마지막 번호 사이에 대시(-)가 0개혹은 1개가 있다
마지막 번호는 3~4자리 숫자이다
'''

# ^\(?[0-9]{2,3}\)?\ ?-?\ ?[0-9]{3,4}\ ?\-?\ ?[0-9]{3,4}$

# ^\(?\d{2,3}\)?\ ?\-?\ ?\d{3,4}\ ?\-?\ ?\d{3,4}$

import re

pattern = re.compile(r'\w{3,4}') # r-string에서 r은 raw로 문자열 그대로 사용하게 해줌
print(pattern)

pattern = re.compile('^\(?[0-9]{2,3}\)?\ ?-?\ ?[0-9]{3,4}\ ?\-?\ ?[0-9]{3,4}$')
print(pattern.match("032) - 9389 - 9483")) # 문자열의 패턴을 검증

pattern = re.compile('^\(?\d{2,3}\)?\ ?\-?\ ?\d{3,4}\ ?\-?\ ?\d{3,4}$')
print(pattern.match("02) - 9822 - 1234"))

pattern = re.compile('[a-z]+')
print(pattern.match('helloworld'))
print(pattern.match('HelloWorld'))

pattern = re.compile('[a-z]+', re.IGNORECASE)
print(pattern.match('HelloWorld'))
#re.IGNORECASE : 대소 구분 없음

pattern = re.compile('[a-z]+')
print(pattern.search('This is for search()'))
print(pattern.findall('This is for findall()'))
# search : 소문자 조합을 처음 발견 시 반환
# findall : 소문자 조합을 모두 찾아 문자열 리스트로 반환




