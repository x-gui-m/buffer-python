import vector_angle
import azimuth
import math

buffer_coords = []
axial_coords = [[326,18],[67,76],[200,200]]

#axial_coords = [[20,20],[80,40],[120,150],[200,100],[260,50],[500,300],[700,100]]

v_radius = 10


#def get_buffer_point(axial_coords,radius):
def get_buffer_point(axial_coords):
    if len(axial_coords) <1:
        return 0

   # v_radius = radius
    elif len(axial_coords) <2:
        get_endpoint_right_buffer_point(True, axial_coords[0], axial_coords[1])
        get_endpoint_right_buffer_point(False, axial_coords[0], axial_coords[1])
        axial_coords = list(reversed(axial_coords))
        get_endpoint_right_buffer_point(True, axial_coords[0], axial_coords[1])
        get_endpoint_right_buffer_point(False, axial_coords[0], axial_coords[1])
        return

    for i in range(len(axial_coords)):
        print("this is the "+str(i)+" point")
        if i == 0:
            tag = True
            get_endpoint_right_buffer_point(tag,axial_coords[0],axial_coords[1])
            continue
        if i == (len(axial_coords)-1):
            tag = False
            get_endpoint_right_buffer_point(tag,axial_coords[-1],axial_coords[-2])
            continue
        get_right_buffer_point(axial_coords[i],axial_coords[i-1],axial_coords[i+1])

    axial_coords = list(reversed(axial_coords))
    print(axial_coords)
    for i in range(len(axial_coords)):
        if i == 0:
            tag = True
            get_endpoint_right_buffer_point(tag, axial_coords[0], axial_coords[1])
            continue
        if i == (len(axial_coords) - 1):
            tag = False
            get_endpoint_right_buffer_point(tag, axial_coords[-1], axial_coords[-2])
            continue
        get_right_buffer_point(axial_coords[i], axial_coords[i - 1], axial_coords[i + 1])


def get_endpoint_right_buffer_point(tag,point1,point2):

    if tag:
        alpha = azimuth.azimuthAngle(point1[0],point1[1],point2[0],point2[1])
        startRadian =  alpha +math.pi
        endRadian =  alpha + (1 * math.pi)/2
    else:
        alpha = azimuth.azimuthAngle(point2[0], point2[1], point1[0], point1[1])
        startRadian = alpha + (1 * math.pi) / 2
        endRadian = alpha + 0 *math.pi /2
    get_buffer_coord_by_radian(point1,startRadian,endRadian,v_radius)


def get_right_buffer_point(point1,point2,point3):
    #point1为中间点，point2为前一点，point3为后一点
    alpha = azimuth.azimuthAngle(point1[0],point1[1],point3[0],point3[1])
    delta = vector_angle.vector_angle(point2[0],point2[1],point1[0],point1[1],point3[0],point3[1])
    l = cross_product(point1[0],point1[1],point2[0],point2[1],point3[0],point3[1])
    print("l = "+str(l))
    if l >0:
        alpha = azimuth.azimuthAngle(point1[0],point1[1],point2[0],point2[1])
        startRadian = alpha + (3 * math.pi) / 2
        endRadian = alpha + (3 * math.pi) / 2 - delta
        get_buffer_coord_by_radian(point1,startRadian,endRadian,v_radius)
    if l < 0:
        '''
        alpha1 = azimuth.azimuthAngle(point1[0],point1[1],point2[0],point2[1])
        print(alpha*180/math.pi,alpha1*180/math.pi)
        if alpha<alpha1:
            beta = alpha + (math.pi - delta)/2
        else:
        '''
        beta = alpha + (math.pi - delta)/2

        x = point1[0] + v_radius /math.sin((math.pi - delta) / 2) * math.cos(beta)
        y = point1[1] - v_radius /math.sin((math.pi - delta) / 2) * math.sin(beta)
        print(alpha*180/math.pi,((math.pi - delta) / 2)*180/math.pi,beta*180/math.pi,v_radius /math.sin((math.pi - delta) / 2))
        buffer_coords.append([x,y])

def get_buffer_coord_by_radian(point,startRadian,endRadian,radius):
    gamma = -math.pi / 6
    phi = startRadian
    while  phi>= endRadian-0.00000000001:
        x = point[0] + radius * math.cos(phi)
        y = point[1] - radius * math.sin(phi)
        buffer_coords.append([x,y])
        phi += gamma


def cross_product(point1_x,point1_y,point2_x,point2_y,point3_x,point3_y):
    return (point1_x-point2_x) * (point3_y-point1_y) - (point3_x-point1_x) * (point1_y-point2_y)


get_buffer_point(axial_coords)
print(buffer_coords)
print(len(buffer_coords))
with open(r"C:\Users\lenovo\Desktop\buffer\buffer-test\buffer-test\buffered.js",'w') as f:
    f.write('var buffer_result = '+str(buffer_coords))
    f.close()