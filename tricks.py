Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10,b=10.1,c="10"
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=10
b=10.1
c="10"
print(type(a),type(b),type(c))
<class 'int'> <class 'float'> <class 'str'>
a=10
b=5
a=a+b
b=a-b
a=a-b
a
5
b
10
a="vjifweuqure"
count=0
for i in a:
    count+=1

print(count)
11
a,b,c=10,10.121,'python;
SyntaxError: unterminated string literal (detected at line 1)
a,b,c=10,10.121,'python'
type(c)
<class 'str'>
type(a)
<class 'int'>
type(b)
<class 'float'>
x=1
y=2
x,y=y,x
x
2
y
1
