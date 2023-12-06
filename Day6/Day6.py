
def main(filename):
    with open(filename) as file:
        lines = file.read().split('\n')
        times = list(map(int, lines[0].split(":")[1].split()))
        distances = list(map(int, lines[1].split(":")[1].split()))
        race_time = int("".join(str(time) for time in times))
        race_distance = int("".join(str(distance) for distance in distances))


        ways_to_win = 0

        for seconds in range(0, race_time+1):
            seconds_after_pressing = race_time - seconds
            initial_speed = seconds
            distance = initial_speed * seconds_after_pressing
            if distance > race_distance:
                ways_to_win += 1

        return ways_to_win

