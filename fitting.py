from os import listdir
import PIL as pil
import cv2
from datetime import datetime
import pandas as pd
import sgolay2 as sgf2
from scipy import signal
import numpy as np
from skimage import exposure
import matplotlib.pyplot as plt


def get_image(file):
    return cv2.imread('images/'+file, cv2.IMREAD_ANYDEPTH | cv2.IMREAD_GRAYSCALE)

def filter_image(image):
    return sgf2.SGolayFilter2(window_size=9, poly_order=3)(image)

def contrast_image(image):
    return exposure.rescale_intensity(image, in_range=tuple(np.percentile(image, (10.0, 95.0))))

def convolve_image(image):
    return signal.convolve(image, [[-1.], [-1.], [-1.],
                                    [-1.], [8.], [-1.],
                                    [-1.], [-1.], [-1.]])

def save_data(data):
    try:
        pd.read_csv('data.csv')
        header = False
    except:
        header = True
    data.to_csv('data.csv', mode='a', header=header, index=False)

def get_files():
    try:
        df = pd.read_csv('data.csv')
    except: df = pd.DataFrame(columns=[1])
    print(df)
    if df.empty:
        return [file for file in listdir('images/') if file.endswith('tiff')]
    else:
        return [file for file in listdir('images/') if file.endswith('tiff') and not(df['filename'].str.contains(file).any())]

def run():
    files = get_files()
    for i in files:
        img = get_image(i)
        time = datetime.now()
        con_img = convolve_image(contrast_image(img))
        filter_img = filter_image(con_img)
        sur = abs((filter_img))>np.max(filter_img)*0.2
        sur = np.where(sur==True)
        k = np.max(sur)
        surr= (sur[0]/k,sur[1]/k)
        #fitt_ellipse
        el_x = None
        el_y = None
        el_maj = None
        el_min = None
        el_ang = None
        time = datetime.now()-time
        time = time.total_seconds()*1000
        data = {
            'filename': [i],
            'ellipse_center_x': [el_x],
            'ellipse_center_y': [el_y],
            'ellipse_majoraxis': [el_maj],
            'ellipse_minoraxis': [el_min],
            'ellipse_angle': [el_ang],
            'elapsed_time': [time],
        }
        save_data(pd.DataFrame(data))

if __name__=='__main__':
    run()

