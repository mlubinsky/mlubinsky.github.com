<https://habr.com/post/417209/>

<https://habr.com/post/414165/>

<https://habr.com/company/ods/blog/344044/>

<https://mlcourse.ai/>

<https://onnx.ai/> NN format

<https://twitter.com/petewarden>

<https://twitter.com/lc0d3r>

<https://www.youtube.com/watch?v=o64FV-ez6Gw&feature=youtu.be>

<https://bair.berkeley.edu/blog/2018/08/06/recurrent/>

<https://www.youtube.com/watch?v=Agv-SioIZac&list=PL-_cKNuVAYAUWTBKPpWbTGmo5zadoaeCk>

<https://deepnotes.io/>

<http://iamtrask.github.io/>

<https://stanford.edu/~shervine/teaching/cs-229/cheatsheet-deep-learning>

<https://stats.stackexchange.com/questions/154879/a-list-of-cost-functions-used-in-neural-networks-alongside-applications>

![ActivationFunction](ActivationFunction.png)

## Deep Learning

<https://arxiv.org/abs/1810.01109> Deep Learning on Android

<https://arxiv.org/abs/1809.02165v1> . Generic object detection

<http://www.deeplearningbook.org/> . BOOK

<https://www.youtube.com/playlist?list=PLldrX-tcWesPRtPAJuQkBo3drEMyAlV2c> .  complimentary youtube channel

<http://neuralnetworksanddeeplearning.com/index.html> . book

<https://github.com/rasbt/deep-learning-book> book

<https://blog.floydhub.com/guide-to-hyperparameters-search-for-deep-learning-models/>

<https://medium.com/octavian-ai/which-optimizer-and-learning-rate-should-i-use-for-deep-learning-5acb418f9b2>

<http://course.fast.ai/>

<https://www.zerotodeeplearning.com/>

<https://github.com/ysh329/deep-learning-model-convertor>

<https://www.youtube.com/watch?v=9X_4i7zdSY8&t=2s>

<https://datascience.stackexchange.com/questions/12851/how-do-you-visualize-neural-network-architectures>

<https://modelzoo.co/>

## DL on Edge
<https://towardsdatascience.com/deep-learning-on-the-edge-9181693f466c>

<https://towardsdatascience.com/why-machine-learning-on-the-edge-92fac32105e6>

<https://medium.com/@bryancostanich/the-future-is-tiny-44dea02e4517>

## ARM
<https://www.dlology.com/blog/how-to-run-deep-learning-model-on-microcontroller-with-cmsis-nn/>
<https://www.youtube.com/watch?v=jlYDrmYJxh4>
<https://developer.arm.com/products/processors/machine-learning/>
<https://community.arm.com/processors/b/blog/posts/new-neural-network-kernels-boost-efficiency-in-microcontrollers-by-5x>
<https://github.com/ARM-software/CMSIS_5>
<https://www.slideshare.net/linaroorg/hkg18312-cmsisnn>

Given probability p, the corresponding odds are calculated as p / (1 – p). 
The logit function is simply the logarithm of the odds: logit(x) = log(x / (1 – x)).
The value of the logit function heads towards infinity as p approaches 1 and towards negative infinity as it approaches 0.

The logit function is useful in analytics because it maps probabilities (which are values in the range [0, 1]) to the full range of real numbers. In particular, if you are working with “yes-no” (binary) inputs it can be useful to transform them into real-valued quantities prior to modeling. This is essentially what happens in logistic regression.

The inverse of the logit function is the sigmoid function. That is, if you have a probability p, sigmoid(logit(p)) = p. The sigmoid function maps arbitrary real values back to the range [0, 1]. The larger the value, the closer to 1 you’ll get.

The formula for the sigmoid function is σ(x) = 1/(1 + exp(-x)).

## Vanishing gradient problem
<https://en.wikipedia.org/wiki/Vanishing_gradient_problem>
<https://www.quora.com/What-is-the-vanishing-gradient-problem>

Vanishing gradient problem depends on the choice of the activation function. Many common activation functions (e.g sigmoid or tanh) 'squash' their input into a very small output range in a very non-linear fashion. For example, sigmoid maps the real number line onto a "small" range of [0, 1]. As a result, there are large regions of the input space which are mapped to an extremely small range. In these regions of the input space, even a large change in the input will produce a small change in the output - hence the gradient is small.

We can avoid this problem by using activation functions which don't have this property of 'squashing' the input space into a small region. A popular choice is Rectified Linear Unit which maps 𝑥 to 𝑚𝑎𝑥(0,𝑥).

Rectified Linear activation function does not have this problem. The gradient is 0 for negative (and zero) inputs and 1 for positive inputs

<https://pythonprogramming.net/introduction-deep-learning-python-tensorflow-keras/>

<https://www.youtube.com/watch?v=T0r-uCXvDzQ>

<https://www.youtube.com/watch?v=aircAruvnKk>

<https://medium.com/inbrowserai/simple-diagrams-of-convoluted-neural-networks-39c097d2925b>

<https://recurrentnull.wordpress.com/2017/12/14/practical-deep-learning-talk/>

<https://recurrentnull.wordpress.com/2018/02/06/deep-learning-concepts-and-frameworks-find-your-way-through-the-jungle-talk/>

<https://brohrer.github.io/blog.html>

<https://mapr.com/blog/deep-learning-tensorflow/>

<https://towardsdatascience.com/how-to-learn-deep-learning-in-6-months-e45e40ef7d48>

<https://www.bepec.in/deeplearning>

<https://www.asozykin.ru/courses/nnpython>

<https://news.ycombinator.com/item?id=17750791>

<https://github.com/fotisk07/Deep-Learning-Coursera>

## TensorFlow

<https://github.com/tensorflow/models/tree/master/research/object_detection>

<https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/using_your_own_dataset.md>

<https://twitter.com/hashtag/tensorflowjs>

<https://tf.wiki/en/preface.html> . 
 
<https://colab.research.google.com/> 

<https://www.tensorflow.org/lite/>

<https://medium.com/tensorflow/training-and-serving-ml-models-with-tf-keras-fd975cc0fa27>
 
<https://www.youtube.com/watch?v=tYYVSEHq-io&t=3664s>

<https://www.youtube.com/watch?v=tjsHSIG8I08>

<https://www.youtube.com/channel/UC0rqucBdTuFTjJiefW5t-IQ> 

<https://becominghuman.ai/an-introduction-to-tensorflow-f4f31e3ea1c0>
 
<https://medium.com/@tensorflow>

<https://habrahabr.ru/search/?q=tensorflow>

<https://github.com/tensorflow/workshops>

https://docs.devicehive.com/docs

https://ai.googleblog.com/2017/05/using-machine-learning-to-explore.html

Nilolenko DeepLearning book
<https://www.amazon.com/Deep-Learning-Applications-Using-Python/dp/1484235150/>   

<https://medium.com/tensorflow/introducing-tensorflow-probability-dca4c304e245>

<https://colab.research.google.com/>

<https://www.youtube.com/watch?v=tYYVSEHq-io>

http://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.66230&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false
 
## RNN LSTM

https://towardsdatascience.com/the-fall-of-rnn-lstm-2d1594c74ce0  The fall of RNN / LSTM use Attention Networks

## Image processing

<https://arxiv.org/abs/1809.02165v1>

<https://www.embedded-vision.com/industry-analysis/books>

<https://towardsdatascience.com/building-an-image-classifier-running-on-raspberry-pi-a7a45153acc8>

<https://towardsdatascience.com/the-4-convolutional-neural-network-models-that-can-classify-your-fashion-images-9fe7f3e5399d>

<https://towardsdatascience.com/neural-network-embeddings-explained-4d028e6f0526>

The 28 × 28 image was considered a one-dimensional vector of size 282 = 796. But this transformation throws away lots of the spatial information contained in the image.
The CNN take advantage of this additional structure (locality and translational invariance) 

<http://rodrigob.github.io/are_we_there_yet/build/classification_datasets_results.html>

<https://habr.com/company/intel/blog/415811/>   NN for image processing

<https://habr.com/company/intel/blog/417809/>

<https://habr.com/post/416777/>

<https://habr.com/hub/image_processing/>

<https://habr.com/company/dataart/blog/350120/>

<https://rowhanm.github.io/MiniCatsDogs/>

<https://www.toptal.com/machine-learning/machine-learning-video-analysis>

<https://hackernoon.com/a-comprehensive-design-guide-for-image-classification-cnns-46091260fb92>

<https://www.zerotosingularity.com/blog/fast-ai-part-1-course-1-annotated-notes/>

<https://medium.com/@hiromi_suenaga/deep-learning-2-part-1-lesson-1-602f73869197>

<https://sod.pixlab.io/>

<https://habr.com/company/binarydistrict/blog/354524/>

<https://heartbeat.fritz.ai/the-5-computer-vision-techniques-that-will-change-how-you-see-the-world-1ee19334354b>

<https://towardsdatascience.com/real-time-object-detection-api-using-tensorflow-and-opencv-47b505d745c4>

<https://towardsdatascience.com/is-google-tensorflow-object-detection-api-the-easiest-way-to-implement-image-recognition-a8bd1f500ea0>

<https://habrahabr.ru/post/354092/> Object recognition

https://medium.com/@jonathan_hui/what-do-we-learn-from-region-based-object-detectors-faster-r-cnn-r-fcn-fpn-7e354377a7c9

<https://blog.paperspace.com>



<https://medium.com/ml-everything/how-to-actually-easily-detect-objects-with-deep-learning-on-raspberry-pi-4fd40af84fee>

<https://medium.com/ml-everything/offline-object-detection-and-tracking-on-a-raspberry-pi-fddb3bde130>

<https://www.pyimagesearch.com/2017/09/18/real-time-object-detection-with-deep-learning-and-opencv/>

## YOLO

<https://medium.com/paperspace/tutorial-on-implementing-yolo-v3-from-scratch-in-pytorch-part-1-a0054d38ec78>

<https://medium.com/@jonathan_hui/real-time-object-detection-with-yolo-yolov2-28b1b93e2088>

<https://pjreddie.com/darknet/yolo/>

<https://pythonprogramming.net/video-tensorflow-object-detection-api-tutorial/>

<https://www.coursera.org/learn/convolutional-neural-networks/lecture/VgyWR/object-detection>


<https://aws.amazon.com/rekognition/>

<https://www.microsoft.com/developerblog/2017/04/10/end-end-object-detection-box/>

<https://towardsdatascience.com/feature-extraction-and-similar-image-search-with-opencv-for-newbies-3c59796bf774>

<https://software.intel.com/en-us/articles/visualising-cnn-models-using-pytorch>

<https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606>
