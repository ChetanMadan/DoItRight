
# coding: utf-8

# In[1]:


import os
import sys
import numpy as np
import cv2
#sys.path.append(os.path.dirname(__file__) + "/../")
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


# In[10]:


def mse(imageA,imageB):
    err = np.sum((imageA.astype("float")-imageB.astype("float"))**2)
    err /= float(imageA.shape[0]*imageA.shape[1])
    return err

def compare_images(imageA, imageB, title):
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")
    ax = fig.add_subplot(1, 2, 2)
    
    plt.imshow(imageB, cmap = plt.cm.gray)
    plt.axis("off")
    plt.show()
    
    return(s,m)


# In[6]:


tf.reset_default_graph()
cfg = load_config("demo/pose_cfg_multi.yaml")
dataset = create_dataset(cfg)
sm = SpatialModel(cfg)
sm.load()
draw_multi = PersonDraw()
# Load and setup CNN part detector
sess, inputs, outputs = predict.setup_pose_prediction(cfg)

# Read image from file
dir=os.listdir("stick")
k=0
cap=cv2.VideoCapture(0)
i=0
while True:
        if i%20 == 0:                   
                ret, orig_frame= cap.read()
                frame = cv2.resize(orig_frame, (0, 0), fx=0.30, fy=0.30)
                image= frame
                sse=0
                mse=0
                
                image_batch = data_to_input(frame)

                # Compute prediction with the CNN
                outputs_np = sess.run(outputs, feed_dict={inputs: image_batch})

                scmap, locref, pairwise_diff = predict.extract_cnn_output(outputs_np, cfg, dataset.pairwise_stats)

                detections = extract_detections(cfg, scmap, locref, pairwise_diff)

                unLab, pos_array, unary_array, pwidx_array, pw_array = eval_graph(sm, detections)

                person_conf_multi = get_person_conf_multicut(sm, unLab, unary_array, pos_array)
                img = np.copy(image)
                #coor = PersonDraw.draw()
                visim_multi = img.copy()
                co1=draw_multi.draw(visim_multi, dataset, person_conf_multi)
                plt.imshow(visim_multi)
                cv2.destroyAllWindows()
                #plt.show()
                visualize.waitforbuttonpress()
                #print("this is draw : ", co1)
                if k==1:
                    qwr = np.zeros((1920,1080,3), np.uint8)

                    cv2.line(qwr, co1[5][0], co1[5][1],(255,0,0),3)
                    cv2.line(qwr, co1[7][0], co1[7][1],(255,0,0),3)
                    cv2.line(qwr, co1[6][0], co1[6][1],(255,0,0),3)
                    cv2.line(qwr, co1[4][0], co1[4][1],(255,0,0),3)

                    cv2.line(qwr, co1[9][0], co1[9][1],(255,0,0),3)
                    cv2.line(qwr, co1[11][0], co1[11][1],(255,0,0),3)
                    cv2.line(qwr, co1[8][0], co1[8][1],(255,0,0),3)
                    cv2.line(qwr, co1[10][0], co1[10][1],(255,0,0),3)
                    # In[9]:
                    cv2.imshow('r',qwr)
                    qwr2="stick/frame"+str(k)+".jpg"
                    qw1 = cv2.cvtColor(qwr, cv2.COLOR_BGR2GRAY)
                    qw2= cv2.cvtColor(qwr2, cv2.COLOR_BGR2GRAY)

                    fig = plt.figure("Images")
                    images = ("Original", qw1), ("Contrast", qw2)
                    for (i, (name, image)) in enumerate(images):
                            ax = fig.add_subplot(1, 3, i + 1)
                            ax.set_title(name)
                    plt.imshow(hash(tuple(image)))
                    # compare the images
                    s,m=compare_images(qw1, qw2, "Image1 vs Image2")
                    k+=1
                    sse=s
                    mse=m
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("sse score : ", sse)
                    print("Mean squared error : ", mse)
                    break
                
cap.release()
cv2.destroyAllWindows()

