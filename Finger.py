# class Clock(object):
# 	def __init__(self, time):
# 		self.time = time
# 	def print_time(self, time):
# 		print(time)
#
# clock = Clock('5:30')
# clock.print_time('10:30')

class Weird(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return x
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y

X = 7
Y = 8
w1 = Weird(X, Y)
print(w1.getX())
