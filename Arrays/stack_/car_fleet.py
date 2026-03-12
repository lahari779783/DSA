"""
Car Fleet

Problem:
Return the number of car fleets that will arrive at the destination.

Approach:
Sort cars by position descending.
Calculate time to reach target.
If a car takes longer than the previous fleet, it forms a new fleet.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def car_fleet(target, position, speed):
    cars = list(zip(position, speed))
    cars.sort(reverse=True)

    fleets = 0
    last_time = 0

    for pos, spd in cars:
        time = (target - pos) / spd

        if time > last_time:
            fleets += 1
            last_time = time

    return fleets


if __name__ == "__main__":
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]

    print(car_fleet(target, position, speed))