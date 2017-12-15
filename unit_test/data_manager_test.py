import sys
sys.path.append('..')

from data_manager import gen_batch_data

def unzip(iterator):
    return list(zip(*iterator))

if __name__ == '__main__':
    a = [[1,2],[3,4],[5,6], [7,8], [9,10]]
    b = ['a', 'b', 'c', 'd', 'e']
    for batch_data in gen_batch_data(list(zip(a, b)), 3):
        batch_data = unzip(batch_data)
        batch_a = batch_data[0]
        batch_b = batch_data[1]
        print(batch_a, batch_b)
