def minArrows(points):
    n = len(points)
    #if No balloons return 0
    if n==0:
        return 0

    #minimum arrow needed
    arrow = 1
    
    #sort the list by balloons end points.
    points = (sorted(points,key=lambda point:point[1]))
    #initalize with first end point of balloon at index 0.
    end = points[0][1]

    #check for all balloons if end[0] > start[1] of balloons then both balloons can brust by same arrow.
    # otherwise new arrow is needed and end is to be updated.
     
    for i in range(1,n):
        if points[i][0]>end:
            arrow +=1
            end = points[i][1]

    return arrow

points = [[10,16],[2,8],[1,6],[7,12]]
print(minArrows(points))