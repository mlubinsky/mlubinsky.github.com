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

         
    us = mondict['us']    #raw MEMS readings [gyro, accl]
    us = us.clone().unsqueeze(0)  #raw MEMS readings, for instance torch.Size([1, 4200, 6]) 
    print('type of us:', type(us), "shape=", us.shape, "dtype=", us.dtype )        
    # type of us: <class 'torch.Tensor'> shape= torch.Size([1, 4200, 6]) dtype= torch.float64

    print(us)
"""    


tensor([[[ 1.7578e-01, -7.7148e-02, -6.8359e-02,  1.1914e-01,  7.8535e+00,
           2.9727e+00],
         [-1.1133e-01,  6.0059e-02, -5.0293e-02, -5.2734e-01,  7.9297e+00,
           4.9551e+00],
         [-8.7891e-03,  0.0000e+00, -3.0762e-02, -6.5039e-01,  9.0547e+00,
           6.0195e+00],
         ...,
         [ 8.7891e-03,  4.8828e-03,  1.6113e-02, -1.0547e-01,  7.5898e+00,
           6.4844e+00],
         [-2.1973e-02, -1.4648e-03,  1.4648e-03, -2.2070e-01,  7.7773e+00,
           6.0957e+00],
         [-3.0762e-02, -2.4414e-03, -1.4648e-03,  3.9062e-02,  7.3652e+00,
           6.8672e+00]]], dtype=torch.float64)
"""

print(network.eval())
"""
GyroNet_v1(
  (cnn): Sequential(
    (0): ReplicationPad1d((78, 0))
    (1): Conv1d(6, 16, kernel_size=(7,), stride=(1,))
    (2): BatchNorm1d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (3): GELU(approximate='none')
    (4): Dropout(p=0.2, inplace=False)
    (5): Conv1d(16, 32, kernel_size=(7,), stride=(1,), dilation=(4,))
    (6): BatchNorm1d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (7): GELU(approximate='none')
    (8): Dropout(p=0.2, inplace=False)
    (9): Conv1d(32, 64, kernel_size=(7,), stride=(1,), dilation=(4,))
    (10): BatchNorm1d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): GELU(approximate='none')
    (12): Dropout(p=0.2, inplace=False)
    (13): Conv1d(64, 128, kernel_size=(7,), stride=(1,), dilation=(4,))
    (14): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (15): GELU(approximate='none')
    (16): Dropout(p=0.2, inplace=False)
  )
  (rnn): LSTM(128, 14, num_layers=2, batch_first=True, dropout=0.2)
  (lin): Sequential(
    (0): Linear(in_features=14, out_features=14, bias=True)
    (1): Tanh()
  )
  (initprocesscov_net): InitProcessCovNet(
    (factor_initial_covariance): Linear(in_features=1, out_features=6, bias=False)
    (factor_process_covariance): Linear(in_features=1, out_features=6, bias=False)
    (tanh): Tanh()
  )
)
"""
        
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
