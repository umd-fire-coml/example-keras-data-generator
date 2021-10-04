import numpy as np
from numpy.core.numeric import indices
from tensorflow.keras.utils import Sequence
import cv2
import os
import pathlib

class DataGenerator(Sequence):
    '''this is a random data generator, edit this data generator to read data from dataset folder and return a batch with __getitem__'''

    def __init__(self, batch_size=8, x_shape=(360, 480, 3), y_shape=(1,)):
        self.batch_size = batch_size

        self.x_shape = x_shape
        self.y_shape = y_shape

        self.X = [(pathlib.Path('test/data/images') / filename).as_posix() for filename in os.listdir('test/data/images')]
        self.y = np.genfromtxt('test/data/image_labels.txt')

        self.indices = np.arange(len(self.X))

        self.on_epoch_end()
        
    def __len__(self):
        """Denotes the number of batches per epoch
        :return: number of batches per epoch
        """
        return len(self.indices) // self.batch_size

    def __getitem__(self, index):
        """Generate one batch of data
        :param index: index of the batch
        :return: x_batch and y_batch
        """
        # Initialization
        batch_X = np.empty((self.batch_size, *self.x_shape))
        batch_y = np.empty((self.batch_size, *self.y_shape))

        # Generate indexes of the batch
        indexes = self.indices[index * self.batch_size : (index + 1) * self.batch_size]
        for i, data_index in enumerate(indexes):
            batch_X[i] = cv2.imread(self.X[data_index])
            batch_y[i] = self.y[data_index]

        return batch_X, batch_y

    def on_epoch_end(self):
        """Shuffle indexes after each epoch
        """
        np.random.shuffle(self.indices)

generator = DataGenerator()
print(generator.X)