import math


def vector_angle(x1,y1,x2,y2,x3,y3):
    vector1_x = x2-x1
    vector1_y = y2-y1
    vector2_x = x3-x2
    vector2_y = y3-y2
    vector1_mod = math.sqrt(vector1_x**2 + vector1_y**2)
    vector2_mod = math.sqrt(vector2_x**2 + vector2_y**2)
    dot_product = vector1_x * vector2_x + vector2_y * vector1_y
    cos_deta = dot_product / vector1_mod / vector2_mod

    #return math.acos(cos_deta)*180/math.pi
    return math.acos(cos_deta)
    #print(dot_product)
    #print(math.acos(cos_deta) *180 / math.pi)


#vector_angle(-7,-7,0,0,-0.866,0.5)
