def point_vs_vector(point, vector):
    (ax, ay), (bx, by) = vector
    px, py = point
    cross = (bx - ax) * (py - ay) - (by - ay) * (px - ax)
    return (cross < 0) - (cross > 0)