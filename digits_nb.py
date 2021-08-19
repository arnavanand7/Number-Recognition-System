import pandas as pd
import numpy as np
import time

train_data=pd.read_csv('mnist_train.txt')
features_train=np.array(train_data.drop(['label'],1))
labels_train=np.array(train_data['label'])


test_data=pd.read_csv('mnist_test.txt')
features_test=np.array(test_data.drop(['label'],1))
labels_test=np.array(test_data['label'])

print("Using Naive Bayes:")
from sklearn.naive_bayes import GaussianNB
clf=GaussianNB()
t0=time.time()
clf.fit(features_train,labels_train)
t1=time.time()
time1=t1-t0
print("Training Time=",time1)
t2=time.time()
pre=clf.predict(features_test)
print(pre)
t3=time.time()
time2=t3-t2
print("Testing Time=",time2)
from sklearn.metrics import accuracy_score
acc=accuracy_score(pre,labels_test)
print("Accuracy=",acc)
print(labels_test)
