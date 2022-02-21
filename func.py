import cv2 as cv
import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv.imread(cv.samples.findFile("lenna.png"),)
#img = cv.imread(cv.samples.findFile("pawian.jpg"))




def original_img(img):
    cv2.imshow('image',img)
    cv2.waitKey(0)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Orginalne.png', img)
    return img
def inverted_img(img):
    img_i = (255-img)
    cv2.imshow('inverted', img_i)
    cv2.waitKey(0)
    return img_i
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Inverted.png', img_i)

def grey_img(img):
    img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grey', img_g)
    cv2.waitKey(0)
    return img_g
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Grey.png', img_g)



def scaleup_img(img,sf_x,sf_y):

    #img_su = cv2.resize(img, None, fx=float(sf_x), fy=float(sf_y))
    img_su = cv2.resize(img, None, fx=sf_x, fy= sf_y)
    cv2.imshow('scale up', img_su)
    cv2.waitKey(0)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Zwiększenie_skali.png', img)
    return img_su

def scaledown_img(img,sf_x,sf_y):
    img_sd1 = cv2.resize(img, None, fx=float(sf_x), fy=float(sf_y))
    print('SCALE DOWN ON LINE')
    cv2.imshow('scale down', img_sd1)
    cv2.waitKey(0)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Zmniejszenie_skali.png', img_sd1)
    return img_sd1

def gauss_img(img):
    img_g = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imshow('gauss', img_g)
    cv2.waitKey(0)
    return img_g

    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/gauss.png', img_g)
def sepia_img(img):
    img_s = cv2.transform(img, np.matrix([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]]))
    cv2.imshow('sepia', img_s)
    cv2.waitKey(0)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Sepia.png', img_s)
    return img_s

def convert_img(img):
    img_c = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    cv2.imshow('convert', img_c)
    cv2.waitKey(0)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/HSV.png', img_c)
    return img_c

def rotate_img(img):
    img_r = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('rotate', img_r)
    cv2.waitKey(0)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Rotate_90.png', img_r)
    return img_r

def brightnesschange_img(img):
    value = 30
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(img_hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    img_output = cv2.merge((h, s, v))
    img_bc = cv2.cvtColor(img_output, cv2.COLOR_HSV2BGR)
    cv2.imshow('brightnesschange', img_bc)
    cv2.waitKey(0)
    return img_bc
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Zmiana_jasnosci.png', img_bc)

def edge_img(img):
    img_ed = cv2.Canny(img, 100, 300)
    cv2.imshow('edge detection', img_ed)
    cv2.waitKey(0)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Wykrycie_krawedzi.png', img_ed)

def erosion_img(img):
    img_er = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    img_erosion = cv2.erode(img_er, kernel, iterations=1)
    cv2.imshow('erosion', img_erosion)
    cv2.waitKey(0)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Erozja.png', img_er)

def dilation_img(img):
    img_d = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    img_dilation = cv2.dilate(img_d, kernel, iterations=1)
    cv2.imshow('dilation', img_dilation)
    cv2.waitKey(0)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Dylatacja.png', img_d)




def skeletonization_img(img):
    img_s = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img_s = cv2.threshold(img_s, 127, 255, 0)
    skel = np.zeros(img_s.shape, np.uint8)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    while True:
        open_s = cv2.morphologyEx(img_s, cv2.MORPH_OPEN, element)
        temp = cv2.subtract(img_s, open_s)
        eroded = cv2.erode(img_s, element)
        skel = cv2.bitwise_or(skel, temp)
        img_s = eroded.copy()

        if cv2.countNonZero(img_s) == 0:
            break

    cv2.imshow('skeletonization', skel)
    cv2.waitKey(0)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Szkieletyzacja.png', skel)




def rotate_angle60(img):
    img = cv.imread(cv.samples.findFile("lenna.png"), 0)
    rows,cols = img.shape
    M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),60,1)
    dst = cv.warpAffine(img,M,(cols,rows))
    flipped = cv.flip(img,1)
    cv.imshow("Rotation",dst)
    cv.waitKey(0)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Rotate_60.png', dst)
    cv.imshow("odbicie lustrzane", flipped)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Odbicie_lustrzane.png', flipped)
    cv.waitKey(0)

def resolution(img):
    #src = cv2.imread('D:/cv2-resize-image-original.png', cv2.IMREAD_UNCHANGED)

    # set a new height in pixels
    new_height = 700

    # dsize
    dsize = (img.shape[1], new_height)

    # resize image
    output = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)

    #cv2.imwrite('resize-image-height.png', output)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Zmiana_rozdzielczosci.png', output)
    cv.imshow("Dif res",output)
    cv.waitKey(0)


def two_in_one(img):
    img1 = cv.imread('lenna.png')
    img2 = cv.imread('pawian.jpg')
    dsize = (512, 512)
    # resize image
    output = cv2.resize(img2, dsize, interpolation=cv2.INTER_AREA)
    # cv2.imwrite('resize-image-height.png', output)

    #dst2 = cv2.add(img1,output)
    dst2 = cv.multiply(img1,output)

    dst = cv.addWeighted(img1, 0.5, output, 0.5, 0)
    cv.imshow('dodawanie', dst)
    cv.waitKey(0)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Dodawanie_obrazow.png', dst)
    cv.imshow('mnozenie', dst2)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Mnozenie_obrazow.png', dst2)
    cv.waitKey(0)



def my_LUT(img):

    cv.imshow('orginal',img)
    cv.waitKey(0)
    contrast_factor=2
    table = np.array([(i - 74) * contrast_factor + 74 for i in range(0, 256)]).clip(0, 255).astype('uint8')

    if img.shape[2] == 1:
        outpu1= cv2.LUT(img, table)[:, :, np.newaxis]
        cv.imshow('LUTB', outpu1)
        cv.waitKey(0)
    else:
        output2= cv2.LUT(img, table)
    cv.imshow('LUTA',output2)
    cv.waitKey(0)


def bin():
    img = cv.imread('lenna.png', 0)
    ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    # ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
    # ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
    # ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
    # ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
    titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    cv.imshow('binaryzacja',thresh1)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Binaryzacja.png', thresh1)
    cv.waitKey(0)

def andorxor():
    img = cv.imread('lenna.png', 0)
    img2 = cv.imread('pawian.jpg',0)

    dsize = (512, 512)
    # resize image
    output = cv2.resize(img2, dsize, interpolation=cv2.INTER_AREA)
    ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    ret, thresh2 = cv.threshold(output, 127, 255, cv.THRESH_BINARY)
    # ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
    # ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
    # ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
    # ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
    titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    bitwiseAnd = cv2.bitwise_and(thresh1,thresh2)
    bitwiseOR = cv2.bitwise_or(thresh1, thresh2)
    bitwiseXOR = cv2.bitwise_xor(thresh1, thresh2)
    cv.imshow('OR', bitwiseOR)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/OR.png', bitwiseOR)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/XOR.png', bitwiseXOR)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/AND.png', bitwiseAnd)
    cv.waitKey(0)
    cv.imshow('XOR', bitwiseXOR)
    cv.waitKey(0)
    cv.imshow('AND', bitwiseAnd)
    cv.waitKey(0)


def furrier ():
    img12 = cv.imread('pawian.jpg', 0)
    f = np.fft.fft2(img12)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))
    cv2.imshow('cos',magnitude_spectrum)
    cv2.waitKey(0)
    plt.subplot(121), plt.imshow(img12, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

def furrier2():
    img13 = cv.imread('pawian.jpg', 0)

    dft = cv.dft(np.float32(img13), flags=cv.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
    plt.subplot(121), plt.imshow(img13, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

def compression():
    #compression_params = [cv2.CV_IMWRITE_PNG_COMPRESSION, 9]
    img = cv2.imread('lenna.png', cv2.IMREAD_UNCHANGED)
    #cv2.imwrite('Lena_compressed.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 0])
    #cv2.imwrite('Lena_compressed2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 9])
    img3 = cv2.imread('Lena_compressed.jpg', cv2.IMREAD_UNCHANGED)
    cv2.imshow('kompresja', img3)
    cv2.waitKey(0)

def hist2(img):
    histg = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(histg)
    plt.show()
def coloro(img):
    b1 = img[:, :, 0]
    b2 = img[:, :, 1]
    # b3=img2[:,:,2]

    b = img.copy()
    # set green and red channels to 0
    b[:, :, 1] = 0
    b[:, :, 2] = 0

    r = img.copy()
    # set green and red channels to 0
    r[:, :, 0] = 0
    r[:, :, 1] = 0

    br = cv.add(b, r)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/BLUE.png', b)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/RED.png', r)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/BLUE_RED.png', br)
    # cv2.imwrite('G:\Programing\Python 2.0\obrazy_wynikowe/Grey_channel_1.png', b1)
    cv.imshow('blue', b)
    cv.imshow('red', r)
    cv.imshow('bred', br)
    cv.imshow('b1', b1)
    cv.imshow('b2', b2)

    cv.waitKey(0)

