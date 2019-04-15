import time
import math
import imutils
import os
import sys
import numpy as np
import cv2
from scipy.misc import imread, imsave
from skimage.measure import compare_ssim as ssim
from config import load_config
from dataset.factory import create as create_dataset
from nnet import predict
from util import visualize
import cv2
from dataset.pose_dataset import data_to_input

from multiperson.detections import extract_detections
from multiperson.predict import SpatialModel, eval_graph, get_person_conf_multicut
from multiperson.visualize import PersonDraw, visualize_detections
import matplotlib.pyplot as plt
import tensorflow as tf
from tkinter import messagebox

slopes=[]
def vibrate(key):
    os.system('play  --null --channels 1 synth %s sine %f' % (1, 500))

def compare_images(slope1, slope2, allowance):
    for key in slope1:
        if abs(slope1[key]-slope2[key]) > allowance:
            vibrate(key)
            print("error at : ", key)
            return (key,slope1[key]-slope2[key])


def slope_calc(co1):
    body_dict={'nose_right': co1[0],
               'nose_left': co1[1],
              'right_eye_ear': co1[2],
              'left_eye_ear': co1[3],
              'right_upper_arm':co1[4],
              'left_upper_arm':co1[5],
              'right_forearm': co1[6],
              'left_forearm': co1[7],
               'right_upper_leg':co1[8],
               'left_upper_leg':co1[9],
               'right_shin':co1[10],
               'left_shin':co1[11]
              }
    body_dict['backbone']=[(int((body_dict['right_upper_arm'][0][0]+body_dict['left_upper_arm'][0][0])/2),
                           int((body_dict['right_upper_arm'][0][1]+body_dict['left_upper_arm'][0][1])/2)),
                           (int((body_dict['right_upper_leg'][0][0]+body_dict['left_upper_leg'][0][0])/2),
                           int((body_dict['right_upper_leg'][0][1]+body_dict['left_upper_leg'][0][1])/2))]
    for key in body_dict:
        a=math.atan((body_dict['backbone'][1][1]-body_dict['backbone'][0][1])/(body_dict['backbone'][0][0]-body_dict['backbone'][1][0]))
        slopes[key]=(math.atan((body_dict[key][1][1]-body_dict[key][0][1])/(body_dict[key][0][0]-body_dict[key][1][0])))-a
    return slopes



def run_predict(frame, sess, inputs, outputs, cfg, dataset, sm, draw_multi):

    tf.reset_default_graph()
    image= frame
    image_batch = data_to_input(frame)

    # Compute prediction_n with the CNN
    outputs_np = sess.run(outputs, feed_dict={inputs: image_batch})
    scmap, locref, pairwise_diff = predict.extract_cnn_output(outputs_np, cfg, dataset.pairwise_stats)
    detections = extract_detections(cfg, scmap, locref, pairwise_diff)
    unLab, pos_array, unary_array, pwidx_array, pw_array = eval_graph(sm, detections)
    m=time.time()
    person_conf_multi = get_person_conf_multicut(sm, unLab, unary_array, pos_array)
    img = np.copy(image)
    visim_multi = img.copy()
    draw_multi.draw(visim_multi, dataset, person_conf_multi, image)
    return pos_array.round().astype(int)


def main(option):
    cfg = load_config("demo/pose_cfg_multi.yaml")
    dataset=create_dataset(cfg)
    sm = SpatialModel(cfg)
    sm.load()
    tf.reset_default_graph()
    draw_multi = PersonDraw()
    sess, inputs, outputs = predict.setup_pose_prediction(cfg)
    fps_time=0
    # Read image from file
    cap=cv2.VideoCapture('msgifs/icon4.gif')
    cap_user=cv2.VideoCapture('user.mp4')
    i=0
    while (True):
        ret, orig_frame= cap.read()
        ret2, orig_frame_user= cap_user.read()
        if i%25 == 0:

            frame = cv2.resize(orig_frame, (0, 0), fx=0.50, fy=0.50)
            user_frame=cv2.resize(orig_frame_user, (0, 0), fx=0.50, fy=0.50)
            co1=run_predict(frame, sess, inputs, outputs, cfg, dataset, sm, draw_multi)
            user_co1=run_predict(user_frame, sess, inputs, outputs, cfg, dataset, sm, draw_multi)
            try:
                slope_reqd=slope_calc(co1)
                slope_user=slope_calc(user_co1)
                compare_images(slope_reqd, slope_user, 0.1)
            except IndexError:
                #if len(co1)!=len(user_co1):
                #messagebox.showinfo("Title", "Please adjust camera to show your keypoints")
                pass
            #frame = cv2.resize(frame, (0, 0), fx=2.0, fy=2.0)
            #user_frame = cv2.resize(user_frame, (0, 0), fx=2.0, fy=2.0)
            cv2.putText(user_frame,
                        "FPS: %f" % (1.0 / (time.time() - fps_time)),
                        (10, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 255, 0), 2)

            cv2.imshow('user_frame', user_frame)
            cv2.imshow('frame', frame)
            fps_time=time.time()
            #visualize.waitforbuttonpress()
            if cv2.waitKey(10)==ord('q'):
                break
    cap.release()
    cap_user.release()
    cv2.destroyAllWindows()
    cap_user.release()
