https://proproprogs.ru/

JAX for PyTorch users
https://cloud.google.com/blog/products/ai-machine-learning/guide-to-jax-for-pytorch-developers

https://pytorchstepbystep.com/

https://habr.com/ru/articles/870426/

### GyroNet
https://github.com/mbrossar/denoise-imu-gyro/blob/master/src/networks.py
```
#$ file net_params.p
# net_params.p: data
# $ file weights_combination_epoch_3380.pt
# weights_combination_epoch_3380.pt: Zip archive data, at least v?[0] to extract

Python pickle (for net_params.p):
Since the .p extension is common for pickle files, try this in a Python interpreter:

import pickle
try:
    with open("net_params.p", "rb") as f:  # "rb" for read binary
        data = pickle.load(f)
        print(type(data))  # See what kind of Python object it is
        # print(data)       # If it's not too large, you can try printing it
except pickle.UnpicklingError as e:
    print(f"Error unpickling: {e}")
except Exception as e:
    print(f"Other error: {e}")

If this works without errors, you've likely confirmed it's a pickle file. The print(type(data)) will tell you what kind of Python object is stored (e.g., a dictionary, a list, etc.).

ZIP Archive (for weights.pt):

List contents: You can use the unzip command to see what's inside the ZIP archive:
unzip -l weights.pt

.data - folder
data   - folder
byteorder - file (little
data.pkl - file
version   - file  (3)



cat extract_pt.py
import torch
fname="/home/spotbot/denoising_inference_Oct072024/results/MEMS/2024_09_25_14_29_26/weights_combination_epoch_3380.pt"
try:
   model = torch.load(fname)  # PyTorch will handle the ZIP automatically
   print(type(model))  # This should tell you the type of saved object (e.g., a model)
   print(model.keys()) # If it's a state_dict, this will list the layers
   for k, v in model.items():
       print(k)
except Exception as e:
        print(f"Error loading PyTorch model: {e}")

mean_u
std_u
gyro_std
cnn.1.weight
cnn.1.bias
cnn.2.weight
cnn.2.bias
cnn.2.running_mean
cnn.2.running_var
cnn.2.num_batches_tracked
cnn.5.weight
cnn.5.bias
cnn.6.weight
cnn.6.bias
cnn.6.running_mean
cnn.6.running_var
cnn.6.num_batches_tracked
cnn.9.weight
cnn.9.bias
cnn.10.weight
cnn.10.bias
cnn.10.running_mean
cnn.10.running_var
cnn.10.num_batches_tracked
cnn.13.weight
cnn.13.bias
cnn.14.weight
cnn.14.bias
cnn.14.running_mean
cnn.14.running_var
cnn.14.num_batches_tracked
rnn.weight_ih_l0
rnn.weight_hh_l0
rnn.bias_ih_l0
rnn.bias_hh_l0
rnn.weight_ih_l1
rnn.weight_hh_l1
rnn.bias_ih_l1
rnn.bias_hh_l1
lin.0.weight
lin.0.bias


Your PyTorch model file appears to be a dictionary of tensors and parameters
rather than a full model object.
The key reason your file (model.pt) is not a full model object but rather a state_dict
(a dictionary of tensors and parameters) is the way PyTorch models are typically saved.
Let me explain:

1) What You Loaded (model.pt) is a state_dict
Your code:

import torch
fname = "model.pt"
model = torch.load(fname)  
print(type(model)) 

for k, v in model.items():
       print(k)
prints a list of parameter names like:


mean_u
std_u
gyro_std
cnn.1.weight
cnn.1.bias
...
This means the loaded model is a dictionary (state_dict), not an actual PyTorch nn.Module model.

Evidence That It’s a state_dict:
The type(model) will print <class 'collections.OrderedDict'>, meaning it's a dictionary.
The output contains parameter names (cnn.1.weight, rnn.weight_ih_l0, etc.), which are only the model's weights and not the architecture.
A full model object would allow calling model.forward(input_tensor), but your model.pt does not.

2) What is a state_dict?
A state_dict is a dictionary mapping layer names to their learned parameters (weights and biases). It does not include the model architecture itself.

Example:

{
    "cnn.1.weight": tensor(...),  # Convolution layer weights
    "cnn.1.bias": tensor(...),    # Convolution layer bias
    "rnn.weight_ih_l0": tensor(...),  # RNN input-hidden weights
    ...
}
Since it only contains parameters, PyTorch cannot reconstruct the model without separately defining its architecture.

 Why Isn’t It a Full Model Object?
A full model object (i.e., an nn.Module) includes:

Model architecture: The layers (nn.Conv2d, nn.Linear, nn.LSTM, etc.)
Model parameters: The trained weights and biases
Your file only contains the parameters, not the architecture.

 How to Convert It Back to a Full Model Object?
To use the model, you need to define the architecture and load the state_dict into it.

Example:

import torch
import torch.nn as nn

# Define the original model class
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
        )
        self.rnn = nn.LSTM(32, 64, num_layers=2)
        self.lin = nn.Linear(64, 10)

    def forward(self, x):
        x = self.cnn(x)
        x, _ = self.rnn(x)
        x = self.lin(x)
        return x

# Create model instance
model = MyModel()

# Load the state_dict
state_dict = torch.load("model.pt")
model.load_state_dict(state_dict)

# Set model to evaluation mode
model.eval()

print(model)  # Now you have a full model object!

```
### How to Make full model
```
Yes, you cannot directly convert your model.pt (which is just a state_dict) to .tflite (LiteRT format)
 because TFLite requires the full model architecture and weights, not just the weights.
However, you can still convert it to .tflite by following these steps:

Steps to Convert model.pt (state_dict) to .tflite
Since your model.pt only contains weights, you need to:

Define the original PyTorch model architecture.
Load the state_dict into the model.
Export the full model to ONNX.
Convert ONNX to TFLite.

Step 1: Define the Model Class
+++++++++++++++++++++++++++++++
Since your model.pt does not contain the model architecture, you must define it manually.
Example (modify this to match your actual model):

import torch
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
        )
        self.rnn = nn.LSTM(32, 64, num_layers=2, batch_first=True)
        self.lin = nn.Linear(64, 10)

    def forward(self, x):
        x = self.cnn(x)
        x, _ = self.rnn(x)
        x = self.lin(x)
        return x

# Create model instance
model = MyModel()

Step 2: Load the state_dict
+++++++++++++++++++++++++++
Now, load the weights from model.pt:

state_dict = torch.load("model.pt")
model.load_state_dict(state_dict)
model.eval()  # Set model to evaluation mode

Step 3: Convert to ONNX
+++++++++++++++++++++++++++++++
Now that you have a complete model, export it to ONNX:

dummy_input = torch.randn(1, 3, 224, 224)  # Adjust input shape as needed

torch.onnx.export(
    model,
    dummy_input,
    "model.onnx",
    export_params=True,
    opset_version=11,
    input_names=["input"],
    output_names=["output"]
)
Step 4: Convert ONNX to TensorFlow SavedModel
+++++++++++++++++++++++++++++++++++++++++++++
To convert the ONNX model to TensorFlow format, install onnx2tf:

pip install onnx2tf

Then, convert:

onnx2tf -i model.onnx -o model_tf

Step 5: Convert to TFLite
++++++++++++++++++++++++++
Use TensorFlow’s TFLite Converter:

import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model("model_tf")
tflite_model = converter.convert()

with open("model.tflite", "wb") as f:
    f.write(tflite_model)

```

### How to Convert the Model to LiteRT Format (.tflite)?
```
To convert a PyTorch model to TFLite (LiteRT format), follow these steps:

Step 1: Convert to TorchScript
-------------------------------
Convert the model to TorchScript (either tracing or scripting):

import torch
model = MyModel()  # Load the model class
model.load_state_dict(torch.load("model.pt"))
model.eval()

# Convert to TorchScript
scripted_model = torch.jit.trace(model, torch.randn(1, C, H, W))  # Adjust input size
scripted_model.save("model_scripted.pt")

Step 2: Convert to ONNX
------------------------
Export the scripted model to ONNX format:

torch.onnx.export(
    scripted_model,
    torch.randn(1, C, H, W),  # Adjust input shape
    "model.onnx",
    export_params=True,
    opset_version=11,
    input_names=["input"],
    output_names=["output"]
)

Step 3: Convert ONNX to TFLite
------------------------------
Use TensorFlow’s tf.lite.TFLiteConverter:

import tensorflow as tf
import onnx
import tf2onnx

# Load ONNX model
onnx_model = onnx.load("model.onnx")

# Convert ONNX to TFLite
converter = tf.lite.TFLiteConverter.from_saved_model("model.onnx")
tflite_model = converter.convert()

# Save the TFLite model
with open("model.tflite", "wb") as f:
    f.write(tflite_model)

Step 4: Verify the TFLite Model
--------------------------------
Run inference on the converted model:

interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print(f"Input details: {input_details}")
print(f"Output details: {output_details}")
--------
Extract (if needed): If you want to examine the individual files, you can extract them:
unzip weights.pt
This will extract the contents into the current directory.  Look for files with extensions like .pth, .bin, or other model-related files.

PyTorch Specific (for weights.pt):

Even though it's a ZIP, it's very likely a PyTorch save file.  Try loading it directly in PyTorch:

import torch
try:
    model = torch.load("weights.pt")  # PyTorch will handle the ZIP automatically
    print(type(model))  # This should tell you the type of saved object (e.g., a model)
    # print(model.keys()) # If it's a state_dict, this will list the layers
except Exception as e:
    print(f"Error loading PyTorch model: {e}")


This is the most direct way to confirm if it's a PyTorch model.
 
PyTorch save format: PyTorch often uses ZIP archives to store multiple components of a model
(weights, architecture, optimizer state, etc.).
The torch.load() function handles these ZIP files transparently.
By combining the file command with the Python code snippets above,
you should be able to determine the exact nature of both files.
The PyTorch approach for weights.pt is the most likely to succeed if it's indeed a PyTorch model file.
```
#### You can visualize it in a few ways:
```
A. Print Model Structure and Weights
Since your model file is a state_dict, you can inspect the shape of each parameter:

import torch

fname = "model.pt"
state_dict = torch.load(fname)

# Print details of model weights
for k, v in state_dict.items():
    print(f"{k}: {v.shape}")

B. Load It into a PyTorch Model (If You Have the Model Class)
If you have access to the original PyTorch model class, you can load the state_dict:

import torch
from my_model_definition import MyModel  # Replace with your actual model class

model = MyModel()
model.load_state_dict(torch.load("model.pt"))
model.eval()

print(model)  # View model architecture

C. Visualize with torchsummary
If you have the model class, install torchsummary and run:

from torchsummary import summary

summary(model, input_size=(C, H, W))  # Replace C, H, W with actual input shape

D. Visualize Model Graph Using torchviz
If you can pass a sample input, use torchviz:

from torchviz import make_dot

x = torch.randn(1, C, H, W)  # Replace with actual input shape
y = model(x)

make_dot(y, params=dict(model.named_parameters())).render("model_graph", format="png")
```
### Model viewer

https://netron.app/

```
While there isn't a single, dedicated "PyTorch model viewer" that directly opens .ph files,
there are several excellent tools and techniques you can use
to visualize and inspect your PyTorch models:

1. Netron:

Versatile and widely used: Netron is a free, open-source viewer that supports a wide variety of model formats,
including ONNX (Open Neural Network Exchange).   
Convert to ONNX: PyTorch models can be easily exported to the ONNX format.
Once you have the ONNX file, you can open it in Netron to visualize the model's
architecture, layers, connections, and even see the weights and biases (if included).   
How to use it:
Install Netron: Download and install Netron from their website (https://netron.app/).
Export to ONNX: In your PyTorch code, use torch.onnx.export() to export your model to an ONNX file.
Open in Netron: Open the ONNX file in Netron.

2. TensorBoard:

Part of the TensorFlow ecosystem: While primarily associated with TensorFlow, TensorBoard
can also be used with PyTorch.   
Visualize graphs: TensorBoard can visualize the structure of your PyTorch model,
showing the flow of data through the different layers.   
How to use it:
Install TensorBoard: pip install tensorboard
Use SummaryWriter:
In your PyTorch code, use torch.utils.tensorboard.SummaryWriter to add the model graph to a log directory.
Launch TensorBoard: Run tensorboard --logdir <log_directory> to start TensorBoard and view the visualization in your browser.

3. Torchviz:

PyTorch-specific: Torchviz is a Python library specifically designed for visualizing PyTorch models.   
Generate graph visualizations:
It can create visualizations of the computational graph of your model, showing the operations and tensors involved.
How to use it:
Install Torchviz: pip install torchviz graphviz (you'll also need Graphviz)
Use make_dot(): In your PyTorch code, import make_dot() from torchviz and use it to generate a visualization of your model.

4. print(model):

Simple but effective: In many cases, simply printing your model object (print(model)) will give you a decent overview of its architecture.
Limitations: This method might not be ideal for very complex models, as the output can be quite long and difficult to read.

Which tool to choose?

Netron: A good general-purpose viewer for various model formats, including ONNX. It's great for getting a quick understanding of the model's structure.   
TensorBoard: Useful for visualizing the model graph and also offers other features for monitoring training progress.

Torchviz: Specifically designed for PyTorch, can be helpful for understanding the computational graph.   
print(model): A quick and easy way to see the basic structure of the model.
Important Note:

The .ph extension is not a standard PyTorch extension. It's likely that the file was saved with a custom extension.
However, if it's a saved PyTorch model, you should still be able to load it using torch.load() and then use the visualization tools mentioned above to inspect it.

```

### pip index versions torch
```

WARNING: pip index is currently an experimental command. It may be removed/changed in a future release without prior warning.
torch (2.5.1)
Available versions: 2.5.1, 2.5.0, 2.4.1, 2.4.0, 2.3.1, 2.3.0, 2.2.2, 2.2.1, 2.2.0, 2.1.2, 2.1.1, 2.1.0, 2.0.1, 2.0.0, 1.13.1, 1.13.0, 1.12.1, 1.12.0, 1.11.0
  INSTALLED: 1.12.1
  LATEST:    2.5.1
```

### brew info pytorch
```
==> pytorch: stable 2.5.1 (bottled)
Tensors and dynamic neural networks
https://pytorch.org/
Not installed
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/p/pytorch.rb
License: BSD-3-Clause
==> Dependencies
Build: cmake ✘, ninja ✘, python@3.13 ✘
Required: abseil ✘, eigen ✘, libuv ✘, libyaml ✔, numpy ✘, openblas ✘, protobuf ✘, pybind11 ✘, sleef ✘, libomp ✘
==> Requirements
Build: Xcode (on macOS) ✘
Required: macOS >= 12 (or Linux) ✔
```

## ML Book

http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf 

## Keras Books
Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow by Aurélien Geron

https://www.manning.com/books/deep-learning-with-python-second-edition François Chollet


## PyTorch

https://www.youtube.com/playlist?list=PLA0M1Bcd0w8xUIMIPSoiW05lDyPNPt4tf (ru)

https://leanpub.com/pytorch

Book https://sebastianraschka.com/blog/2022/ml-pytorch-book.html

Book https://sebastianraschka.com/blog/2022/ml-pytorch-book.html

https://www.ritchieng.com/the-incredible-pytorch/

https://pytorch.org/tutorials/

https://pytorch.org/docs/stable/index.html

https://github.com/Atcold/pytorch-Deep-Learning-Minicourse . PyTorch

https://github.com/vietnguyen91/Deeplab-pytorch

https://theblog.github.io/post/from-tensorflow-to-pytorch/

https://nn.labml.ai/

https://github.com/omerbsezer/Fast-Pytorch

https://spandan-madan.github.io/DeepLearningProject/docs/Deep_Learning_Project-Pytorch.html

<https://www.reddit.com/r/Python/comments/cyslju/ai_cheatsheets_now_learn_tensorflow_keras_pytorch/>

### Youtube

https://www.youtube.com/c/PyTorch

https://www.youtube.com/watch?v=v43SlgBcZ5Y PyTorch Tutorial (2022), Part 1: Tensors

https://www.youtube.com/watch?v=w9U57o6wto0 PyTorch Tutorial (2022), Part 2: Basic Networks

https://www.youtube.com/watch?v=NaptjtDyvuY PyTorch Tutorial (2022), Part 3:

https://www.youtube.com/watch?v=c36lUUr864M Deep Learning With PyTorch - Full Course

https://www.youtube.com/watch?v=Wr0SZ5BNmVk Intro To TorchData: Load Data Like A Pro In PyTorch

https://www.youtube.com/watch?v=GIsg-ZUy0MY PyTorch for Deep Learning - Full Course / Tutorial


 
