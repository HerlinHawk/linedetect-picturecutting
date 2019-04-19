import os
import numpy as np
import cv2 as cv
import skimage.morphology as skm
import matplotlib.pyplot as plt
import sklearn.cluster as skclus
root_path = os.getcwd()
#print(root_path)
print(type(os.listdir(root_path)))
#listdir ['.idea', 'depart', 'origin', 'segement.py']

#to save the segment picture
def make_segment_dir(root_path):
    segment_path = os.path.join(root_path, 'depart')
    if 'depart' not in os.listdir(root_path):
        os.mkdir(os.path.join(root_path,'depart'))
    else: print('directory already existed:',segment_path)
    return segment_path
segment_dir = make_segment_dir(root_path)
print(segment_dir)
def find_origin_data_dir(root_path):
    for root, dir, file_name in os.walk(root_path):
        #print(file_name,dir,root)
        for a in dir:
            #print(a)
            if a == 'origin':
                data_path = os.path.join(root_path,a)
                #print(data_path)

    return data_path

data_path = find_origin_data_dir(root_path)

def cut_picture(data_path,segment_path):
    images_name = []
    file_name = []
    i=0
    for file in os.listdir(data_path):
        #print(images)
        file_name.append(file)
        images_name.append(data_path+'\\'+file)
    for image_name in  images_name:
        print(image_name)
        im = cv.imread(image_name)
        #cv.imshow('origin_pic',im)
        im = cv.Canny(im,100,200)
        #cv.imshow('edgs1', im)
        im = cv.Canny(im,150,200)
        #cv.Canny(object,tresh1,trsh2)
        #cv.imshow('edgs2',im)
        ##corrosion and expand


        ##cut the pic into 25 pieces and save to segment_path
        width, height= im.shape
        pieces = np.zeros((int(width/5),int(height/5)))  #form should be zeros((n,m))2dimesion array
        #print(im.shape) #1792,2560
        #im = skm.remove_small_holes(im,100,in_place=False)
        print(type(im))#remove  the holes
        im = cv.GaussianBlur(im, (15,15),1)
        plt.imshow(im)
        im = skm.remove_small_objects(im, 20,in_place=False) #(oject,size(remove oject size),return bool?)

        print(type(im))

        plt.show()
        for wd in range(0,width-2,int(width/5)):
            #print(str(wd)+'a')
            print(wd)
            for hd in range(0,height,int(height/5)):
                a = im[wd:int(wd+width/5),hd:hd+int(height/5)]
                print(a.shape)
                #cv.imwrite(segment_path+'\\'+str(wd)+'_'+str(hd)+file_name[i],a)
                num = np.count_nonzero(a)
                print(num)
                #print(segment_path+'\\'+str(wd)+'_'+str(hd)+file_name[i])
                #cv.imshow('cut'+str(num),a)

        i=i+1
        cv.waitKey(0)
    #print(images_name)
cut_picture(data_path,segment_dir)
