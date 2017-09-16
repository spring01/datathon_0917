
import numpy as np
import cPickle as pickle
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten

with open('chembin_form.p', 'rb') as pic:
    feat_mat, target_mat, all_forms = pickle.load(pic)


feat_mat = feat_mat.astype(np.float64)

num_feat = feat_mat.shape[1]
num_classes = target_mat.shape[1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(feat_mat, target_mat, test_size=0.33)


model = Sequential()
model.add(Dense(200, input_dim=num_feat, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(200, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(), metrics = ['accuracy'])

model.fit(X_train, y_train,
          batch_size=128,
          epochs=20,
          verbose=1,
validation_data=(X_test, y_test))


import matplotlib.pyplot as plt
weights = model.get_weights()[0]
for i in range(weights.shape[1]):
    plt.plot(np.abs(weights[:, i]))
plt.xlabel('Feature')
plt.ylabel('Absolute value of weights')
plt.show()


#~ np.random.choice(range(X_test.shape[0]), replace=False)

#~ model.predict()

