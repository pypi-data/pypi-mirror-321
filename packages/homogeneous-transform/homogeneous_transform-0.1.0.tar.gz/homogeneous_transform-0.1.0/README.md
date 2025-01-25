# Homogeneous Transform

A simple Python library for creating homogeneous transformation matrices for 3D transformations, including rotation, translation, and scaling. This library is built using **NumPy** and **SciPy** for efficient numerical computations.

---

## **Features**
- Generate **homogeneous rotation matrices** from `scipy.spatial.transform.Rotation`instance.
- Create **homogeneous translation matrices** from 3D translation vectors.
- Construct **homogeneous scaling matrices** from 3D scale vectors.
- Easy-to-use functions for common transformation operations.

---

## **Installation**

Install the package:
```bash
pip install homogeneous-transform
```


---

## **Usage**

### **Importing the Library**
```python
import numpy as np
from homogeneous_transform import rh, th, sh
from scipy.spatial.transform import Rotation as R
```

### **Examples**

#### **1. Create a Homogeneous Rotation Matrix**
Convert a rotation instance (e.g., 45 degrees around the Z-axis) into a 4x4 homogeneous matrix:
```python
rotation = R.from_euler('z', 45, degrees=True)  # Rotation around Z-axis
rotation_matrix = rh(rotation)
print("Homogeneous Rotation Matrix:")
print(rotation_matrix)
```

**Output**:
```
Homogeneous Rotation Matrix:
[[ 0.70710678 -0.70710678  0.          0.        ]
 [ 0.70710678  0.70710678  0.          0.        ]
 [ 0.          0.          1.          0.        ]
 [ 0.          0.          0.          1.        ]]
```

#### **2. Create a Homogeneous Translation Matrix**
Convert a translation vector (e.g., \([1, 2, 3]\)) into a 4x4 homogeneous matrix:
```python
translation_vector = [1, 2, 3]
translation_matrix = th(translation_vector)
print("Homogeneous Translation Matrix:")
print(translation_matrix)
```

**Output**:
```
Homogeneous Translation Matrix:
[[1. 0. 0. 1.]
 [0. 1. 0. 2.]
 [0. 0. 1. 3.]
 [0. 0. 0. 1.]]
```

#### **3. Create a Homogeneous Scaling Matrix**
Convert a scale vector (e.g., \([2, 3, 4]\)) into a 4x4 homogeneous matrix:
```python
scale_vector = [2, 3, 4]
scaling_matrix = sh(scale_vector)
print("Homogeneous Scaling Matrix:")
print(scaling_matrix)
```

**Output**:
```
Homogeneous Scaling Matrix:
[[2. 0. 0. 0.]
 [0. 3. 0. 0.]
 [0. 0. 4. 0.]
 [0. 0. 0. 1.]]
```

---

## **API Reference**

### `rh(rotation_instance)`
- **Description**: Converts a `scipy.spatial.transform.Rotation` instance into a 4x4 homogeneous rotation matrix.
- **Parameters**:
  - `rotation_instance`: A `scipy.spatial.transform.Rotation` object.
- **Returns**: A `numpy.ndarray` representing the 4x4 rotation matrix.

### `th(translation_vector)`
- **Description**: Converts a 3D translation vector into a 4x4 homogeneous translation matrix.
- **Parameters**:
  - `translation_vector`: A 3-element list, tuple, or NumPy array representing x, y, z.
- **Returns**: A `numpy.ndarray` representing the 4x4 translation matrix.

### `sh(scale_vector)`
- **Description**: Converts a 3D scale vector into a 4x4 homogeneous scaling matrix.
- **Parameters**:
  - `scale_vector`: A 3-element list, tuple, or NumPy array representing sx, sy, sz.
- **Returns**: A `numpy.ndarray` representing the 4x4 scaling matrix.


---

## **License**
This project is licensed under the GNU GENERAL PUBLIC License. See the [LICENSE](LICENSE) file for details.

---

## **Contributing**

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a clear description of the changes.


