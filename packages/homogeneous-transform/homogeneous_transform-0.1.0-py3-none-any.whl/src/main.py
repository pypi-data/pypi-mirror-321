import numpy as np
from scipy.spatial.transform import Rotation as R

def rh(rotation_instance):
    """
    Converts a rotation instance from scipy into a 4x4 homogeneous rotation matrix.
    
    Parameters:
        rotation_instance (tuple or list or np.ndarray): A scipy rotation instance.
    
    Returns:
        np.ndarray: A 4x4 homogeneous rotation matrix.
    """
    
    # Validate the input
    if not isinstance(rotation_instance, R):
        raise TypeError("The rotation_instance must be a scipy.spatial.transform.Rotation object.")
    
    rh_matrix = np.eye(4) # 4x4 identity matrix

    rh_matrix[:3, :3] = rotation_instance.as_matrix() # Homogeneous rotation matrix

    return rh_matrix


def th(translation_vector = np.zeros(3)):
    """
    Converts a translation vector (x, y, z) into a 4x4 homogeneous translation matrix.
    
    Parameters:
        translation_vector (tuple or list or np.ndarray): A 3D translation vector (x, y, z).
    
    Returns:
        np.ndarray: A 4x4 homogeneous translation matrix.
    """

    # Validate the input
    if len(translation_vector) != 3:
        raise ValueError("The translation_vector must be a 3D vector.")
    
    th_matrix = np.eye(4) # 4x4 identity matrix

    th_matrix[:3, 3] = translation_vector # Homogeneous translation matrix

    return th_matrix


def sh(scale_vector):
    """
    Converts a scale vector (x, y, z) into a 4x4 homogeneous scaling matrix.
    
    Parameters:
        scale_vector (tuple or list or np.ndarray): A 3D scale vector (x, y, z).
    
    Returns:
        np.ndarray: A 4x4 homogeneous scaling matrix.
    """

    # Validate the input
    if len(scale_vector) != 3:
        raise ValueError("The scale vector must have exactly 3 components (x, y, z).")
    
    sh_matrix = np.eye(4) # 4x4 identity matrix
    sh_matrix[0, 0] = scale_vector[0]  # Scale along x
    sh_matrix[1, 1] = scale_vector[1]  # Scale along y
    sh_matrix[2, 2] = scale_vector[2]  # Scale along z

    return sh_matrix

    