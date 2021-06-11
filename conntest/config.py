import json
import os

PATH = '/Users/yifanwang/.config/conntest'
FILE = os.path.join(PATH, 'config.json')

class Config:
    def __init__(self):
        self.data = []
        self.load()

    def load(self):
        if not os.path.exists(PATH):
            os.mkdir(PATH)
        if not os.path.exists(FILE):
            self.data = [
                    'www.baidu.com',
                    'www.google.com',
                    'www.bilibili.com',
                    'www.github.com'
                ]
            self.save()
        with open(FILE, 'r') as f:
            self.data = json.load(f)['hostnames']

    def save(self):
        with open(FILE, 'w+') as f:
            f.write(json.dumps({
                'hostnames': self.data
            }))

    def add(self, item: str):
        if item not in self.data:
            self.data.append(item)
            self.save()
            return True
        else:
            return False

    def remove(self, item: str):
        if item in self.data:
            self.data.remove(item)
            self.save()
            return True
        else:
            return False

    def clear(self):
        self.data.clear()
        self.save()