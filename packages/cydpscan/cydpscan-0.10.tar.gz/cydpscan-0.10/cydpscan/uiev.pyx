from libc.stdint cimport *
from libcpp.vector cimport vector
from libcpp.map cimport map as cpp_map
from libcpp.utility cimport pair

cdef extern from "hdbscanner.hpp" nogil :
    cpp_map[int, vector[pair[float, float]]] get_dbscan2d(vector[float] &, float, int)
    cpp_map[int, vector[vector[float]]] get_dbscan3d(vector[float] &, float, int)

cpdef calculate_dbscan_2d(object coords, float eps, int min_pts):
    cdef:
        vector[float] floatvec
        Py_ssize_t i,j
        Py_ssize_t len_of_coords=len(coords)

    if len_of_coords==0:
        return {}
    floatvec.reserve(len_of_coords*2)
    if not isinstance(coords[0], (float,int)):
        for i in range(len_of_coords):
            for j in range(len(coords[i])):
                floatvec.emplace_back(<float>(coords[i][j]))
    else:
        for i in range(len_of_coords):
            floatvec.emplace_back(<float>(coords[i]))
    return get_dbscan2d(floatvec,eps,min_pts)

cpdef calculate_dbscan_3d(object coords, float eps, int min_pts):
    cdef:
        vector[float] floatvec
        Py_ssize_t i,j
        Py_ssize_t len_of_coords=len(coords)

    if len_of_coords==0:
        return {}
    floatvec.reserve(len_of_coords*3)
    if not isinstance(coords[0], (float,int)):
        for i in range(len_of_coords):
            for j in range(len(coords[i])):
                floatvec.emplace_back(<float>(coords[i][j]))
    else:
        for i in range(len_of_coords):
            floatvec.emplace_back(<float>(coords[i]))
    return get_dbscan3d(floatvec,eps,min_pts)

