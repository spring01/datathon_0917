
import numpy as np
import cPickle as pickle
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten

with open('inter_dis_score.p', 'rb') as pic:
    all_inter, all_target, all_score, sig_diseases = pickle.load(pic)

all_inter = all_inter.astype(np.float64)

num_feat = all_inter.shape[1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(all_inter, all_score, test_size=0.33)


model = Sequential()
model.add(Dense(200, input_dim=num_feat, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(200, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(1))
model.compile(loss=keras.losses.mse,
              optimizer=keras.optimizers.Adam(), metrics = ['accuracy'])

model.fit(X_train, y_train,
          batch_size=128,
          epochs=10,
          verbose=1,
validation_data=(X_test, y_test))

