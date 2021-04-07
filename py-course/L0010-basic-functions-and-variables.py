Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sys
>>> type(sys.path)
<class 'list'>
>>> sys.path
['', 'C:\\Bitnami\\pyton3-5-4\\Lib\\idlelib', 'C:\\Bitnami\\pyton3-5-4\\python36.zip', 'C:\\Bitnami\\pyton3-5-4\\DLLs', 'C:\\Bitnami\\pyton3-5-4\\lib', 'C:\\Bitnami\\pyton3-5-4', 'C:\\Bitnami\\pyton3-5-4\\lib\\site-packages']
>>> sys.copyright
'Copyright (c) 2001-2017 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'
>>> sys.int_info
sys.int_info(bits_per_digit=15, sizeof_digit=2)
>>> sys.api_version
1013
>>> sys.displayhook
<function displayhook at 0x02FDD7C8>
>>> float("0x02FDD7C8")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    float("0x02FDD7C8")
ValueError: could not convert string to float: '0x02FDD7C8'
>>> float(0x02FDD7C8)
50190280.0
>>> cadena = "Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32 Type 'copyright', 'credits' or 'license()' for more information."
>>> cadena
"Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32 Type 'copyright', 'credits' or 'license()' for more information."
>>> list(cadena)
['P', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '6', '.', '2', ' ', '(', 'v', '3', '.', '6', '.', '2', ':', '5', 'f', 'd', '3', '3', 'b', '5', ',', ' ', 'J', 'u', 'l', ' ', ' ', '8', ' ', '2', '0', '1', '7', ',', ' ', '0', '4', ':', '1', '4', ':', '3', '4', ')', ' ', '[', 'M', 'S', 'C', ' ', 'v', '.', '1', '9', '0', '0', ' ', '3', '2', ' ', 'b', 'i', 't', ' ', '(', 'I', 'n', 't', 'e', 'l', ')', ']', ' ', 'o', 'n', ' ', 'w', 'i', 'n', '3', '2', ' ', 'T', 'y', 'p', 'e', ' ', "'", 'c', 'o', 'p', 'y', 'r', 'i', 'g', 'h', 't', "'", ',', ' ', "'", 'c', 'r', 'e', 'd', 'i', 't', 's', "'", ' ', 'o', 'r', ' ', "'", 'l', 'i', 'c', 'e', 'n', 's', 'e', '(', ')', "'", ' ', 'f', 'o', 'r', ' ', 'm', 'o', 'r', 'e', ' ', 'i', 'n', 'f', 'o', 'r', 'm', 'a', 't', 'i', 'o', 'n', '.']
>>> cadena.split()
['Python', '3.6.2', '(v3.6.2:5fd33b5,', 'Jul', '8', '2017,', '04:14:34)', '[MSC', 'v.1900', '32', 'bit', '(Intel)]', 'on', 'win32', 'Type', "'copyright',", "'credits'", 'or', "'license()'", 'for', 'more', 'information.']
>>> cadena.split(",")
['Python 3.6.2 (v3.6.2:5fd33b5', ' Jul  8 2017', " 04:14:34) [MSC v.1900 32 bit (Intel)] on win32 Type 'copyright'", " 'credits' or 'license()' for more information."]
>>> cadena2 = "lunes\tmartes\tmiércoles\tjueves\tviernes\tsábado\tdomingo"
>>> cadena2.split("\t")
['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
>>> cadena2
'lunes\tmartes\tmiércoles\tjueves\tviernes\tsábado\tdomingo'
>>> print(cadena2)
lunes	martes	miércoles	jueves	viernes	sábado	domingo
>>> 
