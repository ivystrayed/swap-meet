from .item import Item
class Electronics(Item):
    def __init__(self, category, condition):
        self.category = "Electronics"
        super().__init__(category, condition)
    def __str__(self):
        return "A gadget full of buttons and secrets."

