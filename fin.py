
# coding: utf-8

# In[9]:


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


# In[11]:



tf.reset_default_graph()
cfg = load_config("demo/pose_cfg_multi.yaml")

dataset = create_dataset(cfg)

sm = SpatialModel(cfg)
sm.load()

draw_multi = PersonDraw()

# Load and setup CNN part detector
sess, inputs, outputs = predict.setup_pose_prediction(cfg)

# Read image from file
file_name = "demo/try.jpeg"
file_name1='demo/try2.jpeg'
image = imread(file_name,0)
image2=imread(file_name1, 0)

image_batch = data_to_input(image)
image_batch2=data_to_input(image2)
# Compute prediction with the CNN

outputs_np = sess.run(outputs, feed_dict={inputs: image_batch})
outputs_np2 = sess.run(outputs, feed_dict={inputs: image_batch2})

scmap, locref, pairwise_diff = predict.extract_cnn_output(outputs_np, cfg, dataset.pairwise_stats)
scmap2, locref2, pairwise_diff2 = predict.extract_cnn_output(outputs_np2, cfg, dataset.pairwise_stats)


# In[6]:


detections = extract_detections(cfg, scmap, locref, pairwise_diff)
detections2=extract_detections(cfg, scmap2, locref2, pairwise_diff2)

unLab, pos_array, unary_array, pwidx_array, pw_array = eval_graph(sm, detections)
unLab2, pos_array2, unary_array2, pwidx_array2, pw_array2 = eval_graph(sm, detections2)

person_conf_multi = get_person_conf_multicut(sm, unLab, unary_array, pos_array)
person_conf_multi2 = get_person_conf_multicut(sm, unLab2, unary_array2, pos_array2)


img = np.copy(image)
img2= np.copy(image2)
#coor = PersonDraw.draw()
visim_multi = img.copy()
visim_multi2 = img2.copy()

co1=draw_multi.draw(visim_multi, dataset, person_conf_multi)
co2=draw_multi.draw(visim_multi2, dataset, person_conf_multi2)


cv2.imshow('frame',visim_multi2)

cv2.imshow('frame',visim_multi)
cv2.waitKey(0)
cv2.destroyAllWindows()
#plt.show()
visualize.waitforbuttonpress()
print("this is draw : ", co1)


# In[5]:


co1


# In[8]:


qwr = np.zeros((1920,1080,3), np.uint8)

cv2.line(qwr, co1[5][0], co1[5][1],(255,0,0),3)
cv2.line(qwr, co1[7][0], co1[7][1],(255,0,0),3)
cv2.line(qwr, co1[6][0], co1[6][1],(255,0,0),3)
cv2.line(qwr, co1[4][0], co1[4][1],(255,0,0),3)


cv2.line(qwr, co1[9][0], co1[9][1],(255,0,0),3)
cv2.line(qwr, co1[11][0], co1[11][1],(255,0,0),3)
cv2.line(qwr, co1[8][0], co1[8][1],(255,0,0),3)
cv2.line(qwr, co1[10][0], co1[10][1],(255,0,0),3)


qwr2 = np.zeros((1920,1080,3), np.uint8)

cv2.line(qwr2, co2[5][0], co2[5][1],(255,0,0),3)
cv2.line(qwr2, co2[7][0], co2[7][1],(255,0,0),3)
cv2.line(qwr2, co2[6][0], co2[6][1],(255,0,0),3)
cv2.line(qwr2, co2[4][0], co2[4][1],(255,0,0),3)


cv2.line(qwr2, co2[9][0], co2[9][1],(255,0,0),3)
cv2.line(qwr2, co2[11][0], co2[11][1],(255,0,0),3)
cv2.line(qwr2, co2[8][0], co2[8][1],(255,0,0),3)
cv2.line(qwr2, co2[10][0], co2[10][1],(255,0,0),3)


# In[9]:


cv2.imshow('r',qwr)
cv2.imshow('r2', qwr2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


qw1 = cv2.cvtColor(qwr, cv2.COLOR_BGR2GRAY)
qw2= cv2.cvtColor(qwr2, cv2.COLOR_BGR2GRAY)


# In[ ]:


fig = plt.figure("Images")
images = ("Original", qw1), ("Contrast", qw2)
for (i, (name, image)) in enumerate(images):
    ax = fig.add_subplot(1, 3, i + 1)
    ax.set_title(name)
    cv2.imshow('fr',image)


# compare the images
s,m=compare_images(qw1, qw2, "Image1 vs Image2")


if(s>0.5 and m<=1000):
        print("The person is present in the database - printing details ")
else:
        print("This person is not on the predefined dataset - employ web scraping script")
        
            
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


s


# In[ ]:


m

