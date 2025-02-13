Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nota1=input("primeira nota)
...             
SyntaxError: unterminated string literal (detected at line 1)
>>> nota1= input("primeira nota: ")
...             
primeira nota: 10
>>> print nota1
...             
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> type nota1
...             
SyntaxError: invalid syntax
>>> type (nota1)
...             
<class 'str'>
>>> print (nota1)
...             
10
>>> 
========================================================================== RESTART: Shell =========================================================================
>>> nota 1= int(input("primeira nota: )
...                   
SyntaxError: unterminated string literal (detected at line 1)
>>> nota 1= int(input("primeira nota: ")
...             
SyntaxError: invalid syntax
>>> nota1= int(input("primeira nota: "))
...             
nota1= int(input("primeira nota: "))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    nota1= int(input("primeira nota: "))
ValueError: invalid literal for int() with base 10: 'nota1= int(input("primeira nota: "))'
>>> 
>>> 
========================================================================== RESTART: Shell =========================================================================
>>> [DEBUG ON]
>>> [DEBUG OFF]
