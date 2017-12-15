import random

def gen_batch_data(data, batch_size, shuffle=False):
    """
    Args:
        data: list of data
        batch_size: size of one batch
        shuffle: whether shuffle data or not
    Return:
        iterator of batch data
    """
    cnt = 0
    data_size = len(data)
    assert data_size >= batch_size
    if shuffle:
        random.shuffle(data)

    while cnt < data_size:
        if cnt + batch_size <= data_size:
            yield data[cnt: cnt + batch_size]
        else:
            yield data[cnt: data_size] + data[: batch_size - data_size + cnt]
        cnt += batch_size
