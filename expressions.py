class Expression:
    def __init__(self, name, lex=140, ley=80, rex=280, rey=80):
        self.name = name
        self.left_eye_x = lex
        self.left_eye_y = ley
        self.right_eye_x = rex
        self.right_eye_y = rey
    
    def getName(self):
        return self.name
    
    def getCoords(self):
        return [self.left_eye_x, self.left_eye_y, 
                self.right_eye_x, self.right_eye_y]
    
# Idle
IDLE = Expression("Idle")

# Look Left
LOOK_LEFT = Expression("Look_Left", lex=20, rex=160)

# Look Right
LOOK_RIGHT = Expression("Look_Right", lex=260, rex=400)

# Look Up
LOOK_UP = Expression("Look_Up", ley=20, rey=20)

# Look Down
LOOK_DOWN = Expression("Look_Down", ley=140, rey=140)

# Look Top Left
LOOK_TOP_LEFT = Expression("Look_Top_Left", lex=20, ley=20, rex=160, rey=20)

# Look Top Right
LOOK_TOP_RIGHT = Expression("Look_Top_Right", lex=260, ley=20, rex=400, rey=20)

# Look Bottom Left
LOOK_BOTTOM_LEFT = Expression("Look_Bottom_Left", lex=20, ley=140, rex=160, rey=140)

# Look Bottom Right
LOOK_BOTTOM_RIGHT = Expression("Look_Bottom_Right", lex=260, ley=140, rex=400, rey=140)