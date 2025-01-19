from PIL import Image
import wget
import matplotlib.pyplot as plt
import numpy as np
#url = 'https://raw.githubusercontent.com/jonkrohn/DLTFpT/master/notebooks/oboe-with-book.jpg'
url = 'https://www.jesusbasail.com/Bio/mypic.jpg'
#filename = wget.download(url)
img = wget.download(url)
img = Image.open('mypic.jpg')
imggray = img.convert('LA')
imgmat = np.array(list(imggray.getdata(band=0)), float)
imgmat.shape = (imggray.size[1], imggray.size[0])
imgmat = np.matrix(imgmat)
#plt.imshow(imggray)
plt.imshow(imgmat, cmap='gray')
plt.show()

#Now we will reconstruct the image:

U, sigma, V = np.linalg.svd(imgmat) # calculate the SVD of the matrix (image)
#print(U,sigma,V)

#Using only the most significant singular vectors and value
reconstimg = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
_ = plt.imshow(reconstimg, cmap='gray')
plt.show()

#increasing the singular matrix in different sizes
for i in [2, 4, 8, 16, 32, 64]:
    reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
    plt.imshow(reconstimg, cmap='gray')
    title = "n = %s" % i
    plt.title(title)
    plt.show()

#comparing:
print("imgmat.shape",imgmat.shape)
full_representation =  imgmat.shape[0]*imgmat.shape[1]
print("full_representation= ",full_representation)
svd64_rep = 64*imgmat.shape[0] + 64 + 64*imgmat.shape[1]
print("svd64_r =",svd64_rep)
print("svd64_rep/full_representation =", svd64_rep/full_representation)