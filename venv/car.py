class Car:
    isStart=False

    def checkStatus(self):
        if self.isStart == False:
            print('请先启动车子')
        return self.isStart

    def go(self):
        if self.checkStatus()==False:
            return
        print('车子前进了')

    def back(self):
        if self.checkStatus()==False:
            return
        print('车子后退了')

    def stop(self):
        if self.checkStatus()==False:
            return
        print('车子暂停了')
    def start(self):
        if self.isStart==True:
            print('车子已经启动了')
            return
        self.isStart=True
        print('车子启动了')

class SKD(Car):
    def drive(self):
        if self.checkStatus() == False:
            return
        print('手动驾驶')
class TSL(Car):
    def drive(self):
        if self.checkStatus() == False:
            return
        print('自动驾驶')
