import time
import math
import imutils
import os
import sys
import numpy as np
import cv2
from scipy.misc import imread, imsave
from skimage.measure import structural_similarity as ssim
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

def vibrate(key):
    os.system('play  --null --channels 1 synth %s sine %f' % (1, 500))


def compare_images(slope1, slope2, allowance):
    for key in slope1:
        print(key,slope1[key]-slope2[key])
        if abs(slope1[key]-slope2[key]) > allowance:
            vibrate(key)
            print("error at : ", key)
            return (key,slope1[key]-slope2[key])

def slope_calc(co1, co2):
    body_dict={'right_upper_arm':co1[4],
              'left_upper_arm':co1[5],
               'right_upper_leg':co1[8],
               'left_upper_leg':co1[9]
              }
    slopes={}
    slopes_user={}
    body_dict['backbone_top']=np.array([int((body_dict['right_upper_arm'][0]+body_dict['left_upper_arm'][0])/2),
                           int((body_dict['right_upper_arm'][1]+body_dict['left_upper_arm'][1])/2)])
    body_dict['backbone_bottom']=np.array([int((body_dict['right_upper_leg'][0]+body_dict['left_upper_leg'][0])/2),
                           int((body_dict['right_upper_leg'][1]+body_dict['left_upper_leg'][1])/2)])

    body_dict_lines={
        'backbone':(body_dict['backbone_top'], body_dict['backbone_bottom']),
        'nose_right':(co1[0],co1[1]),
        'nose_left': (co1[0], co1[2]),
        'right_eye_ear': (co1[1], co1[3]),
        'left_eye_ear':(co1[2],co1[4]),
        'right_upper_arm':(co1[5],co1[7]),
        'left_upper_arm':(co1[6],co1[8]),
        'right_forearm': (co1[7],co1[9]),
        'left_forearm': (co1[8],co1[10]),
        'right_upper_leg':(co1[11],co1[13]),
        'left_upper_leg':(co1[12],co1[14]),
        'right_shin':(co1[13],co1[15]),
        'left_shin':(co1[14],co1[16])
    }
    for key in body_dict_lines:
        a=math.atan((body_dict_lines['backbone'][1][1]-body_dict_lines['backbone'][0][1])/(body_dict_lines['backbone'][0][0]-body_dict_lines['backbone'][1][0]))
        slopes[key]=(math.atan((body_dict_lines[key][1][1]-body_dict_lines[key][0][1])/(body_dict_lines[key][0][0]-body_dict_lines[key][1][0])))-a


    body_dict_user={'right_upper_arm':co2[4],
              'left_upper_arm':co2[5],
               'right_upper_leg':co2[8],
               'left_upper_leg':co2[9]
              }
    body_dict_user['backbone_top']=np.array([int((body_dict_user['right_upper_arm'][0]+body_dict_user['left_upper_arm'][0])/2),
                           int((body_dict_user['right_upper_arm'][1]+body_dict_user['left_upper_arm'][1])/2)])
    body_dict_user['backbone_bottom']=np.array([int((body_dict_user['right_upper_leg'][0]+body_dict_user['left_upper_leg'][0])/2),
                           int((body_dict_user['right_upper_leg'][1]+body_dict_user['left_upper_leg'][1])/2)])

    body_dict_lines_user={
        'backbone':(body_dict_user['backbone_top'], body_dict_user['backbone_bottom']),
        'nose_right':(co2[0],co2[1]),
        'nose_left': (co2[0], co2[2]),
        'right_eye_ear': (co2[1], co2[3]),
        'left_eye_ear':(co2[2],co2[4]),
        'right_upper_arm':(co2[5],co2[7]),
        'left_upper_arm':(co2[6],co2[8]),
        'right_forearm': (co2[7],co2[9]),
        'left_forearm': (co2[8],co2[10]),
        'right_upper_leg':(co2[11],co2[13]),
        'left_upper_leg':(co2[12],co2[14]),
        'right_shin':(co2[13],co2[15]),
        'left_shin':(co2[14],co2[16])
    }


    for key in body_dict_lines_user:
        b=math.atan((body_dict_lines_user['backbone'][1][1]-body_dict_lines_user['backbone'][0][1])/(body_dict_lines_user['backbone'][0][0]-body_dict_lines_user['backbone'][1][0]))
        slopes_user[key]=(math.atan((body_dict_lines_user[key][1][1]-body_dict_lines_user[key][0][1])/(body_dict_lines_user[key][0][0]-body_dict_lines_user[key][1][0])))-a

    return slopes, slopes_user



def run_predict(frame, sess, outputs, inputs, cfg, dataset,sm, draw_multi):

    # Load and setup CNN part detector
    #tf.reset_default_graph()
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
    #coor = PersonDraw.draw()
    visim_multi = img.copy()
    co1=draw_multi.draw(visim_multi, dataset, person_conf_multi, image)
    return pos_array


def main(option):
    start_time=time.time()
    cfg = load_config("demo/pose_cfg_multi.yaml")
    dataset=create_dataset(cfg)
    sm = SpatialModel(cfg)
    sm.load()
    tf.reset_default_graph()
    draw_multi = PersonDraw()
    sess, inputs, outputs = predict.setup_pose_prediction(cfg)
    fps_time=0
    # Read image from file
    slopes={}
    k=0
    cap=cv2.VideoCapture(option)
    cap_user=cv2.VideoCapture(0)
    i=0
    while (True):
        ret, orig_frame= cap.read()
        ret2, orig_frame_user= cap_user.read()
        if i%25 == 0:
            #frame=orig_frame
            frame = cv2.resize(orig_frame, (0, 0), fx=0.50, fy=0.50)
            user_frame=cv2.resize(orig_frame_user, (0, 0), fx=0.50, fy=0.50)
            co1=run_predict(frame, sess, outputs, inputs, cfg, dataset,sm,draw_multi)
            print("CO1            ", co1)
            user_co1=run_predict(user_frame,sess, outputs, inputs,cfg,dataset,sm,draw_multi)
            print("USER_CO1            ", user_co1)
            print("CO1            ", co1)
            try:

                slope_reqd, slope_user=slope_calc(co1, user_co1)
                compare_images(slope_reqd, slope_user, 0.75)
            except IndexError:
                #if len(co1)!=len(user_co1):
                pass
            frame = cv2.resize(frame, (0, 0), fx=2.0, fy=2.0)
            user_frame = cv2.resize(user_frame, (0, 0), fx=2.0, fy=2.0)
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
    elapsed= time.time()-start_time
    cap.release()
    cap_user.release()
    cv2.destroyAllWindows()
