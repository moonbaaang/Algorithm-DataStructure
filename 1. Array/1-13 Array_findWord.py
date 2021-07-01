'''
백트래킹 관련

아이디어
1. board 배열의 모든 요소를 순회
2. word[0]과 board[x][y]요소가 같다면
    - x,y위치 문자와 word의 현재 문자와 같은지 확인
    - x,y가 board크기를 벗어나는지 확인
    - 이미 방문한 위치인지 확인
    - board[x-1][y]와 word의 다음 문자로 재귀호출
    - board[x+1][y]와 word의 다음 문자로 재귀호출
    - board[x][y-1]와 word의 다음 문자로 재귀호출
    - board[x][y+1]와 word의 다음 문자로 재귀호출
'''

from typing import List

def exist(board: List[List[str]], word:str)->bool:
    direction = [[-1,0],[1,0],[0,-1],[0,1]]

    def search_direction(x:int, y:int, subword:str):
        if (x<0 or x>= len(board)) or \
            (y<0 or y>=len(board[0])):
            return False

        if board[x][y] != subword[0]:
            return False

        if len(subword) == 1:
            return True

        board[x][y] = '.'

        for i, j in direction:
            if search_direction(x+i, y+j, subword[1:]):
                return True

        board[x][y] = subword[0]
        return False

    res = False
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == word[0] and \
               search_direction(x, y, word):
                res = True
                break
    return res

print(exist([["A","B","C", "D"],["S","F","S","D"],["A","D","E","D"]], word="BFSE"))
