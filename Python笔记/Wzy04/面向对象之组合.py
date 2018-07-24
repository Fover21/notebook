# 组合: 给一个类的对象封装一个属性,这个属性是另一个类的对象.
class GameRole:
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def attack(self, p):
        p.hp = p.hp - self.ad
        print('%s 攻击 %s,%s 掉了%s血,还剩%s血' % (self.name, p.name, p.name, self.ad, p.hp))

    def armament_weapon(self, wea):
        self.wea = wea


class Weapon:
    def __init__(self, name, ad):
        self.name = name
        self.ad = ad

    def fight(self, p1, p2):
        p2.hp = p2.hp - self.ad
        print('%s 用%s打了%s,%s 掉了%s血,还剩%s血'
              % (p1.name, self.name, p2.name, p2.name, self.ad, p2.hp))


p1 = GameRole('盖伦', 20, 500)
p2 = GameRole('亚索', 50, 200)

axe = Weapon('倚天剑', 60)
broadsword = Weapon('屠龙刀', 100)

p1.attack(p2)  # 盖伦 攻击 亚索,亚索 掉了20血,还剩180血
p2.attack(p1)  # 亚索 攻击 盖伦,盖伦 掉了50血,还剩450血

p1.armament_weapon(axe)
p1.wea.fight(p1, p2)  # 盖伦 用倚天剑打了亚索,亚索 掉了60血,还剩120血
p2.armament_weapon(broadsword)
p2.wea.fight(p2, p1)  # 亚索 用屠龙刀打了盖伦,盖伦 掉了100血,还剩350血

注意：
	1.查询顺序：
		对象.属性：先从对象空间找，如果找不到，再从类空间找，再找不到，再从父类找。。。
		类名.属性：先从本类空间找，如果找不到，再从父类找，。。。

	2.对象与对象之间是互相独立的。
	3.通过类名可以直接更改本类中的静态变量值
	4.但是通过对象不能改变本类中的静态变量值，只能引用类中的静态变量。
	5.类名()产生了一个（含有类对象指针的）空间，所以，对象可以访问类中的静态变量和动态变量。