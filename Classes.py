class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return f'Point({self.x},{self.y})'

    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case, we chose the same representation as in __repr__'''
        return f'Point({self.x},{self.y})'

class Rectangle:
    def __init__(self, bottom_left, top_right, color):
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.color = color

    def __str__(self):
        return f"I am a {self.color} rectangle with bottom left corner at ({self.bottom_left.x}, {self.bottom_left.y}) and top right corner at ({self.top_right.x}, {self.top_right.y})." 

    def __eq__(self, other):
        return (isinstance(other, Rectangle) and
                self.bottom_left == other.bottom_left and
                self.top_right == other.top_right and
                self.color == other.color)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f"Rectangle({self.bottom_left}, {self.top_right}, '{self.color}')"

    def get_bottom_left(self):
        return self.bottom_left

    def get_top_right(self):
        return self.top_right

    def get_color(self):
        return self.color

    def reset_color(self, new_color):
        self.color = new_color

    def get_perimeter(self):
        width = abs(self.top_right.x - self.bottom_left.x)
        height = abs(self.top_right.y - self.bottom_left.y)
        return 2 * (width + height)

    def get_area(self):
        width = abs(self.top_right.x - self.bottom_left.x)
        height = abs(self.top_right.y - self.bottom_left.y)
        return width * height

    def move(self, dx, dy):
        self.bottom_left.move(dx, dy)
        self.top_right.move(dx, dy)

    def intersects(self, other):
        return not (self.top_right.x < other.bottom_left.x or
                    self.bottom_left.x > other.top_right.x or
                    self.top_right.y < other.bottom_left.y or
                    self.bottom_left.y > other.top_right.y)

    def contains(self, x, y):
        return (self.bottom_left.x <= x <= self.top_right.x and
                self.bottom_left.y <= y <= self.top_right.y)

class Canvas:
    def __init__(self):
        self.rectangles = []

    def __str__(self):
        return f"Canvas: {len(self.rectangles)} Rectangles"

    def __eq__(self, other):
        return isinstance(other, Canvas) and self.rectangles == other.rectangles

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f"Canvas({self.rectangles})"

    def add_one_rectangle(self, rectangle):
        if isinstance(rectangle, Rectangle):
            self.rectangles.append(rectangle)

    def count_same_color(self, color):
        return sum(1 for rectangle in self.rectangles if rectangle.get_color() == color)

    def total_perimeter(self):
        return sum(rectangle.get_perimeter() for rectangle in self.rectangles)

    def min_enclosing_rectangle(self):
        if not self.rectangles:
            return None

        min_x = min(rectangle.get_bottom_left().x for rectangle in self.rectangles)
        max_x = max(rectangle.get_top_right().x for rectangle in self.rectangles)
        min_y = min(rectangle.get_bottom_left().y for rectangle in self.rectangles)
        max_y = max(rectangle.get_top_right().y for rectangle in self.rectangles)

        bottom_left = Point(min_x, min_y)
        top_right = Point(max_x, max_y)

        return Rectangle(bottom_left, top_right, "Red") 

    def common_point(self):
        if len(self.rectangles) < 2:
            return False

        for i in range(len(self.rectangles)):
            for j in range(i + 1, len(self.rectangles)):
                if not self.rectangles[i].intersects(self.rectangles[j]):
                    return False

        return True

    def __len__(self):
        return len(self.rectangles)
        