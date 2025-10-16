class SeyHello:
    def __init__(self, target = "World"):
        self.target = target

    def say(self):
        print(f"Hello, {self.target}!!")

if __name__ == '__main__':
    app = SeyHello()
    app.say()
    app = SeyHello("Someone")
    app.say()