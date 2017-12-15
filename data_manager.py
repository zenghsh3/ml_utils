import random

def gen_batch_data(data, batch_size, shuffle=False):
    cnt = 0
    data_size = len(data)
    if shuffle:
        random.shuffle(data)

    while cnt < data_size:
        if cnt + batch_size <= data_size:
            yield data[cnt: cnt + batch_size]
        else:
            yield data[cnt: data_size] + data[: batch_size - data_size + cnt]
        cnt += batch_size
