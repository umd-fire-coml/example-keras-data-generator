from src.datagen import DataGenerator



@pytest.fixture
def my_data_generator():
    return DataGenerator()

def test_batch_size:
    assert len(my_data_generator().__getitem__()) == my_data_generator().batch_size

def test_x_shape:
    assert 1==1

def test_y_shape:
    assert 1==1

def test_num_dataset_items:
    assert 1==1