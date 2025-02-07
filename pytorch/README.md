https://proproprogs.ru/

JAX for PyTorch users
https://cloud.google.com/blog/products/ai-machine-learning/guide-to-jax-for-pytorch-developers

https://pytorchstepbystep.com/

https://habr.com/ru/articles/870426/
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

### Model viewer
```
While there isn't a single, dedicated "PyTorch model viewer" that directly opens .ph files,
there are several excellent tools and techniques you can use
to visualize and inspect your PyTorch models:

1. Netron:

Versatile and widely used: Netron is a free, open-source viewer that supports a wide variety of model formats, including ONNX (Open Neural Network Exchange).   
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


 
