'''
문자열 객체는 인덱스로 접근은 가능하나 업데이트는 불가능

문자열 메소드
s = "python is scripting Language"
s.lower() / s.upper()
s.strip()

s.isalpha() / s.isdigit() / s.isspace() / s.isalnum()

s.startswith('start')
s.endswith('end')

s.find('str')
s.replace('old', 'new')
s.split(구분문자)
"".join(리스트)


문자열 포맷팅
1) % - 포멧
ex) name = 'Byoungjeon'
"Hello %s" %name
>> Hello Daeseok

"My name is %s, age is %s." %(name, age)
>> My name is Byoungjeon, age is 26.

2) str.format() 메서드
name = 'Byoungjeon' / age = 26
"Hello, my name is {} and I'm {}".format(name, age)
"Hello, my name is {1} and I'm {0}".format(age, name)

who = {'name':'Byoungjeon', 'age': 26}
"Hello, my name is {name} and I'm {age}".format(name= who['name'], age=who['age']
>>"Hello, my name is Byoungjeon and I'm 26"

"Hello, my name is {'name'} and I'm {age}".format(**who)

3) f-string 포매팅
name = 'Byoungjeon' / age = 26
f"Hello my name is {name} and I'm {age} years old."

'''
