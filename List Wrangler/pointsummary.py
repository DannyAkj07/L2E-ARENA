def point_summary(point):
    summary = {
        "x": point[0],
        "y": point[1],
        "manhattan": abs(point[0]) + abs(point[1])}

    return summary


print(point_summary([-3,4]))
