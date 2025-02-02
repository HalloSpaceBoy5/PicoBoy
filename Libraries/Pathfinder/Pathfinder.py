from heapq import heappop, heappush



    
class Pathfinder:

        
    def Find_Path(moveablelocs, start, end):
        def heuristic(a, b):
            # Manhattan distance
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        open_set = []
        heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristic(start, end)}
        
        while open_set:
            _, current = heappop(open_set)
            
            if current == end:
                return Pathfinder.reconstruct_path(came_from, current)
            
            neighbors = [((current[0] - 1, current[1]), 0),
                         ((current[0] + 1, current[1]), 1),
                         ((current[0], current[1] - 1), 2),
                         ((current[0], current[1] + 1), 3)]
            
            for neighbor, direction in neighbors:
                if neighbor in moveablelocs:
                    tentative_g_score = g_score[current] + 1
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                        heappush(open_set, (f_score[neighbor], neighbor))
        
        return []

    def reconstruct_path(came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

    
