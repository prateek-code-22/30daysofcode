#Problem: https://leetcode.com/problems/robot-bounded-in-circle/
#Robot is facing NORTH direction and given a set of instructions steps for robot to follow.
#find out if robot path make a circle or loop ? 

def isRobotBounded(s: str) -> bool:
    posX = 0 
    posY = 0  

    #robot facing NORTH direction
    dirX = 0
    dirY = 1

    for steps in s:
        #move straight 1 unit 
        if steps == 'G':
            posX , posY = posX+dirX ,posY+dirY

        #direction change to left so anticlock wise 90 degree.
        elif steps == 'L':
            dirX , dirY = -dirY , dirX

        #direction change to right so clockwise 90 degree.
        elif steps == 'R':
            dirX , dirY = dirY, -dirX

    #if starting and end position are same than loop is formed OR directions is different.
    if (posX,posY)==(0,0) or (dirX,dirY)!=(0,1):
        return True
    else:
        return False


s = "GGLLGG"
print(isRobotBounded(s))
