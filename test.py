import math
import vector_angle
import azimuth

def cross_product(point1_x,point1_y,point2_x,point2_y,point3_x,point3_y):
    return (point3_x-point1_x) * (point1_y-point2_y) - (point1_x-point2_x) * (point3_y-point1_y)


coords = [[math.sqrt(3),-1],[0,0],[-math.sqrt(3),-1]]
radius = 1

alpha = azimuth.azimuthAngle(coords[1][0], coords[1][1], coords[0][0], coords[0][1])
delta = vector_angle.vector_angle(coords[0][0], coords[0][1], coords[1][0], coords[1][1], coords[2][0], coords[2][1])
print(alpha*180/math.pi,delta*180/math.pi)
l = cross_product( coords[1][0], coords[1][1], coords[0][0], coords[0][1], coords[2][0], coords[2][1])
print("l is "+str(l))
if l <0:
    startRadian = alpha + (3 * math.pi) / 2
    endRadian = alpha + (3 * math.pi) / 2 - delta
    print(startRadian * 180 / math.pi, endRadian * 180 / math.pi)
    gamma = -math.pi / 6
    phi = startRadian
    while  phi>= endRadian-0.00000000001:
        x = coords[1][0] + radius * math.cos(phi)
        y = coords[1][1] - radius * math.sin(phi)
        print([x,y])
        phi += gamma

