# cd /home/spotbot/denoising_inference_Oct072024/
#  cat denoising_inference.py
""" Module to run sequences for testing """

import os
import numpy as np
import torch
import sys
import pandas as pd
from typing import Dict
from pathlib import Path

from src.networks import GyroNet_v1
from src.utils import pload, pdump


base_dir = os.path.dirname(os.path.realpath(__file__))

def run_sequence(
        trained_network_directory: str,
        input_filename: str,
        network_class=GyroNet_v1,
        perform_denoising: bool = True,
) -> Dict:

    # Get neural network object and load weights
    net_params = pload(trained_network_directory, 'net_params.p')
    network = network_class(**net_params)
    path_weights = os.path.join(trained_network_directory, 'weights_pre_training_epoch_2000.pt')          #weights.pt
    weights = torch.load(path_weights, map_location=torch.device('cpu'))
    network.load_state_dict(weights)
    network.eval()

    # Fetch subsequence data
    input_suffix = Path(input_filename).suffix
    if input_suffix == ".p":
        mondict = pload(input_filename)
    elif input_suffix == ".csv":
        timestamp_accel_gyro_x_y_zs = pd.read_csv(input_filename)
        df = pd.read_csv(input_filename, names=["timestamp_ms", "gyro_x", "gyro_y", "gyro_z", "accel_x", "accel_y", "accel_z"], header=None)
        timestamps = df.pop("timestamp_ms")
        print(df)
        mondict = {"us": torch.tensor(df.values)}
    else:
        print("Error unsupported input filetype {}".format(input_suffix))
        return None

    print(mondict)
    us = mondict['us']    #raw MEMS readings [gyro, accl]
    us = us.clone().unsqueeze(0)  #raw MEMS readings, for instance torch.Size([1, 4200, 6])

    with torch.no_grad():
        net_outputs = network(us)
        if len(net_outputs) == 1:
            ys = net_outputs
        elif len(net_outputs) == 3:
            ys = net_outputs[0]
        if perform_denoising:
            us_fix = ys[:, :, :6] * us[:, :, :6] - ys[:, :, 6:12]
        else:
            us_fix = us

        if input_suffix == ".csv":
            data = us_fix[0].cpu().numpy()
            df = pd.DataFrame({"timestamp_ms": timestamps, "gyro_x": data[:, 0], "gyro_y": data[:, 1], "gyro_z": data[:, 2], "accel_x": data[:, 3], "accel_y": data[:, 4], "accel_z": data[:, 5]})
            filename_path = Path(input_filename)
            parent = filename_path.parent
            stem = filename_path.stem
            with open(os.path.join(parent, stem + "_denoised.csv"), "w", newline='\n') as out_f:
                df.to_csv(out_f, index=False, header=False)

        result = {
            'us': us[0].cpu().numpy(),
            'us_fix': us_fix[0].cpu().numpy(),
        }

        return result


if __name__ == '__main__':
    # Run a single sequence with a single network:
    trained_network_name = '2024_09_25_14_29_26'
    result = run_sequence(
        trained_network_directory=os.path.join(base_dir, 'results/MEMS', trained_network_name),
        input_filename=sys.argv[1]
    )
    print(result)
