from libc.stdint cimport *
from libcpp.vector cimport vector
from libcpp.string cimport string
cimport cython
import cython
from typing import Literal


cdef extern from "newhdbscan.hpp" nogil :
    ctypedef struct resultstruct:
        vector[double] original_data
        int label
        double membership_probability
        double outlier_score
        int outlier_id
    vector[resultstruct] calculate_hdbscan(vector[vector[double]] & dataset, int min_points, int min_cluster_size, string distance_metric)

def py_calculate_hdbscan(object data,int min_points, int min_cluster_size, distance_metric:Literal["Euclidean","Manhattan"]="Euclidean"):
    """
    Perform HDBSCAN clustering on a dataset using the specified parameters.

    This function wraps a C++ implementation of HDBSCAN - https://github.com/rohanmohapatra/hdbscan-cpp, converting Python data
    types into the required C++ types before passing them to the underlying C++
    implementation. It returns clustering results as a list of resultstruct objects
    defined in C++.

    Parameters
    ----------
    data : list of list of float
        A two-dimensional list where each sublist represents a data point in the dataset.
    min_points : int
        The minimum number of points required in a neighborhood to consider a point as a core point.
    min_cluster_size : int
        The minimum number of points required to form a cluster.
    distance_metric : {'Euclidean', 'Manhattan'}, optional
        The metric used to compute the distance between points. Defaults to 'Euclidean'.

    Returns
    -------
    list of resultstruct
        A list where each element is a resultstruct containing the clustering result for each data point,
        including labels and outlier scores.

    Raises
    ------
    ValueError
        If the input dataset is empty or if any of the data points in the dataset are empty.

    Note
    ----
    This function interfaces with a C++ backend. Ensure that the required you have Cython and a C++ compiler installed!
    """
    cdef:
        Py_ssize_t len_data=len(data)
        Py_ssize_t sub_len_data
        Py_ssize_t i, j
        string cpp_distance_metric
        vector[vector[double]] dataset
        double subdata
    if not len_data:
        raise ValueError("Dataset is empty")
    sub_len_data=len(data[0])
    if not sub_len_data:
        raise ValueError("Data in dataset is empty")
    dataset.reserve(len_data)
    if isinstance(distance_metric,bytes):
        cpp_distance_metric=<string>((distance_metric))
    else:
        cpp_distance_metric=<string>((str(distance_metric)).encode())
    for i in range(len_data):
        dataset.emplace_back()
        for j in range(sub_len_data):
            subdata=<double>(data[i][j])
            dataset.back().emplace_back(subdata)
    return (calculate_hdbscan(dataset,min_points,min_cluster_size,cpp_distance_metric))


