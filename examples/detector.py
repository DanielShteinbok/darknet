# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

import sys, os
sys.path.append(os.path.join(os.getcwd(),'/home/daniel/htn2020/video_summarizer/darknet/python/'))

import darknet as dn
import pdb

dn.set_gpu(0)
net = dn.load_net(b"/home/daniel/htn2020/video_summarizer/darknet/cfg/yolov3.cfg", b"/home/daniel/htn2020/video_summarizer/darknet/yolov3.weights", 0)
meta = dn.load_meta(b"/home/daniel/htn2020/video_summarizer/darknet/cfg/coco.data")
# does not exist
#r = dn.detect(net, meta, b"/home/daniel/htn2020/video_summarizer/darknet/data/bedroom.jpg")
#print(r)

# And then down here you could detect a lot more images like:
r = dn.detect(net, meta, b"/home/daniel/htn2020/video_summarizer/darknet/data/eagle.jpg")
#r = dn.detect(net, b"/home/daniel/htn2020/video_summarizer/darknet/data/eagle.jpg")
print (r)
r = dn.detect(net, meta, b"/home/daniel/htn2020/video_summarizer/darknet/data/giraffe.jpg")
print (r)
r = dn.detect(net, meta, b"/home/daniel/htn2020/video_summarizer/darknet/data/horses.jpg")
print (r)
r = dn.detect(net, meta, b"/home/daniel/htn2020/video_summarizer/darknet/data/person.jpg")
print (r)

