import random
import time

class TestSeekerPrototype():
    def __init__(self, data):
        self.data = data

    def process(self):
        time.sleep(10)
        rnd = random.randrange(0, 10000000)
        print(self.data)

        return {
            'events': [
                {
                    'timestamp': 1608249260,
                    'message': f'This is a test Event message {rnd}'
                }
            ]
        }
