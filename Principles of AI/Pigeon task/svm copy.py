from PIL import Image
import joblib as jl
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

import os

def read_and_display_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Display the image
        #img.show()

        # Print some image properties
        print(f'Format: {img.format}')
        print(f'Size: {img.size}')
        print(f'Mode: {img.mode}')
        img_matrix = np.array(img)
        print(img_matrix[150:153, 300:400])
        #plt.imshow(img_matrix)
        #plt.title('Image as Matrix')
        #plt.axis('off')  # Hide the axes
        #plt.show()
        #matrix_section = img_matrix[150:310, 300:400]

        # Display the image matrix section
        #plt.imshow(matrix_section)
        #plt.title('Image Matrix Section (Rows 300-350, Columns 300-350)')
        #plt.axis('off')  # Hide the axes
        #plt.show()

        # Print the matrix
        #print(img_matrix)
def load_images_from_false():
    images = []
    for i in range(1,5):
        directory = "../dataset/false/" + str(i)

# List all files and directories
        files_and_dirs = os.listdir(directory)

# Filter to only list files
        files = [f for f in files_and_dirs if os.path.isfile(os.path.join(directory, f)) and f != ".DS_Store"]

        for fname in files:
            image_path = directory+"/"+str(fname)
            with Image.open(image_path) as img:
                # Display the image
                #img.show()
                # Print some image properties
                img = img.resize((1920, 1080))
                images.append(np.array(img).flatten())  # Flatten the image
            
        #print(img_matrix[150:153, 300:400])
        #img = img.resize((64, 64))  # Resize images to 64x64
        
   # for i in range(57, 1877):
       # image_path = '/Users/kalpanajohari/Downloads/images/off/captured_image_'+ str(i) +'.jpg'
       # with Image.open(image_path) as img:
        # Display the image
        #img.show()

        # Print some image properties
            #print(f'Format: {img.format}')
            #print(f'Size: {img.size}')
            #print(f'Mode: {img.mode}')
           # img = img.resize((640, 480))
           # images.append(np.array(img).flatten())  # Flatten the image
    return images
def load_images_from_true():
    images = []
    for i in range(1,5):
        directory = "./dataset/true/" + str(i)

# List all files and directories
        files_and_dirs = os.listdir(directory)

# Filter to only list files
        files = [f for f in files_and_dirs if os.path.isfile(os.path.join(directory, f)) and f != ".DS_Store"]

        for fname in files:
            image_path = directory+"/"+str(fname)
            with Image.open(image_path) as img:
                #img = img.resize((640, 480))
                img = img.resize((1920, 1080))
                images.append(np.array(img).flatten())  # Flatten the image
            
        #print(img_matrix[150:153, 300:400])
        #img = img.resize((64, 64))  # Resize images to 64x64
    
    return images

# Load images from folders
class1_images = load_images_from_false()
class2_images = load_images_from_true()

# Create labels
class1_labels = [0] * len(class1_images)
class2_labels = [1] * len(class2_images)

# Combine images and labels
images = np.array(class1_images + class2_images)
labels = np.array(class1_labels + class2_labels)
print("All images array flatten")
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

filename = '/Users/kalpanajohari/Downloads/monkey_model.sav'
jl.dump(svm_model, filename)

#print(X_test)
y_pred = svm_model.predict(X_test)
print(y_pred)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
#check the model

image_path = '/Users/kalpanajohari/Downloads/TestDataMonkey/MonkeyTest1.jpg'
with Image.open(image_path) as img:
    images1 = []
        # Display the image
        #img.show()

        # Print some image properties
            #print(f'Format: {img.format}')
            #print(f'Size: {img.size}')
            #print(f'Mode: {img.mode}')
    img = img.resize((1920, 1080))
    images1.append(np.array(img).flatten())  # Flatten the image
            
        #print(img_matrix[150:153, 300:400])
        #img = img.resize((64, 64))  # Resize images to 64x64
        
    
y_pred1 = svm_model.predict(images1)
print("Final Result", y_pred1)