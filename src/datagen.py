import numpy as np
import cv2
from tensorflow.keras.utils import Sequence

class DataGenerator(Sequence):
    '''this is a random data generator, edit this data generator to read data from dataset folder and return a batch with __getitem__'''

    def __init__(self, batch_size=8, x_shape=(360, 480, 3), y_shape=(10,), n_dataset_items=233):
        self.batch_size = batch_size
        self.x_shape = x_shape
        self.y_shape = y_shape
        self.n_dataset_items = n_dataset_items
        self.indexes = np.arange(self.n_dataset_items)
        self.on_epoch_end()
        
        self.x_filepaths = os.listdir('.test/data/images')
        self.y_labels = np.genfromtxt('./test/data/image_labels.txt',dtype='int')

    def __len__(self):
        """Denotes the number of batches per epoch
        :return: number of batches per epoch
        """
        return int(np.floor(self.n_dataset_items / self.batch_size))

    def __getitem__(self, index):
        """Generate one batch of data
        :param index: index of the batch
        :return: x_batch and y_batch
        """
        # Initialization
        x_batch = np.empty((self.batch_size, *self.x_shape))
        y_batch = np.empty((self.batch_size, *self.y_shape))

        # Generate indexes of the batch
        indexes = self.indexes[index * self.batch_size : (index + 1) * self.batch_size]

        # Generate data
        for i in range(self.batch_size):
            x_batch[i,] = self.x_filepaths[indexes[i]]
            y_batch[i,] = self.y_labels[indexes[i]]

        # Return batch data
        return x_batch, y_batch



    def on_epoch_end(self):
        """Shuffle indexes after each epoch
        """
        np.random.shuffle(self.indexes)

