import unittest
import numpy as np
import scipy.spatial.transform.rotation as R
from src.main import *

class TestMain(unittest.TestCase):
    def test_translation1(self):
        array1 = th([1,2,3])
        array2 = np.array([[1,0,0,1],
                           [0,1,0,2],
                           [0,0,1,3],
                           [0,0,0,1]])
        np.testing.assert_array_equal(array1, array2)


if __name__ == "__main__":
    unittest.main()