import math
from loguru import logger

LEFT = 1
RIGHT = 2
UP = 3
OK = 0


def calculate_angle(origin_x: float, origin_y: float, destination_x: float, destination_y: float) -> float:
    angle = math.atan2(
        destination_y - origin_y,
        destination_x - origin_x,
    )
    return angle


def next_angle(current_rotation: float, angle_target: float) -> float:
    return abs(current_rotation - angle_target)


def angular_difference(current, target):
    # Calcula a diferença angular levando em conta o intervalo circular [-π, π]
    diff = target - current
    return normalize_angle(diff)


def normalize_angle(angle: float) -> float:
    while angle > math.pi:
        angle -= 2 * math.pi
    while angle < -math.pi:
        angle += 2 * math.pi
    return angle


def move_to_target(
        pos_x_current: float,
        pos_y_current: float,
        rotation_current: float,
        rotation_target: float,
        pos_x_destination: float,
        pos_y_destination: float
) -> int:
    destination_angle = calculate_angle(
        pos_x_current,
        pos_y_current,
        pos_x_destination,
        pos_y_destination,
    )

    angle_difference = math.hypot(
        rotation_current - rotation_target
    )

    logger.info(
        f"\ndestination_angle: {destination_angle}"
        f"\nrotation_current: {rotation_current}"
        f"\nangle_difference: {angle_difference}"
        f"\ndistance: {math.hypot(pos_x_destination - pos_x_current, pos_y_destination - pos_y_current)}"
    )

    if math.hypot(pos_x_destination - pos_x_current, pos_y_destination - pos_y_current) > 5.25:
        return UP

    if abs(angle_difference) > 0.02:
        if angle_difference > 0:
            return RIGHT
        else:
            return LEFT
    return 0
