# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

#from scipy.misc import imread
import cv2

def array_to_image(arr):
    arr = arr.transpose(2,0,1)
    c = arr.shape[0]
    h = arr.shape[1]
    w = arr.shape[2]
    arr = (arr/255.0).flatten()
    data = dn.c_array(dn.c_float, arr)
    im = dn.IMAGE(w,h,c,data)
    return im

def detect2(net, meta, image, thresh=.5, hier_thresh=.5, nms=.45):
    #boxes = dn.make_network_boxes(net)
    #probs = dn.predict_image(net, image)
    #num =   dn.num_boxes(net)
    #dn.network_detect(net, image, thresh, hier_thresh, nms, boxes, probs)
    #res = []
    #for j in range(num):
        #for i in range(meta.classes):
            #if probs[j][i] > 0:
                #res.append((meta.names[i], probs[j][i], (boxes[j].x, boxes[j].y, boxes[j].w, boxes[j].h)))
    #res = sorted(res, key=lambda x: -x[1])
    #dn.free_ptrs(dn.cast(probs, dn.POINTER(dn.c_void_p)), num)
    #return res
    num = dn.c_int(0)
    pnum = dn.pointer(num)
    dn.predict_image(net, im)
    dets = dn.get_network_boxes(net, im.w, im.h, thresh, hier_thresh, None, 0, pnum)
    num = pnum[0]
    if (nms): dn.do_nms_obj(dets, num, meta.classes, nms);

    res = []
    for j in range(num):
        for i in range(meta.classes):
            if dets[j].prob[i] > 0:
                b = dets[j].bbox
                res.append((meta.names[i], dets[j].prob[i], (b.x, b.y, b.w, b.h)))
    res = sorted(res, key=lambda x: -x[1])
    #dn.free_image(im)
    dn.free_detections(dets, num)
    return res


import sys, os
sys.path.append(os.path.join(os.getcwd(),'/home/daniel/htn2020/video_summarizer/darknet/python/'))

import darknet as dn

# Darknet
#net = dn.load_net("cfg/tiny-yolo.cfg", "tiny-yolo.weights", 0)
net = dn.load_net(b"/home/daniel/htn2020/video_summarizer/darknet/cfg/yolov3.cfg", b"/home/daniel/htn2020/video_summarizer/darknet/yolov3.weights", 0)
#meta = dn.load_meta("cfg/coco.data")
meta = dn.load_meta(b"/home/daniel/htn2020/video_summarizer/darknet/cfg/coco.data")
#r = dn.detect(net, meta, "data/dog.jpg")
#r = dn.detect(net, meta, b"/home/daniel/htn2020/video_summarizer/darknet/data/eagle.jpg")
#print(r)

# scipy
#arr= imread('data/dog.jpg')
#im = array_to_image(arr)
#r = detect2(net, meta, im)
#print(r)

# OpenCV
arr = cv2.imread("/home/daniel/htn2020/video_summarizer/darknet/data/eagle.jpg")
im = array_to_image(arr)
dn.rgbgr_image(im)
r = detect2(net, meta, im)
print(r)

