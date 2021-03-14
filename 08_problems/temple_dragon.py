#!/usr/bin/env python3

class Item:
    BLOCKED=0
    FREE=1

    LINK_NONE=0
    LINK_UP=1
    LINK_RIGHT=2
    LINK_DOWN=4
    LINK_LEFT=8

    LINK_LEVEL2_UP=16
    LINK_LEVEL2_RIGHT=32
    LINK_LEVEL2_DOWN=64
    LINK_LEVEL2_LEFT=128

    ROTATION_0=0
    ROTATION_90=1
    ROTATION_180=2
    ROTATION_270=3

    def __init__(self,position2d,positions,level1_avail,level2_avail,links,rotation):
        self.position2d = position2d
        self.positions = positions
        self.level1 = level1_avail
        self.level2 = level2_avail
        self.links = links

        self.rotate(rotation)

    def rotate(self,rotation):
        pass

class Dragon(Item):
    def __init__(self,position2d,rotation):
        # on a single line
        dragon_position=[(0,0),(0,1),(0,2)]
        ground_level=[self.BLOCKED, self.BLOCKED, self.BLOCKED]
        first_level=[self.BLOCKED,self.FREE,self.BLOCKED]
        links=[self.LINK_NONE,self.LINK_NONE,self.LINK_NONE]
        super(Dragon,self).__init__(position2d,dragon_position,ground_level,first_level,links,rotation)

class TempleWithTwoDoors(Item):
    def __init__(self,position2d,rotation):
        temple_position=[(0,0)]
        ground_level=[self.BLOCKED]
        first_level=[self.BLOCKED]
        links=[ self.LINK_RIGHT | self.LINK_DOWN ]
        super(TempleWithTwoDoors,self).__init__(position2d,temple_position,ground_level,first_level,links,rotation)

class TempleWithBridge1(Item):
    def __init__(self,position2d,rotation):
        temple_position=[(0,0),(1,0)]
        ground_level=[self.BLOCKED,self.FREE]
        first_level=[self.BLOCKED,self.BLOCKED]
        links=[ self.LINK_RIGHT, self.LINK_LEVEL2_DOWN ]
        super(TempleWithBridge1,self).__init__(position2d,temple_position,ground_level,first_level, links,rotation)

class TempleWithBridge2(Item):
    def __init__(self,position2d,rotation):
        temple_position=[(0,0),(0,1)]
        ground_level=[self.BLOCKED,self.FREE]
        first_level=[self.BLOCKED,self.BLOCKED]
        links=[ self.LINK_DOWN, self.LINK_LEVEL2_RIGHT ]
        super(TempleWithBridge2,self).__init__(position2d,temple_position,ground_level,first_level, links,rotation)

class HalfCircleWithRightTurn(Item):
    def __init__(self,position2d,rotation):
        position=[(0,0),(0,1),(1,1)]
        level1 = [self.BLOCKED,self.BLOCKED,self.BLOCKED]
        level2 = [self.FREE,self.FREE,self.FREE]
        links=[self.LINK_DOWN,self.LINK_NONE,self.LINK_DOWN]
        super(HalfCircleWithRightTurn,self).__init__(position2d,position,level1,level2,links,rotation)

class HalfCircleWithLeftTurn(Item):
    def __init__(self,position2d,rotation):
        position=[(0,0),(0,1),(1,0)]
        level1 = [self.BLOCKED,self.BLOCKED,self.BLOCKED]
        level2 = [self.FREE,self.FREE,self.FREE]
        links=[self.LINK_NONE,self.LINK_DOWN,self.LINK_DOWN]
        super(HalfCircleWithLeftTurn,self).__init__(position2d,position,level1,level2,links,rotation)

class HalfCircleWithStairs(Item):
    def __init__(self,position2d,rotation):
        position=[(0,0),(0,1),(1,1)]
        level1 = [self.BLOCKED,self.BLOCKED,self.FREE]
        level2 = [self.FREE,self.FREE,self.BLOCKED]
        links=[self.LINK_DOWN,self.LINK_NONE,self.LINK_LEVEL2_DOWN]
        super(HalfCircleWithStairs,self).__init__(position2d,position,level1,level2,links,rotation)

class RightTurn(Item):
    def __init__(self,position2d,rotation):
        position=[(0,0),(1,0)]
        level1 = [self.BLOCKED,self.BLOCKED]
        level2 = [self.FREE,self.FREE]
        links=[self.LINK_RIGHT,self.LINK_DOWN]
        super(RightTurn,self).__init__(position2d,position,level1,level2,links,rotation)

class RightTurnWithStairs(Item):
    def __init__(self,position2d,rotation):
        position=[(0,0),(1,0),(0,1)]
        level1 = [self.BLOCKED,self.FREE,self.BLOCKED]
        level2 = [self.FREE,self.BLOCKED,self.FREE]
        links=[self.LINK_NONE,self.LINK_LEVEL2_RIGHT,self.LINK_DOWN]
        super(RightTurnWithStairs,self).__init__(position2d,position,level1,level2,links,rotation)

class LeftTurnWithStairs(Item):
    def __init__(self,position2d,rotation):
        position=[(0,0),(1,0),(1,1)]
        level1 = [self.FREE,self.BLOCKED,self.BLOCKED]
        level2 = [self.BLOCKED,self.FREE,self.FREE]
        links=[self.LINK_LEVEL2_LEFT,self.LINK_NONE,self.LINK_DOWN]
        super(LeftTurnWithStairs,self).__init__(position2d,position,level1,level2,links,rotation)

class DoubleCurveWithStairs(Item):
    def __init__(self,position2d,rotation):
        position=[(0,0),(0,1),(1,1)]
        level1 = [self.FREE,self.BLOCKED,self.BLOCKED]
        level2 = [self.BLOCKED,self.FREE,self.FREE]
        links=[self.LINK_LEVEL2_UP,self.LINK_NONE,self.LINK_DOWN]
        super(DoubleCurveWithStairs,self).__init__(position2d,position,level1,level2,links,rotation)

// table is 5 x 5