"""
Design a rate limiter

Functional:
1) Accept
2) Error Response
3) Rules
    - Capacity: 
    - time:
4) 
"""
from abc import ABC, abstractmethod
from enum import Enum
import time
from collections import defaultdict

class RuleEngine(ABC):
    def __init__(self,refill_rate,max_tokens):
        self.refill_rate = refill_rate
        self.max_tokens = max_tokens
        self.last_refill_time = time.time()

    @abstractmethod
    def process_request(self,userID):
        pass


class RequestStatus(Enum):
    SUCCESS = 1
    FAIL = 2

class TokenBucket(RuleEngine):
    def __init__(self,rate):
        super().__init__(rate,5)
        self.previous_time = 0
        self.user_bucket = defaultdict(int)
        
    def refill_tokens(self,user_id):
        now = time.time()
        if user_id not in self.user_bucket:
            self.user_bucket[user_id] = {
                'current_tokens': self.max_tokens,
                'last_refill_time': now
            }
        
        elapsed_time = now - self.user_bucket[user_id]["last_refill_time"]
        new_tokens = elapsed_time*self.refill_rate
        self.user_bucket[user_id]["current_tokens"] = min(
            new_tokens+self.user_bucket[user_id]["current_tokens"],
            self.max_tokens)
        self.user_bucket[user_id]["last_refill_time"] = now

    def process_request(self, user_id):
        self.refill_tokens(user_id)
        user_data = self.user_bucket[user_id]
        if user_data["current_tokens"] >=1:
            user_data["current_tokens"]-=1
            return True
        return False

class RateLimiterManager:
    _instance = None

    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance = super(RateLimiterManager,cls).__new__(cls)
        return cls._instance
    
    def __init__(self,rate):
        if not hasattr(self,"initialized"):
            self.timestamp = 0
            self.rule = TokenBucket(rate)
            self.initialized = True


    def allowRequest(self,user_id):
        status = self.rule.process_request(user_id)
        return status

class User:
    def __init__(self,name:str,id:int):
        self.name = name
        self.id = id

    def get_id(self):
        return self.id
    
if __name__ == "__main__":
    rate = 1 # 1 token per second
    client1 = User("ABC",1)
    client2 = User("CDA",2)

    rate_limiter_manager = RateLimiterManager(rate)

    for i in range(10):
        time.sleep(0.25)
        if(rate_limiter_manager.allowRequest(client1.get_id)):
            print(f"Request:{i+1} from {client1.name}: Allowed")
        else:
            print(f"Request:{i+1} from {client1.name}: Denied")