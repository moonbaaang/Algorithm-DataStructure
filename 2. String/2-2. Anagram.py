# 애너그램
'''
같은 알파벳을 가지는 단어들을 조합
collections 모듈에 defaultdict함수로 사전형 선언 시 매 초기 키값이 추가될때마다 대응되는 값의 초기데이터 타입을 만들어줌
'''
import collections
from typing import List
'''
아이디어 1 (정렬 및 해시 테이블) 시간복잡도O(n*LlogL) 공간복잡도O(n*L)
1. 해시테이블 생성
    - 키로 문자열, 값으로 리스트
2. 입력 문자열 리스트 순회
    - 문자열 정렬
    - 정렬된 문자열을 키로 찾은 리스트에 문자열 추가
'''
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hashmap = collections.defaultdict(list)
        
    for s in strs:
        hashmap["".join(sorted(s))].append(s)

    return hashmap.values()

print(groupAnagrams(['ab', 'cd', 'ef', 'abc', 'acb','eat','tea']))
print(groupAnagrams(['abc', 'acb', 'bca']))
'''
아이디어 2 (문자 카운트 및 해시테이블) 시간복잡도O(n*L) 공간복잡도O(n*L)
1. 해시테이블 설정
    - 키로 a-z까지 문자 개수, 튜플값으로 리스트
2. 입력 문자열 리스트 순회
    - 각 문자열 문자를 순회하며 카운트
    - 만들어진 문자 카운트 배열 기준 해시 테이블에서 키로 찾고
    같은 키를 가지는 문자열을 값으로 추가
'''
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hashmap = collections.defaultdict(list)

    for s in strs:
        count = [0]*26 # 알파벳 소문자 저장

        for ch in s:
            count[ord(ch) - ord('a')] += 1
        hashmap[tuple(count)].append(s)

    return hashmap.values()

print(groupAnagrams(['ab', 'cd', 'ef']))
print(groupAnagrams(['abc', 'acb', 'bca']))
