from typing import List 

class Solution:
    def robotSim(self, commands, obstacles):
        current_position = [0, 0]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # all the possible directions (north, east, south, west)
        current_direction = 0  # robot starts facing north
        max_distance = 0
        
        # Convert obstacles list to a set for faster lookups
        obstacle_set = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -1:  # Turn right 90 degrees
                current_direction = (current_direction + 1) % 4
            elif command == -2:  # Turn left 90 degrees
                current_direction = (current_direction + 3) % 4
            else:
                for _ in range(command):
                    next_position = [
                        current_position[0] + directions[current_direction][0],
                        current_position[1] + directions[current_direction][1]
                    ]
                    if tuple(next_position) not in obstacle_set:
                        current_position = next_position
                        # Calculate the squared distance from the origin
                        max_distance = max(max_distance, current_position[0] ** 2 + current_position[1] ** 2)
                    else:
                        break  # Stop moving in this direction if there's an obstacle
        
        return max_distance

commands = [4,-1,3]
obstacles = []
sol = Solution()
print(sol.robotSim(commands, obstacles))
        