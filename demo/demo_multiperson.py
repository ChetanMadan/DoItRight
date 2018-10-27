import os
import sys

import numpy as np
import cv2
sys.path.append(os.path.dirname(__file__) + "/../")

from scipy.misc import imread, imsave

from config import load_config
from dataset.factory import create as create_dataset
from nnet import predict
from util import visualize
from dataset.pose_dataset import data_to_input

from multiperson.detections import extract_detections
from multiperson.predict import SpatialModel, eval_graph, get_person_conf_multicut
from multiperson.visualize import PersonDraw, visualize_detections

import matplotlib.pyplot as plt


cfg = load_config("demo/pose_cfg_multi.yaml")

dataset = create_dataset(cfg)

sm = SpatialModel(cfg)
sm.load()

draw_multi = PersonDraw()

# Load and setup CNN part detector
sess, inputs, outputs = predict.setup_pose_prediction(cfg)
k=0
# Read image from file
dir= os.listdir("written/")
for file in dir:

    file_name = "written/"+file
    image = imread(file_name, mode='RGB')

    image_batch = data_to_input(image)

    # Compute prediction with the CNN
    outputs_np = sess.run(outputs, feed_dict={inputs: image_batch})
    scmap, locref, pairwise_diff = predict.extract_cnn_output(outputs_np, cfg, dataset.pairwise_stats)

    detections = extract_detections(cfg, scmap, locref, pairwise_diff)
    unLab, pos_array, unary_array, pwidx_array, pw_array = eval_graph(sm, detections)
    person_conf_multi = get_person_conf_multicut(sm, unLab, unary_array, pos_array)

    img = np.copy(image)
    #coor = PersonDraw.draw()
    visim_multi = img.copy()

    fig = plt.imshow(visim_multi)
    co1=draw_multi.draw(visim_multi, dataset, person_conf_multi)

    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)

    plt.show()
    visualize.waitforbuttonpress()
    print("this is draw : ", co1)
    qwr = np.zeros((1920,1080,3), np.uint8)

    cv2.line(qwr, co1[5][0], co1[5][1],(255,0,0),3)
    cv2.line(qwr, co1[7][0], co1[7][1],(255,0,0),3)
    cv2.line(qwr, co1[6][0], co1[6][1],(255,0,0),3)
    cv2.line(qwr, co1[4][0], co1[4][1],(255,0,0),3)


    cv2.line(qwr, co1[9][0], co1[9][1],(255,0,0),3)
    cv2.line(qwr, co1[11][0], co1[11][1],(255,0,0),3)
    cv2.line(qwr, co1[8][0], co1[8][1],(255,0,0),3)
    cv2.line(qwr, co1[10][0], co1[10][1],(255,0,0),3)

    cv2.imwrite("stick/frame%d.jpg"%k, qwr)
    k+=1
    cv2.destroyAllWindows()
    qw1 = cv2.cvtColor(qwr, cv2.COLOR_BGR2GRAY)

