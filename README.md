# !!MODIFIED!!
This is an even more fucked-up version of Darknet, that will probably not work on your computer
unless you are either me or Josh (even then, hopefully). Here's what I changed:
* `Makefile` is patched with [tiagoshibata's patch](https://gist.github.com/tiagoshibata/f322466e8b31c14a4b98d53bf74e4f6c)
to work with opencv4, and modified to look for opencv. It will die if you don't have opencv.
* `python/darknet.py` and `examples/detect.py` were modified with small hacks that made them
not die right away with python3, but I also sprinkled in a bunch of my own absolute paths so GLHF
* Also, I set the thing to use `yolov3` with pretrained weights, as you can see in `examples/detect.py`.
you will probably want to `wget` that... 

![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

# Darknet #
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

**Discord** invite link for for communication and questions: https://discord.gg/zSq8rtW

## Scaled-YOLOv4: 

* **paper:** https://arxiv.org/abs/2011.08036

* **source code - Pytorch (use to reproduce results):** https://github.com/WongKinYiu/ScaledYOLOv4

* **source code - Darknet:** https://github.com/AlexeyAB/darknet

* **Medium:** https://alexeyab84.medium.com/scaled-yolo-v4-is-the-best-neural-network-for-object-detection-on-ms-coco-dataset-39dfa22fa982?source=friends_link&sk=c8553bfed861b1a7932f739d26f487c8

## YOLOv4:

* **paper:** https://arxiv.org/abs/2004.10934

* **source code:** https://github.com/AlexeyAB/darknet

* **Wiki:** https://github.com/AlexeyAB/darknet/wiki

* **useful links:** https://medium.com/@alexeyab84/yolov4-the-most-accurate-real-time-neural-network-on-ms-coco-dataset-73adfd3602fe?source=friends_link&sk=6039748846bbcf1d960c3061542591d7

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).

![scaled_yolov4](https://user-images.githubusercontent.com/4096485/101356322-f1f5a180-38a8-11eb-9907-4fe4f188d887.png) AP50:95 - FPS (Tesla V100) Paper: https://arxiv.org/abs/2011.08036

----

![YOLOv4Tiny](https://user-images.githubusercontent.com/4096485/101363015-e5c21200-38b1-11eb-986f-b3e516e05977.png)

----

![YOLOv4](https://user-images.githubusercontent.com/4096485/90338826-06114c80-dff5-11ea-9ba2-8eb63a7409b3.png)


----

![OpenCV_TRT](https://user-images.githubusercontent.com/4096485/90338805-e5e18d80-dff4-11ea-8a68-5710956256ff.png)
