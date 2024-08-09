from core import PlayerControl, Player
from manager import AutoControls

ac = AutoControls()
pc = PlayerControl(ac)
p = Player()

while True:
    target_x = 286.25
    target_y = 114.30
    desired_angle = pc.calculate_rotation(
        p.position.x,
        p.position.y,
        target_x=target_x,
        target_y=target_y,
    )
    current_angle = pc.rotate_player(
        p.position.rx,
        desired_angle
    )
    pc.move_to_point(
        p.position.x,
        p.position.y,
        target_x=target_x,
        target_y=target_y,
        desired_angle=desired_angle
    )

