import numpy as np
from tensorflow.keras.utils import Sequence

# DELETE THIS WHEN USING YOUR OWN DATASET, DO NOT STORE THE ACTUAL DATASET IN MEMEORY HERE
X_DATASET = [np.random.rand(*x_shape) for i in range(n_dataset_items)] 
Y_DATASET = [np.random.rand(*y_shape) for i in range(n_dataset_items)]

class DataGenerator(Sequence):
    '''this is a random data generator, edit this data generator to read data from dataset folder and return a batch with __getitem__'''

    def __init__(self, batch_size=8, x_shape=(256, 256, 3), y_shape=(10,), n_dataset_items=100):
        self.batch_size = batch_size
        self.x_shape = x_shape
        self.y_shape = y_shape
        self.n_dataset_items = n_dataset_items
        self.indexes = np.arange(self.n_dataset_items)
        self.on_epoch_end()
        # do not store your dataset like this when



    def __len__(self):
        """Denotes the number of batches per epoch
        :return: number of batches per epoch
        """
        return int(np.floor(n_dataset_items / self.batch_size))

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




    def on_epoch_end(self):
        """Shuffle indexes after each epoch
        """
        np.random.shuffle(self.indexes)

