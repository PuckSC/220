class Button:
    def __init__(self, shape, label):
        self.text = label
        self.shape = shape

    def get_label(self):
        return self.text

    def draw(self, win):
        button = self.shape
        label = self.text
        button.draw(win)
        label.draw(win)

    def undraw(self):
        button = self.shape
        label = self.text
        button.undraw()
        label.undraw()

    def is_clicked(self, point):
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        return p1.getX() < point.getX() < p2.getX() and p1.getY() < point.getY() < p2.getY()

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text = label
