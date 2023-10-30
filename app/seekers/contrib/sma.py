import random
import time

class SMASeekerPrototype():
    def process(self):
        return {
            'events': [
                {
                    'timestamp': 1608249260,
                    'message': f'This is a test message {random.randrange(0, 10000000)}'
                }
            ]
        }
