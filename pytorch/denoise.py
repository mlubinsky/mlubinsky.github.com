Is tensorflow-probability uses tf_keras or tensorflow.keras?


This is a great question that gets at the heart of how TensorFlow Probability integrates with Keras!

TensorFlow Probability (TFP) primarily uses tf_keras under the hood.   

Here's a breakdown of why and what it means:

tf_keras: This is the Keras implementation that's tightly integrated with TensorFlow. It's the version of Keras that you get when you install TensorFlow.   
tensorflow.keras: This is also a valid way to import Keras, and it often points to the same underlying implementation as tf_keras. 
However, tf_keras is generally preferred within the TensorFlow ecosystem, especially when working with TFP.

Why tf_keras is important for TFP:

Compatibility: TFP is built on top of TensorFlow, and tf_keras is the most natural way to use Keras within that context. 
It ensures that TFP components work seamlessly with Keras layers and models.
Internal Dependencies: As you saw in the error message you encountered, TFP has internal dependencies on tf_keras. 
It relies on specific functionalities and structures within tf_keras to implement its probabilistic layers and other features.
What this means for you:

Import Keras correctly: When working with TFP, it's best to import Keras using import tf_keras as keras or from tf_keras import layers, etc.
  This makes it clear that you're using the TensorFlow-integrated Keras.
Version Compatibility: Ensure that your tf_keras version is compatible with both your TensorFlow and TensorFlow Probability versions. 
  This is crucial to avoid the kind of "Arg specs do not match" errors you encountered.
In summary:

While tensorflow.keras might work in some cases, 
sticking with tf_keras is the recommended and more reliable approach when using TensorFlow Probability. 
It ensures compatibility and avoids potential issues arising from different Keras implementations.


pip install tensorflow-probability==0.18.0

Failed to import TF-Keras. Please note that TF-Keras is not installed by default when you install TensorFlow Probability. This is so that JAX-only users do not have to install TensorFlow or TF-Keras. To use TensorFlow Probability with TensorFlow, please install the tf-keras or tf-keras-nightly package.
This can be be done through installing the tensorflow-probability[tf] extra.


Traceback (most recent call last):
  File "/root/MICHAEL/SPOTBOT/convert.py", line 15, in <module>
    from onnx_tf.backend import prepare
  File "/usr/local/lib/python3.11/site-packages/onnx_tf/__init__.py", line 1, in <module>
    from . import backend
  File "/usr/local/lib/python3.11/site-packages/onnx_tf/backend.py", line 28, in <module>
    from onnx_tf.common.handler_helper import get_all_backend_handlers
  File "/usr/local/lib/python3.11/site-packages/onnx_tf/common/handler_helper.py", line 3, in <module>
    from onnx_tf.handlers.backend import *  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/onnx_tf/handlers/backend/bernoulli.py", line 2, in <module>
    from tensorflow_probability import distributions as tfd
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/__init__.py", line 22, in <module>
    from tensorflow_probability.python import *  # pylint: disable=wildcard-import
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/__init__.py", line 152, in <module>
    dir(globals()[pkg_name])  # Forces loading the package from its lazy loader.
    ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/internal/lazy_loader.py", line 60, in __dir__
    module = self._load()
             ^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/internal/lazy_loader.py", line 40, in _load
    self._on_first_access()
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/__init__.py", line 79, in _validate_tf_environment
    import tf_keras  # pylint: disable=unused-import
    ^^^^^^^^^^^^^^^







Traceback (most recent call last):
  File "/root/MICHAEL/SPOTBOT/convert.py", line 15, in <module>
    from onnx_tf.backend import prepare
  File "/usr/local/lib/python3.11/site-packages/onnx_tf/__init__.py", line 1, in <module>
    from . import backend
  File "/usr/local/lib/python3.11/site-packages/onnx_tf/backend.py", line 28, in <module>
    from onnx_tf.common.handler_helper import get_all_backend_handlers
  File "/usr/local/lib/python3.11/site-packages/onnx_tf/common/handler_helper.py", line 3, in <module>
    from onnx_tf.handlers.backend import *  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/onnx_tf/handlers/backend/bernoulli.py", line 2, in <module>
    from tensorflow_probability import distributions as tfd
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/__init__.py", line 20, in <module>
    from tensorflow_probability import substrates
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/substrates/__init__.py", line 17, in <module>
    from tensorflow_probability.python.internal import all_util
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/__init__.py", line 138, in <module>
    dir(globals()[pkg_name])  # Forces loading the package from its lazy loader.
    ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/internal/lazy_loader.py", line 57, in __dir__
    module = self._load()
             ^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/internal/lazy_loader.py", line 40, in _load
    module = importlib.import_module(self.__name__)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/experimental/__init__.py", line 31, in <module>
    from tensorflow_probability.python.experimental import bijectors
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/experimental/bijectors/__init__.py", line 17, in <module>
    from tensorflow_probability.python.bijectors.ldj_ratio import forward_log_det_jacobian_ratio
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/bijectors/__init__.py", line 19, in <module>
    from tensorflow_probability.python.bijectors.absolute_value import AbsoluteValue
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/bijectors/absolute_value.py", line 19, in <module>
    from tensorflow_probability.python.bijectors import bijector
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/bijectors/bijector.py", line 26, in <module>
    from tensorflow_probability.python.internal import batch_shape_lib
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/internal/batch_shape_lib.py", line 23, in <module>
    from tensorflow_probability.python.internal import prefer_static as ps
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/internal/prefer_static.py", line 368, in <module>
    ones_like = _copy_docstring(tf.ones_like, _ones_like)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/tensorflow_probability/python/internal/prefer_static.py", line 85, in _copy_docstring
    raise ValueError(
ValueError: Arg specs do not match: original=FullArgSpec(args=['input', 'dtype', 'name', 'layout'], varargs=None, varkw=None, defaults=(None, None, None), kwonlyargs=[], kwonlydefaults=Nne, annotations={}), new=FullArgSpec(args=['input', 'dtype', 'name'], varargs=None, varkw=None, defaults=(None, None), kwonlyargs=[], kwonlydefaults=None, annotations={}), fn=<function oes_like_v2 at 0x7f71264fb880>





pip install tf-keras
Installing collected packages: numpy, tensorboard, ml-dtypes, keras, tensorflow, tf-keras
  Attempting uninstall: numpy
    Found existing installation: numpy 2.1.3
    Uninstalling numpy-2.1.3:
      Successfully uninstalled numpy-2.1.3
  Attempting uninstall: ml-dtypes
    Found existing installation: ml_dtypes 0.5.1
    Uninstalling ml_dtypes-0.5.1:
      Successfully uninstalled ml_dtypes-0.5.1
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
tf-nightly 2.19.0.dev20250207 requires ml-dtypes<1.0.0,>=0.5.1, but you have ml-dtypes 0.4.1 which is incompatible.
Successfully installed keras-3.8.0 ml-dtypes-0.4.1 numpy-2.0.2 tensorboard-2.18.0 tensorflow-2.18.0 tf-keras-2.18.0

root@spotace:~/MICHAEL/SPOTBOT/src# pip list | grep keras
keras                        3.8.0
keras-nightly                3.8.0.dev2025021403
tf_keras                     2.18.0
root@spotace:~/MICHAEL/SPOTBOT/src# pip list | grep tensor
safetensors                  0.5.2
tensorboard                  2.18.0
tensorboard-data-server      0.7.2
tensorflow                   2.18.0
tensorflow-addons            0.23.0
tensorflow-io-gcs-filesystem 0.37.1
tensorflow-probability       0.25.0


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


import onnx
from onnx_tf.backend import prepare
#exit(0)
import tensorflow as tf

"""
2025-02-17 20:55:46.526763: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:467] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739854546.550773  830338 cuda_dnn.cc:8670] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
E0000 00:00:1739854546.557949  830338 cuda_blas.cc:1407] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
W0000 00:00:1739854546.576786  830338 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.
W0000 00:00:1739854546.576839  830338 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.
W0000 00:00:1739854546.576844  830338 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.
W0000 00:00:1739854546.576847  830338 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.
2025-02-17 20:55:46.582478: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX512F FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
Traceback (most recent call last):
  File "/root/MICHAEL/SPOTBOT/convert.py", line 15, in <module>
    from onnx_tf.backend import prepare
  File "/usr/local/lib/python3.11/site-packages/onnx_tf/__init__.py", line 1, in <module>
    from . import backend
  File "/usr/local/lib/python3.11/site-packages/onnx_tf/backend.py", line 28, in <module>
    from onnx_tf.common.handler_helper import get_all_backend_handlers
  File "/usr/local/lib/python3.11/site-packages/onnx_tf/common/handler_helper.py", line 3, in <module>
    from onnx_tf.handlers.backend import *  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/onnx_tf/handlers/backend/bernoulli.py", line 2, in <module>
    from tensorflow_probability import distributions as tfd
ModuleNotFoundError: No module named 'tensorflow_probability'
"""



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
   sample_inputs = torch.randn(1, 4200, 6, dtype=torch.float64)
   sample_inputs = (sample_inputs,)

   print("before convert")
   edge_model = ai_edge_torch.convert(network.eval(),sample_inputs)
"""
/usr/local/lib/python3.11/site-packages/torch/export/_unlift.py:75: UserWarning: Attempted to insert a get_attr Node with no underlying reference in the owni                              ng GraphModule! Call GraphModule.add_submodule to add the necessary submodule, GraphModule.add_parameter to add the necessary Parameter, or nn.Module.registe                              r_buffer to add the necessary buffer
  getattr_node = gm.graph.get_attr(lifted_node)
/usr/local/lib/python3.11/site-packages/torch/fx/graph.py:1801: UserWarning: Node lifted_tensor_0 target lifted_tensor_0 lifted_tensor_0 of  does not referen                              ce an nn.Module, nn.Parameter, or buffer, which is what 'get_attr' Nodes typically target
  warnings.warn(

The error message suggests that Torch Export (FX-based tracing) is having trouble handling a tensor reference inside your model. This often happens when:

A tensor inside your model is not properly registered as a buffer (register_buffer) or parameter (nn.Parameter).
Your model contains in-place operations or non-traceable Python logic that torch.export cannot capture correctly.
Possible Fixes
1️⃣ Check if Any Constants Should Be Registered as Buffers
If your model has tensors created as attributes (e.g., self.some_tensor = torch.tensor([...])), you need to register them as a buffer:

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.some_tensor = torch.tensor([1.0, 2.0, 3.0])  # ⚠️ This causes issues
        self.register_buffer("some_tensor", self.some_tensor)  # ✅ Fix by registering it as a buffer
👉 Fix: Look inside your model and replace such tensor assignments with self.register_buffer(name, tensor).

2️⃣ Convert Any Constants to nn.Parameter (if Trainable)
If the tensor should be trainable, use nn.Parameter:

self.some_tensor = nn.Parameter(torch.tensor([1.0, 2.0, 3.0]))
3️⃣ Ensure sample_inputs Has the Correct Type
Before conversion, make sure sample_inputs is in a tuple and has requires_grad=False:

sample_inputs = (torch.randn(1, 4200, 6, dtype=torch.float64, requires_grad=False),)
4️⃣ Convert Model to float32 (Some Exporters Don't Support float64)
If your model was trained in float64 (double precision), try converting it to float32 before exporting:

model = model.to(torch.float32)
sample_inputs = (sample_inputs[0].to(torch.float32),)  # Ensure inputs match
edge_model = ai_edge_torch.convert(model.eval(), sample_inputs)
"""

    edge_model.export('michael.tflite')
    exit(0) ### EXIT
        
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
