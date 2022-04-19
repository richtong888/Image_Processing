import cv2
from matplotlib import pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 15, 15
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
for i in range(0,99):

    s = '%05d' % i
    imgForTest = 'face_original_img_1/img' +str(s)+ '.jpg'

    img = cv2.imread(imgForTest)  # this is a PIL image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
    plt.imshow(img)
    print(img.shape)
    img = img.reshape((1,) + img.shape)
    print(img.shape)
    #x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    #x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

    datagen = ImageDataGenerator(
        zca_whitening=True,
        rotation_range=30,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=False,
        brightness_range= [0.1,1.5],
        fill_mode='nearest')


    cnt = 0
    for batch in datagen.flow(img, batch_size=1,
                            save_to_dir='face_aug_img_1', save_prefix='face', save_format='png'):
        # plt.subplot(5,4,1 + i)
        # plt.axis("off")
        
        # augImage = batch[0]
        # augImage = augImage.astype('float32')
        # augImage /= 255
        # plt.imshow(augImage)
        
        cnt += 1
        if cnt > 4:
            break  # otherwise the generator would loop indefinitely
    # These output 4 picture
