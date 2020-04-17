class IDigging:

    def __init__(self):
        self.digging_speed = 0
        self.maximum_depth = 0

    def dig(self):
        print(f"{self.name} digs")