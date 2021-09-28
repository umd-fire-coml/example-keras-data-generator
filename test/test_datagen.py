from src.datagen import DataGenerator
import numpy as np
import pytest



@pytest.fixture
def my_data_generator():
    return DataGenerator()

def test_batch_size():
    generator = my_data_generator()
    assert(len(generator.__getitem__(1)[0]) == generator.batch_size)

def test_x_shape():
    generator = my_data_generator()
    assert(np.shape(generator.__getitem__(1)[0][0]) == generator.x_shape)

def test_y_shape():
    generator = my_data_generator()
    assert(np.shape(generator.__getitem__(1)[1][0]) == generator.y_shape)