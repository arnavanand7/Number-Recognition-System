import pandas as pd
import numpy as np
import time

train_data=pd.read_csv('mnist_train.txt')
features_train=np.array(train_data.drop(['label'],1))
labels_train=np.array(train_data['label'])


test_data=pd.read_csv('mnist_test.txt')
features_test=np.array(test_data.drop(['label'],1))
labels_test=np.array(test_data['label'])

print("Using KNN:")
from sklearn import neighbors
clf=neighbors.KNeighborsClassifier(n_neighbors=5)

t0=time.time()
clf.fit(features_train,labels_train)
t1=time.time()
time1=t1-t0
print("Training Time=",time1)

##feature_test=features_test[1:2000]
##label_test=labels_test[1:2000]
t2=time.time()
pre=clf.predict(features_test)
print(pre)
t3=time.time()
time2=t3-t2
print("Testing Time=",time2)
print()
from sklearn.metrics import accuracy_score
acc=accuracy_score(pre,labels_test)
print("Accuracy=",acc)

count0=count1=count2=count3=count4=count5=count6=count7=count8=count9=0
for i in range(0,len(labels_test)):
    if pre[i]!=labels_test[i]:
##        print("Predicted=",pre[i])
##        print("Actual Digit=",labels_test[i])
          if labels_test[i]==0:
              count0+=1
          elif labels_test[i]==1:
              count1+=1
          elif labels_test[i]==2:
              count2+=1
          elif labels_test[i]==3:
              count3+=1
          elif labels_test[i]==4:
              count4+=1
          elif labels_test[i]==5:
              count5+=1
          elif labels_test[i]==6:
              count6+=1
          elif labels_test[i]==7:
              count7+=1
          elif labels_test[i]==8:
              count8+=1
          else:
              count9+=1
print(count0,count1,count2,count3,count4,count5,count6,count7,count8,count9)
            

            


