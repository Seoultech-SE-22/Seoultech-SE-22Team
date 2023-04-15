import time

class Timer:
    def __init__(self, time):
        self.time = time
        
    # def countdown(self):
    #     while self.time > 0:
    #         print(self.time)
    #         self.time -= 1
    #         time.sleep(1)
    #     print("Time's up!")
    
    def update(self):
        self.time -= 1
        time.sleep(1)

    

    def reset(self, num):
        self.time = num



#timer = Timer2(15)
#timer.countdown()
