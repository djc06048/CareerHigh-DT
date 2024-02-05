import sys, math
def calculate_min_distance(points):
    min_dis=sys.maxsize
    for i in range(0,len(points)-1):
        first=points[i]
        for j in range(i+1,len(points)):
            second=points[j]
            dis=math.sqrt((first[0]-second[0])**2 +(first[1]-second[1])**2)
            if(min_dis>dis):
                a=first
                b=second


    return [first,second]
print(calculate_min_distance([[1,1],[2,3],[4,0],[3,-1]]))
