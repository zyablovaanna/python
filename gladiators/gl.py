import random
N, M = 30, 2

def luck(N, M):
        def decorator(func):
            def wrapper(*a,**kw):
                result = func(*a, **kw)
                if random.randint(1, 100) <= N:
                    result = result * M;
                return result;
            return wrapper
        return decorator;

class Gladiator:
    def __init__(self, name, health, damage):
        self.__name = name;
        self.__health = health;
        self.__damage = damage;
    
    def __str__(self):
        return f"Гладиатор {self.__name}, Здоровье: {self.__health}, Урон {self.__damage} "

    @property
    def name(self):
        return self.__name;
    
    @property
    def health(self):
        return self.__health;
    @health.setter
    def health(self, health):
        self.__health = health;
     
    @property
    @luck(N,M)
    def damage(self):
        return self.__damage;    

    def take_damage(self, d):
        self.__health -= d;
        if (self.__health < 0):
         self.__health = 0;