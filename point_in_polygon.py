def point_in_polygon(point, polygon):
    '''
    Args:
        point be a array of [x, y]
        polygon be a array of [x_1, y_1, x_2, y_2...x_n, y_n(x_1, y_1)]
        there may or may not be the ending head, this func will check and
        repair the polygon array.
    Return:
        True if the point in polygon else False
    '''
    # get x of i_th point
    def poly_x(i): return polygon[2*i]
    # get y of i_th point
    def poly_y(i): return polygon[2*i+1]
    # check if the polygon be a cycle, if true, repair for effiency
    if polygon[0] == polygon[-2] and polygon[1] == polygon[-1]:
        polygon = polygon[:-2]
    # get the length(how many slides) of the polygon.
    j = len(polygon) / 2 - 1
    # init x, y of the point and the nodes oddness.
    [x,y], odd_nodes = point, False
    # for each slide of the polygon, judge if the line go through it
    # the line is a line horizontal of point y
    for i in range(j+1):
        # check if the y coord if point is between the slide ends y(s)
        # and only consider the left part of the polygon
        if ((poly_x(i) <= x or poly_x(j) <= x) and ((poly_y(i) < y 
            and poly_y(j) >= y) or (poly_y(j) < y and poly_y(i) >= y))):
            if (poly_x(i) + (y - poly_y(i)) / (poly_y(j) 
                - poly_y(i)) * (poly_x(j) - poly_x(i))) < x:
                # if x pass the slide change the oddness
                odd_nodes = not odd_nodes
        # mv the j to current index to keep i, j specific a slide
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
