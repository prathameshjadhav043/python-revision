# Python -
# Guido Van Rossam - 1989
# DOB - Feb 20th 1991

# Functional Prog features - no need to declare a variable

# ----
# Desktop app
# web app
# Database
# Network app
# Games
# Data analyse
# Machine Learning
# AI

# ------
# Features
# simple and easy
# 33 keywords

# --
# Free - u can customize also
# -
# High Level Prog lang - humans can understand
# -
# Dynamically Typed - not require to declare a variable
# ---------

# Flavors of python
# CPython
# Jython
# pypy - performance good
# Anaconda - handle big data
# -------

# Rules
# 0-9
# a-z
# A-Z
# _
# -------------
# 1Prashant = 10

# if = abc - false
# ---

# _======>private
# __=====>Strongly Private
# -------
# 33 reserved words

# True, False, None	 - 3
# and,or,not,is		-4
# if,else,elif		-3
# while,for,break,continue,return,in,yield - 7
# try,except,finally,raise,assert 	- 5
# import,from,as,class,def,pass,global,nonlocal,lamda,del,with -11
# -----------

# Python inbuilt fn
# print()
# type()
# id()
# ----
# 14 Data types-
# int
# float
# complex
# bool
# str
# bytes
# bytesarray
# range
# list
# tuple
# set
# frozenset
# dict
# None
# ----------

# 1. int
# 10, 20, 30
# 1000000000000000000000000000000
# --
# Decimal(10) - 0 to 9
# Binary(2) - 0 to 1
# Octal(8) - 0 to 7
# Hexa(16) - 0 to 9 - a to f
# -----
# a = 0b1111
# a = 0B1111
# a = 0o1111
# a = 0x1111
# -------------

# Base Conversion
# bin()
# oct()
# hex()
# -------

# 2. float
# x = 1.23
# ---

# 3. complex
# a+bj
# x=10+20j
# a - > real part
# b - > imaginary
# ------

# 4. bool
# True and False

# True+True = 2
# 1+0 = 1
# ----

# 5. str 
# index
# slice
# len(str)
# -----
# s = 'Rishab'
# s1 = "Prashant"
# -
# s='Rishab'
# s1="Prashant"

# s2= '''Prathmesh
#         Jadhav'''
# s3='''Hi, "Hello" good'''
# print(s3)
# ----
#    5432-1
# s='Bilal'
#    01234
# ------
# slice
# [begin:end:step]
# s='Rishab Rajput'
# --
# s='Rishab Rajput'
# # s[1:4]
# # s[:4]
# # s[:]
# # s[-1:-4]
# # s[-4:-1]
# # s[::2]
# s[::-1]
# ------------------------------------------------

# name1 = 'Ravi'
# name1*5
# ---
# name1 = 'Ravi '
# # name1*5
# len(name1)
# ---------------------

# Type Casting 
# int()
# float()
# complex()
# bool()
# str()
# -------
# # float(19)
# # float(10+5j)
# # complex(2)
# # int(2+3j)
# # bool(1)
# # str(10)
# ---------------

# d/f b/w Immutable and mutable
# Immutable - Non Changable
# Mutable - changable
# a = [1,2,3,4,5]
# a[1] = 6 - error
# a[1] = 6 - change
# ------------

# is operator

# x=10
# y=10
# x is y
# y is x
# ----
# x=257
# y=257
# # x is y
# y is x
# - ---
# x=8
# y=9
# # x is y
# y is x
# ---------

# bytes data type 
# immutable array

# x=[10,20,30]
# b=bytes(x)
# type(b)
# ----
# x=[10,20,30]
# b=bytes(x)
# # type(b)
# # type(x)
# # b[1] = 40
# for x in b:print(x)
# ----------

# bytearray data type - same as bytes 
# mutable 

# x=[10,20,30]
# b=bytearray(x)
# # type(b)
# # type(x)
# b[1] = 40
# for x in b:print(x)
# -----------

# list data type - represent []
# mutable

# l=[]
# pop
# remove
# append
# ------
# l=[]
# # type(l)

# l.append(10)
# l.append(20)
# l.append(30)
# l.append('Rishab')
# l.append('Prasang')
# # print(l)
# l.remove(10)
# # print(l)
# l.pop()
# ---
# one = ['b','d','a','x','t']
# one.sort()
# print(one)
# ------- 

# tuple - same as list 
# immutable 
# represent - ()

# t=(10,'Sourav',True,30)
# --- 
# t=(10,'Sourav',True,30)
# # t[1] = 'Abhinav'
# t[1:]
# # print(t)
# ---------------------

# range
# immutable 
# slicing allowed 

# range(end)
# # r = range(11)
# # r = range(11,16)
# r = range(5,51,5)
# # print(r)
# for i in r:print(i)
# -----

