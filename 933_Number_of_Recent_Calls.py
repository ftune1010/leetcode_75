from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.requests.append(t)
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)
        

if __name__ == "__main__":
    obj = RecentCounter()
    
    print(obj.ping(1) == 1)
    print(obj.ping(2) == 2)
    print(obj.ping(3001) == 3)
    print(obj.ping(3002) == 3)