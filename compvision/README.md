Book:
https://books.google.cz/books?id=xtC_EAAAQBAJ&printsec=frontcover&redir_esc=y#v=onepage&q&f=false

YOLO
https://habr.com/ru/articles/865834/

http://cv-blog.ru/

https://arxiv.org/pdf/1812.01187.pdf .  CNN training tricks for image classification

<https://habr.com/ru/post/511372/>  Deep Learning: как это работает? Часть 3 — архитектуры CNN

<https://habr.com/ru/post/510560/>  RetinaNet

Image formats:
<https://youtu.be/P1K0ZNGczsk>

<https://github.com/videoflow/videoflow>

<https://habr.com/ru/post/461365/> compvision

https://habr.com/ru/company/jetinfosystems/blog/498652/ Mask R-CNN etc
<https://habr.com/ru/company/mipt/blog/458190/>  Вижу, значит существую: обзор Deep Learning в Computer Vision (часть 2)

<https://habr.com/ru/post/481844/>

<https://habr.com/ru/company/mailru/blog/460307/>

<https://sahnimanas.github.io/post/anatomy-of-a-high-performance-convolution/> convolution 
<https://www.dlology.com/blog/how-to-train-an-object-detection-model-easy-for-free/>

## Image processing without NN

<https://www.linkedin.com/posts/adityaojas_opencv-deeplearning-innovation-activity-6690219835810484224-9rcO> OpenCV Sudoku Solver

<https://realpython.com/storing-images-in-python/>

<https://open.compscicenter.ru/archive/images/> . Все что нужно знать программисту об изображениях

<https://rsipvision.com/ComputerVisionNews-2019May/>

<https://tryolabs.com/resources/introductory-guide-computer-vision/>

<https://www.tutorialspoint.com/dip/index.htm>

<https://habr.com/ru/post/449198/> . FFMpeg

FFmpeg – это библиотека для создания видеоприложений или даже утилит общего назначения, которая берет на себя всю тяжелую работу по обработке видео, выполняя все декодирование, кодирование, мультиплексирование и демультиплексирование для вас.

Задача: Full HD IP-камера в стандарте h.264 передает RTSP поток. Размер распакованного кадра 1920x1080 пикселей, частота 25 кадров в секунду. Нужно получать декодированные кадры в оперативную память и каждый 25 кадр сохранять на диск.

<https://images.guide/> .  <https://imageoptim.com/> .   Image compression

<https://opensource.com/article/19/3/python-image-manipulation-tools>

<https://habr.com/hub/image_processing/>

Нахождение объектов на картинках: <https://habr.com/ru/company/joom/blog/445354/>

<https://habr.com/ru/post/448316/> Keras, Google GPU, deploying on Android, Google Colab, transfer learning

<https://www.udemy.com/master-deep-learning-computer-visiontm-cnn-ssd-yolo-gans/learn/v4/> . UDEMY

<https://www.matec-conferences.org/articles/matecconf/pdf/2018/14/matecconf_imet2018_01016.pdf> Extract objects from video

* SIFT  
<https://en.wikipedia.org/wiki/Scale-invariant_feature_transform>   
<https://people.eecs.berkeley.edu/~malik/cs294/lowe-ijcv04.pdf>
<https://en.wikipedia.org/wiki/Scale-invariant_feature_transform>

* SURF . Speeded-Up Robust Features
* FAST . <https://www.edwardrosten.com/work/rosten_2006_machine.pdf>
* BRIEF . Binary Robust Independent Elementary Features
<https://www.cs.ubc.ca/~lowe/525/papers/calonder_eccv10.pdf>

* ORB .  Oriented FAST and Rotated BRIEF
* HoG <https://en.wikipedia.org/wiki/Hough_transform>


<https://github.com/Merwanedr/Vusion> image analysis using AI

<https://github.com/Merwanedr/Popbot> . image transformation

## OpenCV
<https://habr.com/ru/company/intel/blog/452790/>

conda install opencv

Basic camera test:

cat test.py
```
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

```

<https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/> . People Counter

<https://www.learnopencv.com>

<https://opencv-python-tutroals.readthedocs.io/en/latest/index.html>

<https://heartbeat.fritz.ai/opencv-python-cheat-sheet-from-importing-images-to-face-detection-52919da36433>

<https://medium.com/machine-learning-world/feature-extraction-and-similar-image-search-with-opencv-for-newbies-3c59796bf774>

<https://www.pyimagesearch.com/2019/03/11/liveness-detection-with-opencv/>

<https://stackoverflow.com/questions/42203898/python-opencv-blob-detection-or-circle-detection>

<https://makehardware.com/2016/05/19/blob-detection-with-python-and-opencv/>

## CNN

<https://poloclub.github.io/cnn-explainer/> 

<https://machinelearningmastery.com/deep-learning-for-computer-vision/> . Book

<https://www.udemy.com/master-deep-learning-computer-visiontm-cnn-ssd-yolo-gans/learn/v4/>

<https://neurohive.io/en/>

### SyNet - fast inference - convolution calculation 
<https://habr.com/ru/post/448436/> n

https://habr.com/ru/post/477718/


<https://machinelearningmastery.com/how-to-manually-scale-image-pixel-data-for-deep-learning/>

<https://www.jeremyjordan.me/>


<https://www.rsipvision.com/ComputerVisionNews-2019March/>

https://habr.com/ru/company/mipt/blog/450732/ . Deep Learning for Computer Vision

## Reviews: Object Detection with Deep Learning: A Review
<https://arxiv.org/abs/1809.02165v2> 

<https://arxiv.org/abs/1807.05511> . 

<https://habr.com/ru/post/459088/> Point Clouds

<https://habr.com/ru/post/444172/>


<https://towardsdatascience.com/@sh.tsang>

<https://habr.com/ru/post/443734/> .  BagNet bag of words

<https://blog.nanonets.com/hyperparameter-optimization/> .  Hyperparameter optimization

### Real time object detection with tensorflow
<https://www.edureka.co/blog/tensorflow-object-detection-tutorial/>

<https://medium.com/@madhawavidanapathirana/real-time-human-detection-in-computer-vision-part-2-c7eda27115c6>


<https://habr.com/ru/company/nixsolutions/blog/443236/> . Демистифицируем свёрточные нейросети

## ResNet
ResNet — это сокращенное название для Residual Network (дословно  — «остаточная сеть»)

Соединения быстрого доступа (shortcut connections) пропускают один или несколько слоев и выполняют сопоставление идентификаторов. Их выходы добавляются к выходам stacked layers. Используя ResNet, можно решить множество проблем, таких как:

ResNet относительно легко оптимизировать: «простые» сети (которые просто складывают слои) показывают большую ошибку обучения, когда глубина увеличивается.
ResNet позволяет относительно легко увеличить точность благодаря увеличению глубины, чего с другими сетями добиться сложнее.

<https://neurohive.io/ru/vidy-nejrosetej/resnet-34-50-101/>

<https://habr.com/ru/post/449864/>

## Segmentation

<https://www.analyticsvidhya.com/blog/2019/04/introduction-image-segmentation-techniques-python/>

Segmentation = classify every pixel on picture.

The Segmentaition does not require a lot of data because every pixel is used for back propagation.
Number of classes on the picture is defined upfront (hyperparameter).


Similarity coefficient metrics: Jaccard Coefficient, Dice Coefficient, Cosine Coefficient.
Jaccard Coefficient = intersection  / union

Fully Convolutional Network (FCN) - no dense (aka fully connected)layer.
FCN has less parameters and can take images of any size.
Instead the dense layer FCN uses up-sampling to the original input size.

Diffferent types of upsampling to make the image of bigger size:
* nearest neibouhr upsampling
* bilinear
* cubic
* unpulling
* deconvolution
* hierarhical (SegNet)

Added skip connection: ResNet (UNet, TernausNet )

<https://neurohive.io/ru/vidy-nejrosetej/u-net-image-segmentation/> U-Net

<https://www.youtube.com/watch?v=SEvUc46gUaQ> . Deep Learning for the Segmentation, Classification, and Quantification

<https://www.youtube.com/watch?v=r2KA99ThEH4>  Deep Learning на пальцах 7 - Segmentation и Object Detection (Владимир Игловиков)

<https://www.youtube.com/watch?v=MpZxV6DVsmM> FastAI lesson 3  - image segmentation


Feature Pyramid Networks (FPN)


## Detection
Predicts:
- boxes around the object
- class (cars, human)
- attributes (optional): colors,

Detection metric is sofisticated: named mAP

confidence of class

NMS - non maximum supression

One-shot detectors (fast):    YOLO, SSD, RetinaNet, SquueezeNet, DetectNet

Two-shot detectors (precize): R-CCN, Fast R-CNN, Faster R-CNN

R(egion)-CNN:  <https://www.youtube.com/watch?v=LFQPUYDUpvg> -> Semen (ru)
* Shot 1) find the regions of interest (region proposals: ~2K per picture) (RoI), wrappen region: scale all regions to the same size (wrapped region)
* Shot 2) for every  such region use CNN (with transfer learning trained on ImageNet replacing the last layer)

R-CNN is slow because if ~2K regions then for every region we need to call CNN


Fast R-CNN:  https://www.youtube.com/watch?v=LFQPUYDUpvg
Full convolution: run convolution just once for entire picture.
Only after that use regions. It speed up 25 times the R-CNN!
 
Faster R-CNN: the proposal regions generated by NN
 
<https://petewarden.com/> ML on embedded devices

<https://www.youtube.com/watch?v=DclyqYN99og&list=PLlb7e2G7aSpQc4CW-9BI9L_jZVyUbbSWX> Введение в анализ изображений lectures

<https://www.youtube.com/watch?v=azkzDWi8X64&list=PLlb7e2G7aSpQ4C5ykr2Ce1mfxM01l6_HV>   Анализ изображений и видео, часть 2

<https://www.datasciencecentral.com/profiles/blogs/off-the-beaten-path-using-deep-forests-to-outperform-cnns-and-rnn>



https://www.udemy.com/master-deep-learning-computer-visiontm-cnn-ssd-yolo-gans/learn/v4/t/lecture/12583888?start=0



<https://medium.freecodecamp.org/how-to-build-the-best-image-classifier-3c72010b3d55> . PyTorch

## License Plate Detection
<https://sod.pixlab.io/articles/license-plate-detection.html>
<https://news.ycombinator.com/item?id=19276977>

<https://habr.com/ru/post/439330/> . - uses MASK R_CNN



## Tools

<https://github.com/opencv/cvat> Image and Video annotator
<http://www.robots.ox.ac.uk/~vgg/software/via/> .  Image Annotator

<https://github.com/Slava/label-tool> .  Image labelling

<https://factordaily.com/indian-data-labellers-powering-the-global-ai-race/> .    Image labelling

<https://idealo.github.io/imageatm/>





<https://github.com/albu/albumentations> . Augmentation

<https://arxiv.org/abs/1603.07285> convolution arithmetics 



<https://paperswithcode.com/sota> software with code

<https://medium.com/@jonathan_hui/object-detection-series-24d03a12f904>

<https://medium.com/@jonathan_hui/object-detection-speed-and-accuracy-comparison-faster-r-cnn-r-fcn-ssd-and-yolo-5425656ae359>

<https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html>

<https://lilianweng.github.io/lil-log/2017/12/31/object-recognition-for-dummies-part-3.html>

<https://youngjoongkwon.com/2018/11/10/object-detection-r-cnn-fast-r-cnn-faster-r-cnn-mask-r-cnn-yolo-and-ssd/>

## Udacity and Udemy and FastAI

<https://www.udacity.com/course/introduction-to-computer-vision--ud810> .  Free course

<https://www.udemy.com/computer-vision-a-z/learn/v4/overview>

<https://www.udemy.com/master-computer-vision-with-opencv-in-python/learn/v4/overview>

<https://www.udemy.com/master-deep-learning-computer-visiontm-cnn-ssd-yolo-gans/learn/v4/overview>

<https://course.fast.ai/>  Practical Deep Learning for Coders, v3


<https://www.youtube.com/channel/UCX7Y2qWriXpqocG97SFW2OQ>

<https://habr.com/ru/company/mailru/blog/439226/> . Scala MXNet Docker

<https://habr.com/ru/post/441006/> image processing  with skikit-image

How to Recognise multiple objects in the same image?
 Detecting multiple objects in the same image boils is essentially a "segmentation problem". 
Two popular algorithms are YOLO (You Only Look Once), and SSD(Single Shot Multibox Detector) 
<https://arxiv.org/abs/1512.02325>
<https://github.com/tensorflow/models/tree/master/object_detection%22Object%20Detection%20API%22>
<https://becominghuman.ai/tensorflow-object-detection-api-tutorial-training-and-evaluating-custom-object-detector-ed2594afcf73>
<https://github.com/thtrieu/darkflow>



<http://blog.qure.ai/notes/semantic-segmentation-deep-learning-review>

## MobileNet
<https://hackernoon.com/tf-serving-keras-mobilenetv2-632b8d92983c>
<https://towardsdatascience.com/review-mobilenetv1-depthwise-separable-convolution-light-weight-model-a382df364b69>

<https://towardsdatascience.com/evolution-of-object-detection-and-localization-algorithms-e241021d8bad>

<https://medium.com/ilenze-com/object-detection-using-deep-learning-for-advanced-users-part-1-183bbbb08b19>
Traditional methods of detection involved using a block-wise orientation histogram(SIFT or HOG) feature which could not achieve high accuracy in standard datasets such as PASCAL VOC.

<https://github.com/bobquest33/dlib_obj_count> . The Shelf Detector System For Retail Stores Using Object Detection; Dlib is a modern C++ toolkit containing machine learning algorithms


<https://habr.com/ru/post/440608/> detect empty space on parking place OpenCV, TensorFlow, Keras

<<http://rodrigob.github.io/are_we_there_yet/build/classification_datasets_results.html>

<https://www.rsipvision.com/category/rsip-vision-learns/>

<https://www.rsipvision.com/computer-vision-news/>

<https://www.toptal.com/machine-learning/machine-learning-video-analysis>

<https://hackernoon.com/a-comprehensive-design-guide-for-image-classification-cnns-46091260fb92>

<https://www.zerotosingularity.com/blog/fast-ai-part-1-course-1-annotated-notes/>

<https://medium.com/@hiromi_suenaga/deep-learning-2-part-1-lesson-1-602f73869197>

<https://sod.pixlab.io/>

<https://habr.com/company/binarydistrict/blog/354524/>


<https://blog.paperspace.com>



## Image processing



<<https://www.liip.ch/en/blog/numbers-recognition-mnist-on-an-iphone-with-coreml-from-a-to-z> .  CoreML

<https://openmv.io/>

## Hardware accelerators TCU, NPU, ... 
<https://habr.com/ru/post/455353/>

<https://habr.com/ru/company/advantech/blog/481862/> Jetson NVidia Maxwell GPU

<https://www.analyticsvidhya.com/blog/2017/10/image-skilltest/>

<https://habr.com/company/intel/blog/415811/>   NN for image processing

<https://habr.com/company/intel/blog/417809/>

<https://habr.com/post/416777/> . CNN explained

<https://heartbeat.fritz.ai/the-5-computer-vision-techniques-that-will-change-how-you-see-the-world-1ee19334354b>

<https://towardsdatascience.com/real-time-object-detection-api-using-tensorflow-and-opencv-47b505d745c4>

<https://towardsdatascience.com/is-google-tensorflow-object-detection-api-the-easiest-way-to-implement-image-recognition-a8bd1f500ea0>

<https://habrahabr.ru/post/354092/> Object recognition - разработать прототип системы, в реальном времени обнаруживающей сотрудников без касок

https://medium.com/@jonathan_hui/what-do-we-learn-from-region-based-object-detectors-faster-r-cnn-r-fcn-fpn-7e354377a7c9


<https://habr.com/ru/post/446872/> . Raspberry Pi and OpenCV
<https://medium.com/ml-everything/how-to-actually-easily-detect-objects-with-deep-learning-on-raspberry-pi-4fd40af84fee>

<https://medium.com/ml-everything/offline-object-detection-and-tracking-on-a-raspberry-pi-fddb3bde130>

## Real-time object detection and tracking

<https://github.com/RedisGears/EdgeRealtimeVideoAnalytics>  using Redis Streams, RedisGears, RedisAI and RedisTimeSeries for Realtime Video Analytics (i.e. counting people)

<https://trackingjs.com/>

<https://habr.com/ru/post/454132/>

https://zoneminder.com/

https://www.youtube.com/watch?v=MyAOtvwTkT0 . TensorFlow Object API

<https://habr.com/ru/company/dataart/blog/350120/>

<https://www.pyimagesearch.com/2017/09/18/real-time-object-detection-with-deep-learning-and-opencv/>

<https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/>

<https://www.pyimagesearch.com/2018/10/29/multi-object-tracking-with-dlib/>

<https://www.pyimagesearch.com/2018/08/06/tracking-multiple-objects-with-opencv/>

<https://heartbeat.fritz.ai/detecting-objects-in-videos-and-camera-feeds-using-keras-opencv-and-imageai-c869fe1ebcdb>

<https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/>

 OpenCV обзавелся поддержкой YOLO внутри себя.
 
BOOSTING Tracker

MIL Tracker

KCF Tracker - Kernelized Correlation Filters

TLD - Tracking, learning and detection

MEDIANFLOW Tracker

GOTURN tracker

MOSSE tracker - Minimum Output Sum of Squared Error

CSRT tracker - Discriminative Correlation Filter with Channel and Spatial Reliability (DCF-CSR)

## YOLO

<https://medium.com/paperspace/tutorial-on-implementing-yolo-v3-from-scratch-in-pytorch-part-1-a0054d38ec78>

<https://medium.com/@jonathan_hui/real-time-object-detection-with-yolo-yolov2-28b1b93e2088>

<http://www.emaraic.com/blog/yolov3-custom-object-detector>

<https://pjreddie.com/darknet/yolo/>

<https://pythonprogramming.net/video-tensorflow-object-detection-api-tutorial/>



<https://aws.amazon.com/rekognition/>

<https://www.microsoft.com/developerblog/2017/04/10/end-end-object-detection-box/>

<https://towardsdatascience.com/feature-extraction-and-similar-image-search-with-opencv-for-newbies-3c59796bf774>

<https://software.intel.com/en-us/articles/visualising-cnn-models-using-pytorch>

<https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606>

<https://github.com/TensorImage/TensorImage>

<https://mlwhiz.com/blog/2018/09/22/object_detection/>

<https://github.com/symisc/sod> Embedded computer vision and ML library

<https://www.youtube.com/watch?v=XVvfcj_F_uc>

<https://habr.com/post/430906/> . Compiling OpenCV for RusberryPi under Ubuntu cross-compilation to ARM

<https://habr.com/ru/post/432444/> Распознавание номеров. Практическое пособие. Часть 1

<https://github.com/OlafenwaMoses/ImageAI>

<https://towardsdatascience.com/evolution-of-object-detection-and-localization-algorithms-e241021d8bad>

<https://towardsdatascience.com/using-object-detection-for-complex-image-classification-scenarios-part-1-779c87d1eecb>

<https://www.pyimagesearch.com/2018/10/22/object-tracking-with-dlib/>

<https://arxiv.org/abs/1809.02165v1>


<https://blog.nanonets.com/real-time-object-detection-for-drones/>

<https://www.embedded-vision.com/industry-analysis/books>

<https://towardsdatascience.com/building-an-image-classifier-running-on-raspberry-pi-a7a45153acc8>

<https://habr.com/post/429400/> . запускаем SqueezeNet v.1.1 на Raspberry Zero в realtime (part2)

<https://habr.com/post/428021/> запускаем SqueezeNet v.1.1 на Raspberry Zero в realtime (part1)

<https://www.pyimagesearch.com/2018/12/31/keras-conv2d-and-convolutional-layers/>

<https://www.youtube.com/channel/UCp0a6npOi89ksgks3ej7FPw/videos> on Raspberry Pi 3


<https://github.com/tensorflow/models/tree/master/research/object_detection>


<https://habr.com/ru/post/439122/> разделим 128х128 одноцветной картинки на четыре части и случайным образом будем помещать в эти четверти эллипс и, например, треугольник; задача состоит в том, что бы обучить сеть отличать, например четырехугольный полигон от эллипса. Мы не будем детектить на одной картинке треугольник и четырехугольник, мы будем детектить их отдельно, в разных трейн, на фоне помехи в виде эллипса.

<https://heartbeat.fritz.ai/detecting-objects-in-videos-and-camera-feeds-using-keras-opencv-and-imageai-c869fe1ebcdb>

<https://towardsdatascience.com/wtf-is-image-classification-8e78a8235acb>

<http://www.themtank.org/a-year-in-computer-vision> . covers year 2016

<https://habr.com/ru/post/346140/> russian translation of part 1

SSD: Single Shot MultiBox Detector использует единую нейронную сеть, которая выполняет все необходимые вычисления и устраняет необходимость в ресурсоёмких методах предыдущего поколения. Он демонстрирует «75,1% mAP, превосходя сравнимую самую современную модель Faster R-CNN».

YOLO9000: Better, Faster, Stronger, в которой используются системы обнаружения YOLOv2 и YOLO9000 (YOLO означает You Only Look Once). YOLOv2 — это сильно улучшенная модель YOLO от середины 2015 года, и она способна показать лучшие результаты на видео с очень высокой частотой кадров (до 90 FPS на изображениях низкого разрешения при использовании обычного GTX Titan X). Вдобавок к повышению скорости, система превосходит Faster RCNN с ResNet и SSD на определённых наборах данных для определения объектов.

Система Feature Pyramid Networks for Object Detection разработана в научно-исследовательском подразделении FAIR (Facebook Artificial Intelligence Research). В ней применяется «врождённая многомасштабная пирамидальная иерархия глубоких свёрточных нейросетей для конструирования пирамид признаков с минимальными дополнительными затратами». Это означает сохранение мощных репрезентаций без потери скорости и дополнительных затрат памяти. Разработчики добились рекордных показателей на наборе данных COCO (Common Objects in Context). В сочетании с базовой системой Faster R-CNN она превосходит результаты победителей 2016 года.

R-FCN: Object Detection via Region-based Fully Convolutional Networks. Ещё один метод, в котором разработчики отказались от применения ресурсоёмких подсетей для отдельных регионов изображения сотни раз на каждой картинке. Здесь детектор по регионам полностью свёрточный и производит совместные вычисления на всём изображении целиком. «При тестировании скорость работы составила 170 мс на одно изображение, что в 2,5–20 раз быстрее, чем у Faster R-CNN»

## Code

<https://github.com/kaszperro/slick-dnn> Deep NN in pure python

<https://github.com/Merwanedr/Vusion> image analysis using AI

<https://github.com/Merwanedr/Popbot> . image transformation

<https://github.com/Mybridge/amazing-machine-learning-opensource-2019>

<https://github.com/keras-team/keras/tree/master/examples> Keras

<https://github.com/Yorko/mlcourse.ai/tree/master/jupyter_russian>

<https://heartbeat.fritz.ai/classification-with-tensorflow-and-dense-neural-networks-8299327a818a>


<https://nextjournal.com/mpd/image-classification-with-keras>


<https://rowhanm.github.io/MiniCatsDogs> Image classification with very few images:
  Data augmentation and Pseudo-labeling. (a variant of semi-supervised learning)

## DataSets

ImageNet <http://image-net.org/challenges/LSVRC/2013/> — это набор данных миллионов помеченных изображений с высоким разрешением, относящихся примерно к 22 тысячам категорий. Изображения были собраны из Интернета и помечены людьми с помощью краудсорсинга. Начиная с 2010 года в рамках конкурса визуальных объектов Pascal проводится ежегодный челлендж «Крупномасштабный конкурс визуального распознавания ImageNet» (ILSVRC2013). ILSVRC использует подмножество ImageNet из примерно 1000 изображений в каждой из 1000 категорий. Существует около 1,2 миллиона обучающих образов, 50 тыс. валидаций 150 тыс. тестовых изображений.

PASCAL VOC предоставляет стандартизированные наборы данных изображений для распознавания классов объектов, стандартному набору инструментов для доступа к наборам данных и аннотациям, позволяет оценивать и сравнивать методы, наконец, оценивает производительность при распознавании классов объектов.

<https://gengo.ai/datasets/20-best-image-datasets-for-computer-vision/>

<http://cocodataset.org/>

<https://en.wikipedia.org/wiki/CIFAR-10> CIFAR 

<https://en.wikipedia.org/wiki/List_of_datasets_for_machine_learning_research>

<https://github.com/mpatacchiola/tensorbag>

  ImageNet

## CNN 

<https://www.youtube.com/watch?v=tOgBz8lFz8Q> . Deep Learning на пальцах 6 - Convolutional Neural Networks . sim0nsays

<https://habr.com/ru/post/443734/>

<https://en.wikipedia.org/wiki/Convolutional_neural_network>

<https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-convolutional-neural-networks>

<https://www.analyticsvidhya.com/blog/2018/12/guide-convolutional-neural-network-cnn/>

<https://habr.com/ru/company/binarydistrict/blog/354524/>

<https://habr.com/ru/company/mailru/blog/311706/> . Review of topologies

<https://habr.com/ru/post/436838/> Понимание сверточных нейронных сетей через визуализации в PyTorch

<https://youtu.be/whNAaM4NwKw> . Лекция 6 - Frameworks . sim0nsays


### CS231n Stanford class
<http://cs231n.stanford.edu/>

<http://cs231n.github.io/> . Stanford class



<https://medium.com/@geek_kid/making-your-first-cnn-part-3-6edd2476aaf1>

<https://www.pyimagesearch.com/2018/12/31/keras-conv2d-and-convolutional-layers/>

<https://www.youtube.com/watch?v=SQ67NBCLV98>

<https://towardsdatascience.com/the-4-convolutional-neural-network-models-that-can-classify-your-fashion-images-9fe7f3e5399d>

<https://towardsdatascience.com/types-of-convolutions-in-deep-learning-717013397f4d>

<https://www.liip.ch/en/blog/poke-zoo-or-making-deep-learning-tell-oryxes-apart-from-lamas-in-a-zoo-part-1-the-idea-and-concepts>

<https://towardsdatascience.com/deep-convolutional-neural-networks-ccf96f830178>

<https://blog.sicara.com/about-convolutional-layer-convolution-kernel-9a7325d34f7d>

<https://www.coursera.org/learn/convolutional-neural-networks/lecture/VgyWR/object-detection>

<https://medium.com/@ageitgey/machine-learning-is-fun-part-3-deep-learning-and-convolutional-neural-networks-f40359318721>

<https://www.youtube.com/watch?v=JB8T_zN7ZC0>  Brandon Rohrer How convolutional neural networks work, in depth

<https://medium.com/inbrowserai/simple-diagrams-of-convoluted-neural-networks-39c097d2925b>

<https://github.com/vdumoulin/conv_arithmetic>

<https://jameslittle.me/blog/2019/tensorflow-object-detection>

<https://arxiv.org/pdf/1707.07012.pdf> NasNet


<https://www.cbronline.com/news/google-ai-creates-novel-neural-network-nasnet> NasNet

<https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/>

<https://habr.com/company/sap/blog/415657/> TensorFlow Object Detection API

<https://ai.googleblog.com/2017/11/automl-for-large-scale-image.html> .  AutoML

<https://recurrentnull.wordpress.com/2017/12/14/practical-deep-learning-talk/>

<https://recurrentnull.wordpress.com/2018/02/06/deep-learning-concepts-and-frameworks-find-your-way-through-the-jungle-talk/>

<https://brohrer.github.io/blog.html>

<https://mapr.com/blog/deep-learning-tensorflow/>

<https://towardsdatascience.com/how-to-learn-deep-learning-in-6-months-e45e40ef7d48>

<https://www.bepec.in/deeplearning>

<https://www.asozykin.ru/courses/nnpython>

<https://news.ycombinator.com/item?id=17750791>

<https://github.com/fotisk07/Deep-Learning-Coursera>


##   Mask R-CNN

<https://habr.com/ru/post/483018/> Mask-R CNN от новичка до профессионала

<https://www.pyimagesearch.com/2018/11/19/mask-r-cnn-with-opencv/>

<https://github.com/matterport/Mask_RCNN>

<https://habr.com/ru/post/451164/>

<https://www.reddit.com/r/MachineLearning/comments/d1oyxf/research_rotated_mask_rcnn/>

<https://medium.com/@ageitgey/snagging-parking-spaces-with-mask-r-cnn-and-python-955f2231c400>

https://towardsdatascience.com/building-a-custom-mask-rcnn-model-with-tensorflow-object-detection-952f5b0c7ab4

<https://habr.com/ru/company/yandex/blog/431108/>

<https://www.analyticsvidhya.com/blog/2018/07/building-mask-r-cnn-model-detecting-damage-cars-python/>


## Software for IP cameras

<https://www.onvif.org/>

<https://habr.com/ru/company/ivideon/blog/458954/>

<https://securityrussia.com/blog/vms-vs-cms.html>

<https://habr.com/ru/company/intems/blog/322634/>

<https://habr.com/ru/company/ivideon/blog/454346/> Nobelic 

Бесплатное программное обеспечение
Herospeed. Herospeed VMS Клиент-серверное программное обеспечение, 256 каналов бесплатно. Скачать можно здесь. Поддерживаемые операционные системы — Windows и MacOS. Китай
iSpy скачать можно здесь. Список поддерживаемых брендов камер. Поддерживаемая операционная система — Windows. Мобильные приложения для Android, iOS и Windows Phone. Подробная инструкция по настройке iSpy на нашем сайте.
Kerberos. Программное обеспечение с открытым исходным кодом. Поддерживаемая операционная система — Linux. Бельгия
motionEyes.  Программное обеспечение с открытым исходным кодом. Поддерживаемые устройства. Поддерживаемая операционная система — Linux.
ZoneMinder. ZoneMinder скачать можно здесь. Поддерживаемые операционные системы — Linux,  Программное обеспечение с открытым исходным кодом.
Veyesys. Rapidvms скачать можно здесь. Поддерживаемые операционные системы — Windows, Linux и MacOS. Китай
Shinobi. Поддерживаемые операционные системы — Windows, Linux и MacOS. Список поддерживаемых брендов камер. Open Source
OpenALPR, программное обеспечение с открытым исходным кодом, для распознавания автомобильных номеров. Поддерживаемые операционные системы — Debian, CentOS. Скачать здесь.
Vargus. Программное обеспечение с открытым исходным кодом. Операционная система — Linux
Valkka. Поддерживаемое оборудование. Поддерживаемая операционная система — Linux (Ubuntu). Open Source


## Face detection
<https://habr.com/ru/company/ivideon/blog/443906/>

<https://www.pyimagesearch.com/2019/03/11/liveness-detection-with-opencv/>

<https://habr.com/ru/company/mailru/blog/449120/>

## Intel RealSense D4(15/35) and other cameras

<https://habr.com/ru/company/ivideon/blog/439870/>

<https://habr.com/company/intel/blog/430720/>

<https://habr.com/company/ivideon/blog/434308/> video monitoring

<https://www.blog.google/perspectives/aparna-chennapragada/google-lens-one-year/>

## Intel OpenVino on Raspberry Pi
<https://habr.com/company/intel/blog/434238/>

<https://habr.com/ru/post/436744/>

<https://software.intel.com/en-us/openvino-toolkit>

## CNN architectures

<https://neurohive.io/ru/vidy-nejrosetej/>

<https://www.jeremyjordan.me/convnet-architectures/>

<https://neurohive.io/en/popular-networks/>

<https://habr.com/company/intel/blog/417809/> . NN architectures for image recognition 

<https://towardsdatascience.com/deep-convolutional-neural-networks-ccf96f830178>

<https://towardsdatascience.com/https-medium-com-piotr-skalski92-deep-dive-into-deep-networks-math-17660bc376ba>

<https://medium.com/@14prakash/image-classification-architectures-review-d8b95075998f>

```
MobileNet
MobeleNet DepthWise
Res50
GoogleNet
SqueezeNet
ShuffleNet
YOLO v3
```

## Object detection

<https://en.wikipedia.org/wiki/Object_detection>

<https://mlwhiz.com/blog/2018/09/22/object_detection/>

<https://medium.com/@fractaldle/brief-overview-on-object-detection-algorithms-ec516929be93>

<http://users.cecs.anu.edu.au/~trumpf/theses/Jack_Henderson.pdf> Object tracking

<https://medium.com/zylapp/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852>

<https://www.learnopencv.com/training-yolov3-deep-learning-based-custom-object-detector/>

<https://www.rsipvision.com/ComputerVisionNews-2019January/>


## OCR (digits/characters) recognition

<https://en.wikipedia.org/wiki/Optical_character_recognition>

<http://neuralnetworksanddeeplearning.com/chap1.html>

https://stackabuse.com/pytesseract-simple-python-optical-character-recognition/

<https://www.codingame.com/playgrounds/37409/handwritten-digit-recognition-using-scikit-learn>

<https://dev.to/frosnerd/handwritten-digit-recognition-using-convolutional-neural-networks-11g0>

<https://nextjournal.com/gkoehler/digit-recognition-with-keras>

<https://www.digitalocean.com/community/tutorials/how-to-build-a-neural-network-to-recognize-handwritten-digits-with-tensorflow>

<https://medium.com/stocard/recognizing-digits-of-loyalty-cards-using-cnn-and-tesseract-4-78c389dc6f03>

<https://towardsdatascience.com/scanned-digits-recognition-using-k-nearest-neighbor-k-nn-d1a1528f0dea>

<http://www.emaraic.com/blog/multi-digit-segmentation-and-recognition>

<https://wosaku.github.io/digits-recognition.html>

<https://docs.aws.amazon.com/rekognition/latest/dg/text-detection.html>
