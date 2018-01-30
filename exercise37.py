# coding=utf-8
# 复习符号
#
#
# 关键字
# KEYWORD	DESCRIPTION	EXAMPLE
# and	逻辑与	True and False == False
# as	with-as语句的一部分	with X as Y: pass
# assert	声明	assert False, "Error!"
# break	停止整个循环	while True: break
# class	定义一个类	class Person(object)
# continue	停止这一次循环，但继续下一次循环	while True: continuev
# def	定义一个函数	def X(): pass
# del	从字典中删除	del X[Y]
# elif	Else if 条件	if: X; elif: Y; else: J
# else	Else 条件	if: X; elif: Y; else: J
# except	如果捕获异常，执行该代码块	except ValueError, e: print e
# exec	将字符串作为Python代码执行	exec 'print "hello"'
# finally	不管是否有异常，finally代码块都执行	finally: pass
# for	for循环	for X in Y: pass
# from	从某一模块中引入特定部分	import X from Y
# global	定义一个全局变量	global X
# if	If 条件	if: X; elif: Y; else: J
# import	引入一个模块到当前模块	import os
# in	for循环的一部分/ 测试X in Y.	for X in Y: pass / 1 in [1] == True
# is	类似==，判断相等	1 is 1 == True
# lambda	创建一个无名函数	s = lambda y: y ** y; s(3)
# not	逻辑非	not True == False
# or	逻辑或	True or False == True
# pass	该代码块为空	def empty(): pass
# print	打印一个字符串	print 'this string'
# raise	代码出错时，抛出一个异常	raise ValueError("No")
# return	退出函数并返回一个返回值	def X(): return Y
# try	尝试代签代码块，有异常则进入except代码块	try: pass
# while	While循环	while X: pass
# with	一个变量的别名	with X as Y: pass
# yield	暂停， 返回给调用者	def X(): yield Y; X().next()


# 数据类型
# 针对每一种数据类型，都举出一些例子来，例如针对string，你可以举出一些字符串，针对 number，你可以举出一些数字。
#
# TYPE	DESCRIPTION	EXAMPLE
# True	True 布尔值.	True or False == True
# False	False 布尔值.	False and True == False
# None	表示 "nothing" 或者"no value".	x = None
# strings	字符串，储存文本信息	x = "hello"
# numbers	储存整数	i = 100
# floats	储存小数	i = 10.389
# lists	储存某种东西的列表	j = [1,2,3,4]
# dicts	储存某些东西的键值对	e = {'x': 1, 'y': 2}


# 字符串转义序列
# 对于字符串转义序列，你需要在字符串中应用它们，确认自己清楚地知道它们的功能。
#
# ESCAPE	DESCRIPTION
# \\	斜线
# \'	单引号
# \"	双引号
# \a	Bell
# \b	退格
# \f	Formfeed
# \n	换行
# \r	Carriage
# \t	Tab键
# \v	垂直的tab


# 字符串格式化
# ESCAPE	DESCRIPTION	EXAMPLE
# %d	格式化整数 (不包含浮点数).	"%d" % 45 == '45'
# %i	与%d相同	"%i" % 45 == '45'
# %o	8进制数字	"%o" % 1000 == '1750'
# %u	负数	"%u" % -1000 == '-1000'
# %x	小写的十六进制数字	"%x" % 1000 == '3e8'
# %X	大写的十六进制数字	"%X" % 1000 == '3E8'
# %e	小写 'e'的指数标记	"%e" % 1000 == '1.000000e+03'
# %E	大写 'e'的指数标记	"%E" % 1000 == '1.000000E+03'
# %f	浮点数	"%f" % 10.34 == '10.340000'
# %F	与%f相同	"%F" % 10.34 == '10.340000'
# %g	%f 或者 %e中较短的一个	"%g" % 10.34 == '10.34'
# %G	%F 或者 %E中较短的一个	"%G" % 10.34 == '10.34'
# %c	字符格式化	"%c" % 34 == '"'
# %r	类型格式化	"%r" % int == "<type 'int'>"
# %s	字符串格式	"%s there" % 'hi' == 'hi there'
# %%	表示百分号%	"%g%%" % 10.34 == '10.34%'


# 操作符
# 有些操作符号你可能还不熟悉，不过还是一一看过去，研究一下它们的功能，如果你研究不出来也没关系，记录下来日后解决。
#
# OPERATOR	DESCRIPTION	EXAMPLE
# +	加	2 + 4 == 6
# -	减	2 - 4 == -2
# *	乘	2 * 4 == 8
# **	幂乘	2 ** 4 == 16
# /	除	2 / 4.0 == 0.5
# //	整除，得到除法的商。	2 // 4.0 == 0.0
# %	模除，返回除法的余数。	2 % 4 == 2
# <	小于	4 < 4 == False
# >	大于	4 > 4 == False
# <=	小于等于	4 <= 4 == True
# >=	大于等于	4 >= 4 == True
# ==	等于，比较操作对象是否相等。	4 == 5 == False
# !=	不等于	4 != 5 == True
# <>	不等于	4 <> 5 == True
# ( )	括号	len('hi') == 2
# [ ]	列表括号	[1,3,4]
# { }	字典括号	{'x': 5, 'y': 10}
# @	装饰符	@classmethod
# ,	逗号	range(0, 10)
# :	冒号	def X():
# .	Dot	self.x = 10
# =	赋值等于	x = 10
# ;	分号	print "hi"; print "there"
# +=	加等于	x = 1; x += 2
# -=	减等于	x = 1; x -= 2
# *=	乘等于	x = 1; x *= 2
# /=	除等于	x = 1; x /= 2
# //=	整除等于	x = 1; x //= 2
# %=	模除等于	x = 1; x %= 2
# **=	幂乘等于	x = 1; x **= 2
