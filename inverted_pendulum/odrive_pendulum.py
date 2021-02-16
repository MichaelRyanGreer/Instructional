import numpy as np

import odrive
from odrive.enums import *

import time

odrv0 = odrive.find_any()

def wait_for_odrive():

    while (odrv0.axis1.current_state != 1):

        time.sleep(0.1)

    return


odrv0.axis1.motor.config.current_lim = 9.0

odrv0.axis1.controller.config.vel_limit = 20.0

odrv0.axis1.motor.config.calibration_current = 4.0

odrv0.config.brake_resistance = 2

odrv0.axis1.motor.config.pole_pairs = 7

odrv0.axis1.motor.config.torque_constant = 0.020674999803304672

odrv0.axis1.motor.config.motor_type = 0

odrv0.axis1.encoder.config.use_index = True


#odrv0.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE

wait_for_odrive()

odrv0.axis1.requested_state = AXIS_STATE_ENCODER_INDEX_SEARCH

wait_for_odrive()

odrv0.axis1.requested_state = AXIS_STATE_ENCODER_OFFSET_CALIBRATION

print("Calibration complete")


for i in range(10):

    time.sleep(0.1)
    print(odrv0.axis1.encoder.pos_estimate)

wait_for_odrive()

#odrv0.axis1.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL
#odrv0.axis1.controller.input_velocity = 0.0

odrv0.axis1.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL
odrv0.axis1.controller.input_torque = 0.0

odrv0.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

for i in np.linspace(0, 8*np.pi, 1400):

    tau = 0.01 if np.sin(i) > 0 else -0.01

    odrv0.axis1.controller.input_torque = tau
    time.sleep(0.001)

odrv0.axis1.requested_state = AXIS_STATE_IDLE
