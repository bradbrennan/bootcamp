import numpy as np

#use as x1, y1 = ecdf_test.ecdf(name of file data)
def ecdf(data):

    #sort and arrange data
    x = np.sort(data)
    y = np.arange(1,len(data) + 1) / len(data)

    return x, y
