import random
from datetime import datetime, timedelta


class Point:

    def __init__(self, timestamp: datetime, latitude: float, longitude: float):
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"{self.timestamp.isoformat()} ({round(self.latitude, 4)}, {round(self.longitude, 4)})"

class Route:

    def __init__(self):
        self.points = []

    def add(self, point: Point):
        self.points.append(point)

    def __repr__(self):
        return f"Route ({len(self.points)} segments):\n" + '\n'.join([f"#{i+1}: {p}" for i, p in zip(range(len(self.points)), self.points) ])



class GpsSensor:

    def __init__(self,
                 initial_timestamp: datetime = datetime(2025, 2, 18, 14, 0),
                 recording_delta: timedelta = timedelta(seconds=30),
                 start_latitude: float = 60.369270,
                 start_longitude: float = 5.349365):
        self.timestamp = initial_timestamp
        self.recording_delta = recording_delta
        self.latitude = start_latitude
        self.longitude = start_longitude

    def sample(self) -> Point:
        result = Point(self.timestamp, self.latitude, self.longitude)
        xmomentum = random.random() * 0.1 - 0.05
        ymomentum = random.random() * 0.1 - 0.05
        self.timestamp += self.recording_delta
        self.latitude += xmomentum
        self.longitude += ymomentum
        return result


def main():
    is_active = True
    sensor = GpsSensor()
    route = Route()
    while is_active:
        print("---- Bike Computer ----\nSelect option:\n1. Track route\n2.Show Route\n3.Quit\n")
        user_input = input(">>> ")
        if not user_input.isdigit() and int(user_input) in {1, 2, 3}:
            print(f"Unrecognized input: '{user_input}'")
        else:
            selected_option = int(user_input)
            if selected_option == 1:
                no_sample = int(input("How many segments do you want to track: "))
                for _ in range(no_sample):
                    route.add(sensor.sample())
                print(f"recorded {no_sample} segments")
            elif selected_option ==2:
                print(route)
            else:
                is_active = False
    print("shutting down")

if __name__ == "__main__":
    main()
