'''
입력받은 문자열이 유효한 IPv4, IPv6인지 확인하는 함수 작성
IPv4 > .으로 분리된 4개의 10진수로 구성, 각 숫자들은 0~255, 0으로 시작할 수 없음
IPv6 > :으로 구분, 4자리 16진수로 구성, 4자리의 숫자 8개의 그룹으로 표현,
        4자리를 채우기위해 0으로 시작하는 숫자가 있을 수도 있음
'''

'''
방법 1 시간복잡도 O(L)(입력 문자열 길이), 공간복잡도 O(1)
1. 점(.)과 콜론(:)으로 IPv4, IPv6 구분
2. IPv4확인
    - 점으로 문자열 리스트 분리
    - 분리된 리스트의 크기가 4인지 확인
    - 각 문자열 순회
    - 문자열 길이가 1~3인지 확인
    - 해당 문자열이 '0'이라면 길이가 1인지 확인
    - 해당 문자열이 숫자이고 255보다 작은지 확인
3. IPv6확인
    - 콜론으로 문자열 리스트 분리
    - 분리된 리스트 크기가 8인지 확인
    - 각 분리된 문자열의 길이가 0~4인지 검사
    - 문자열 각 문자가 모두 16진수 숫자 및 문자로 구성되어 있는지 확인
'''
#ipv4 / ipv6 검증
def check_ipv4(ipv4:str)->str:
    ipnums = ipv4.split(".")

    for num in ipnums:
        if len(num) == 0 or len(num)>3:
            return 'Neither'

        if(len(num) != 1 and num[0] == '0') or \
            not num.isdigit() or int(num)>255:
            return 'Neither'

    return 'IPv4'

print(check_ipv4('234.255.5.0'))

import string
def check_ip_v6(ipv6:str)->str:
    ipnums = ipv6.split(":")

    for num in ipnums:
        if len(num) == 0 or len(num) > 4 or \
            not all(c in string.hexdigits for c in num):
            return 'Neither'

def validIPAddress(IP:str)->str:
    if IP.count('.') == 3:
        return check_ip_v4(IP)
    elif IP.count(':') == 7:
        return check_ip_v6(IP)

    return 'Neither'

'''
방법 2 시간복잡도 O(1)(입력 문자열 길이), 공간복잡도 O(1)
1. IPv4의 규칙을 따르는 정규 문법 구성
2. IPv6의 규칙을 따르는 정규 문법 구성
3. 정규 문법 실행 및 규칙 반환
'''
import re

ipv4_pattern = r"(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.\
        (\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])"

ipv4_pattern = r"((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))\.){3}(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])"


# 더 간단한 표기
ipv4_num_part = r"(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])"
ipv4_pattern = re.compile(r"(^{p}\.){{3}}{p}$".format(p=ipv4_num_part))

def validIPAddress(IP:str)->str:
    IPV4 = '(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])'

    ipv4 = re.compile(r'^({p}\.){{3}}{p}$'.format(p=IPV4))

    if ipv4.match(IP):
        return "IPv4"

    IPV6 = '([0-9a-f]{1,4})'

    ipv6 = re.compile(r'^({p}\:){{7}}{p}$'.format(p=IPV6), re.IGNORECASE)

    if ipv6.match(IP):
        return "IPv6"

    return "Neither"

print(validIPAddress("234.1.32.126"))
print(validIPAddress("12a2:24b6:0:0:0:1490:5fcf:9def"))
print(validIPAddress("12A2:24B6:0:0:0:1490:5FCF:9DEF"))
print(validIPAddress("256.256.256.256"))
print(validIPAddress("0.0.0.0"))
