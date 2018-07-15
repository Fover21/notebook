Python 的 not and or 运算

首先要做一些准备知识：
	1，优先级:逻辑型 < 测试型 < 关系型 < 算数型
	2，逻辑型:or < and < not
	3，在python中，0，‘’，[],{},(),None 为假(False),其余任何东西都为真(True).

接下来就介绍他们的运算：
	x and y : 如果x为真, 则y决定了结果, 返回y.
			  如果x为假, 则x决定了结果, 返回x.

	x or y  : 如果x为假, 则y决定了结果, 返回y.
			  如果x为真, 则x决定了结果, 返回x.

	  not   : 返回表达式结果相反的值.

接下来举一些例子来解释：
	1, 3 and 0   ->  0   (因为x为真y决定了结果，所以结果为3)
	2, 3 or 0    ->  3   (因为x为真x决定了结果，所以结果为3)
	3, [] and 3  ->  []  (因为[]为假x决定了结果，所以结果为[])
	4, None or 3 ->  3   (因为None为假y决定结果，所以结果为3)
	5, 1 or 2 and 3  ->1 (因为and的优先级比or大，所以先算2 and 3 结果我3，再算1 or 3结果为1)
	6, 1<2 and 3>4 or not 1==1 or {} ->{} 
		(根据优先级先算not 1==1 得到1<2 and 3>4 or False or {}
		 再算and得到 True and False or False or {}---->False or False or {}
		 再算or 得到False or {}---->{})
   
   口诀：
    and 前真得后，前假得前 
     or 前真得前，前假得后
代码得多敲，不能光看。