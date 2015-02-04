def point_in_polygon(point, polygon):
    def poly_x(i): return polygon[2*i]
    def poly_y(i): return polygon[2*i+1]
    if polygon[0] != polygon[-2] and polygon[1] != polygon[-1]:
        polygon.extend(polygon[:2])
    j = len(polygon) / 2 - 1
    [x,y], odd_nodes = point, False
    for i in range(j+1):
        if (((poly_y(i) < y and poly_y(j) >= y) or (poly_y(j) < y 
            and poly_y(i) >= y)) and (poly_x(i) <= x or poly_x(j) <= x)):
            if (poly_x(i) + (y - poly_y(i)) / (poly_y(j) 
                - poly_y(i)) * (poly_x(j) - poly_x(i))) < x:
                odd_nodes = not odd_nodes
        j = i
    return odd_nodes


if __name__ == '__main__':
    pl = [1,1,2,3,2,0,1,0.5,0,-1,0,-2,-1,1,-0.5,0.5]
#    pl = [1,0,0,-1,-1,0,0,1]
    import random
    pts = [[random.random()*8-4, random.random()*8-4]for i in range(100000)]
    pts = filter(lambda pt: point_in_polygon(pt, pl), pts)
    import matplotlib.pyplot as plt
    pt_xs, pt_ys = [], []
    for pt in pts:
        pt_xs.append(pt[0])
        pt_ys.append(pt[1])
    plt.scatter(pt_xs, pt_ys)
    plt.show()
