'''
정규표현식
* : 어떤 문자가 0번 혹은 그 이상 출현 가능 (ex, a*b > ab aab aaaaab)
+ : *과 비슷하나 최소 1번 이상 출현
{} : 중괄호 내 숫자 만큼, 혹은 이상(ex, a{3}b > aaaab / a{3,}b > aaaaaaab/  a{2,3}b > aaab aaaab
. : (와일드카드) a.b이면 a와 b 사이 하나의 길이를 갖는 모든 문자 대응 가능
? : (선택문자) ex, colou?r >> color / colour u 문자가 0개 또는 1개
^ : (탈자 부호) 특정 문자, 문자열로 시작하는 문자열 패턴을 만듬. ex, ^a.* > a로 시작하는 모든 문자열
$ : 마지막 문자, 문자열을 지정. ex, .*b$ > b로 끝나는 모든 문자열
[] : 문자 클래스, 해당 범위의 문자를 대시(-)를 통해 지정 ex, [abc] > a 혹은 b 혹은 c가 될수있음, [^cd] > c,d를 제외한 나머지 문자
() : 그룹문자, 특정문자의 조합패턴을 검색하는 경우 사용 ex, (ab)+이면 ab, abab, ababab ,... 가능, ^(th).* > th로 시작하는 모든 문자 가능
| : 수직선 > 비트 연산의 OR연산과 비슷한 역할, 함께 사용된 패턴 중 하나를 선택 및 찾기 가능 > ex, th(is|e|at) > this the that 매칭 가능
\ : 키워드 중 하나를 문자 자체로 찾고 싶은 경우 사용. ex, [0-9]\*[0-9]\+[0-9] > 3*5+5와 같이 사용 가능


문자 클래스       메타문자  설명
[0-9]               \d      숫자와 매치
[^0-9]              \D      숫자를 제외한 나머지 문자와 매치
[ \t\n\r\f\v]       \s      공백문자 : 공백, tab, new line, carriage return, form feed, vertical tab
[^ \t\n\r\f\v]      \S      공백문자를 제외한 나머지와 매치
[a-zA-Z0-9]         \w
[^a-zA-z0-9]        \W
'''
