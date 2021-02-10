class Game:
    def __init__(self, player):
        self.player = player
        self.__life = 100 #私有属性，外部无法直接访问

    def get_life_value(self):
        print("%s当前的生命值还有%d" % (self.player, self.__life))

    def attacked(self):
        self.__life -= 20
        print('%s被攻击了，生命值-20'%self.player)
        self.__restore_life() #被动技能，被攻击时恢复10点生命
    
    def __restore_life(self): #私有方法，外部无法访问
        self.__life += 10
        print('%s恢复10点生命值'%self.player)



p1 = Game('Hammer')
#print(p1.__life)直接访问私有属性会报错
#p1.__restore_life() 外部访问私有方法会报错
p1.attacked()
p1.get_life_value()

#可以通过以下形式访问私有属性或方法
#实例._类名+方法(属性)
p1._Game__restore_life()