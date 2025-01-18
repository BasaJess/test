from PIL import Image
import wget
import matplotlib.pyplot as plt
#url = 'https://raw.githubusercontent.com/jonkrohn/DLTFpT/master/notebooks/oboe-with-book.jpg'
url = 'https://www.jesusbasail.com/Bio/mypic.jpg'
#filename = wget.download(url)
img = wget.download(url)
img = Image.open('mypic.jpg')
plt.imshow(img)
plt.show()