包是一种通过使用‘.模块名’来组织python模块名称空间的方式。

１. 无论是import形式还是from...import形式，凡是在导入语句中（而不是在使用时）遇到带点的，
都要第一时间提高警觉：这是关于包才有的导入语法

2. 包是目录级的（文件夹级），文件夹是用来组成py文件（包的本质就是一个包含__init__.py文件的目录）

3. import导入文件时，产生名称空间中的名字来源于文件，import 包，产生的名称空间的名字同样来源于文件，
即包下的__init__.py，导入包本质就是在导入该文件

强调：

　　1）在python3中，即使包下没有__init__.py文件，import 包仍然不会报错，而在python2中，包下一定要有该文件，否则import 包报错

　　2）创建包的目的不是为了运行，而是被导入使用，记住，包只是模块的一种形式而已，包即模块


注意：
1.关于包相关的导入语句也分为import和from ... import ...两种，但是无论哪种，无论在什么位置，在导入时都必须遵循一个原则：
凡是在导入时带点的，点的左边都必须是一个包，否则非法。可以带有一连串的点，如item.subitem.subsubitem,但都必须遵循这个原则。

2.对于导入后，在使用时就没有这种限制了，点的左边可以是包,模块，函数，类(它们都可以用点的方式调用自己的属性)。

3.对比import item 和from item import name的应用场景：
如果我们想直接使用name那必须使用后者。