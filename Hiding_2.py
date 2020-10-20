def advice(agents, n):
    safest_spaces = []
    high_distance = 0
    for x in range(0,n):
        for y in range(0,n):
            low_dist = None
            for agent in agents:
                if (x,y) in agents:
                    low_dist = 0
                    break
                dist = abs((x - agent[0])) + abs((y - agent[1] ))
                if dist == 0:
                    low_dist = 0
                    break
                if low_dist == None or dist < low_dist:
                    low_dist = dist

            if low_dist > high_distance:
                safest_spaces = [(x,y)]
                high_distance = low_dist
            elif low_dist == high_distance and low_dist != 0:
                safest_spaces.append((x,y))
            else:
                pass
    return safest_spaces




advice([(0, 0), (1, 5), (5, 1)], 6)