import os
import numpy
import cv2
import matplotlib as plt
import pickle 
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

dir = 'Dataset_post/test'

categories = ['cats','dogs']
# data = []
desired_size = (512, 512)

#----------------------------------------------------
#Normalization of the dataset

# for category in categories:
#     path = os.path.join(dir,category)
#     label = categories.index(category)

#     for img in os.listdir(path):
#         imgpath = os.path.join(path,img)
#         w_img = cv2.imread(imgpath,0)
#     try:
#         # Convert the image to grayscale
#         gray_image = cv2.cvtColor(w_img, cv2.COLOR_BGR2GRAY)
#         # Resize the image to the desired size
#         resized_image = cv2.resize(gray_image, desired_size)
#         # Add normalized image to the data array
#         data.append([resized_image,label])
#     except Exception as e:
#         pass
#-----------------------------------------------------------
# Transformation/Serialization with Pickle -> Binary save

# pick_in = open('data','wb')
# pickle.dump(data,pick_in)
# pick_in.close()

#-------------------------------------------------
# Load an randomnize the transform dataset

pick_in = open('data','rb')
data = pickle.load(pick_in)
pick_in.close()

random.shuffle(data)
features = []
labels = []

for feature, label in data:
    features.append(feature)
    labels.append(label)

print("hola")
print (data)
#-----------------------------------------
# Importing the model for the SVM

# xtrain, xtest, ytrain, ytest = train_test_split(features,labels, test_size = 0.3, random_state=42, train_size=0.7)

# model = SVC(C=1,kernel = 'poly', gamma = 'auto')
# model.fit(xtrain,ytrain)

# pick = open('model_1.sav','wb')
# pickle.dump(model,pick)
# pick.close()

# prediction = model.predict(xtest)
# accuracy = model.score(xtest, ytest)

# categories = ['Cat','Dog']

# print('Accuracy', accuracy)
# print('Prediction is : ', categories[prediction[0]])

# w_img = xtest[0].reshape(50,50)
# plt.imshow(w_img,cmap='gray')
# plt.show()