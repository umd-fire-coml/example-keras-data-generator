from src.datagen import DataGenerator
import numpy as np



@pytest.fixture
def my_data_generator():
    return DataGenerator()

def test_batch_size():
    assert len(my_data_generator().__getitem__(1)[0]) == my_data_generator().batch_size

def test_x_shape():
    assert np.shape(my_data_generator().__getitem__(1)[0][0]) == my_data_generator().x_shape

def test_y_shape():
    assert np.shape(my_data_generator().__getitem__(1)[1][0]) == my_data_generator().y_shape

def test_num_dataset_items():
    assert 1==1