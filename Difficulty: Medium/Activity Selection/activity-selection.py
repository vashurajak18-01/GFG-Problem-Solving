class Meeting:
    def __init__ (self, start , finish, position):
        self.start = start
        self.finish = finish
        self.position = position

class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        #code here
        meet = [Meeting(start[i], finish[i],i+1) 
                for i in range(len(start))]

        meet.sort(key = lambda x : (x.finish, x.start))

        count = 1
        lastTime  = meet[0].finish 

        for i in range(1, len(start)):
            if meet[i].start > lastTime:
                count +=1
                lastTime = meet[i].finish

        return count