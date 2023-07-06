import math
## t اینجا فاصله یا همون 
## رو محاسبه میکنیم
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
## تابع اصلی که به روش بک ترک مساله را حل میکند
def solve_orienteering(instance_file):
    ## در این قسمت ورودی ها رو میگیریم ############################
    points = []
    with open(instance_file, 'r') as file:
        lines = file.readlines()
        Tmax, P = map(int, lines[0].split())
        for line in lines[1:]:
            x, y, s = map(float, line.split())
            points.append((x, y, s))

    num_points = len(points)
    scores = [0] * num_points
    visited = [False] * num_points
    path = [0]  # Start with the first point
    
    # print(points)
    #################################################################
    ## پیاده سازی بک ترکینگ ##########################################
    def backtrack(current_point, time, total_score):
        if time > Tmax:
            return

        max_score = 0
        next_point = None
        ##  یک دور همه نود های دیگه رو چک میکنیم تا بهترین امتیاز ممکن رو پیدا کنیم
        for i in range(num_points):
            if not visited[i]:
                distance = euclidean_distance(
                    points[current_point][0], points[current_point][1],
                    points[i][0], points[i][1]
                )
                # print(i)
                # print(time+distance)
                # چک کردن شروط مساله
                if time + distance <= Tmax and points[i][2] > max_score:
                    # print('Vared shod')
                    max_score = points[i][2]
                    # print('max')
                    # print(max_score)
                    next_point = i
                    # print('next Point')
                    # print(time+distance)
        if next_point is None:
            # print('cost')
            # print(time)
            return

        path.append(next_point)
        visited[next_point] = True
        scores[next_point] = max_score
        total_score += max_score
        
        backtrack(next_point, time + euclidean_distance(
            points[current_point][0], points[current_point][1],
            points[next_point][0], points[next_point][1]
        ), total_score)




    backtrack(0, 0, 0)
    path.append(num_points - 1)
    # print(scores)
    scores[num_points - 1] = points[num_points - 1][2]
    # print(scores)
    total_score = sum(scores)
    solution = {
        'path': path,
        'total_score': total_score
    }
    return solution

# Usage
instance_file = 'instance.txt'
solution = solve_orienteering(instance_file)


print(f"Path: {solution['path']}")
print(f"Total Score: {solution['total_score']}")
