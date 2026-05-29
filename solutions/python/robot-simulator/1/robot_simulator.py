"""Robot simulator"""
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
RIGHT = "R"
LEFT = "L"
ADVANCE = "A"

ADVANCE_DIRECTION = [(0,1),(1,0),(0,-1),(-1,0)]


class Robot:
    """Robot simulator"""
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, commands):
        for movement in commands:
            if movement == RIGHT:
                self.direction = (self.direction + 1) % 4
            elif movement == LEFT:
                self.direction = (self.direction - 1) % 4
            elif movement == ADVANCE:
                x_pos, y_pos = self.coordinates
                dx, dy = ADVANCE_DIRECTION[self.direction]
                self.coordinates = (x_pos + dx, y_pos + dy)

    