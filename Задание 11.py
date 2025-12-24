import math


def calculate_travel_time(speed, diameter):
    """
    Рассчитывает время, необходимое роботу для объезда планеты по окружности.
    """
    if speed <= 0 or diameter <= 0:
        return "Скорость и диаметр должны быть положительными числами!"
    pi = 3.14159
    circumference = pi * diameter
    time = circumference / speed

    return time


robot_speed = 10
planet_diameter = 12742
result = calculate_travel_time(robot_speed, planet_diameter)
if isinstance(result, str):
    print(result)
else:
    print(f"Роботу потребуется {result:.2f} ч. чтобы объехать планету.")
