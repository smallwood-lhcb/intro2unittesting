import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean, daily_max, daily_min


def test_everything_works():
    npt.assert_array_equal(np.array([0, 0]), np.array([0, 0]))


def test_daily_mean_zeros():
   """Test that mean function works for an array of zeros."""
   from inflammation.models import daily_mean

   test_array = np.array([[0, 0],
                          [0, 0],
                          [0, 0]])

   # Need to use Numpy testing functions to compare arrays
   npt.assert_array_equal(np.array([0, 0]), daily_mean(test_array))


def test_daily_mean_integers():
   """Test that mean function works for an array of integers."""
   from inflammation.models import daily_mean

   test_array = np.array([[1, 2],
                          [3, 4],
                          [5, 6]])

   # Need to use Numpy testing functions to compare arrays
   npt.assert_array_equal(np.array([3, 4]), daily_mean(test_array))

import pytest
@pytest.mark.parametrize(
   "test, expected_mean",
   [
       ([[0, 0], [0, 0], [0, 0]], [0, 0]),
       ([[1, 2], [3, 4], [5, 6]], [3, 4]),
   ])

def test_daily_mean(test, expected_mean):
   """Test mean function works for array of zeroes and positive integers."""
   from inflammation.models import daily_mean
   npt.assert_array_equal(np.array(expected_mean), daily_mean(np.array(test)))

@pytest.mark.parametrize(
   "test, expected_min",
   [
       ([[0, 0], [0, 0], [0, 0]], [0, 0]),
       ([[1, 2], [3, 4], [5, 6]], [1, 2]),
   ])

def test_daily_min(test, expected_min):
   """Test mean function works for array of zeroes and positive integers."""
   from inflammation.models import daily_min
   npt.assert_array_equal(np.array(expected_min), daily_min(np.array(test)))

@pytest.mark.parametrize(
   "test, expected_max",
   [
       ([[0, 0], [0, 0], [0, 0]], [0, 0]),
       ([[1, 2], [3, 4], [5, 6]], [5, 6]),
   ])


def test_daily_max(test, expected_max):
   """Test mean function works for array of zeroes and positive integers."""
   from inflammation.models import daily_max
   npt.assert_array_equal(np.array(expected_max), daily_max(np.array(test)))


def test_daily_max_integers():
   """Test that max function works for an array of integers."""
   from inflammation.models import daily_mean

   test_array = np.array([[1, 2],
                          [3, 4],
                          [5, 6]])

   # Need to use Numpy testing functions to compare arrays
   npt.assert_array_equal(np.array([5, 6]), daily_max(test_array))

def test_daily_min_integers():
   """Test that min function works for an array of integers."""
   from inflammation.models import daily_mean

   test_array = np.array([[1, 2],
                          [3, 4],
                          [5, 6]])

   # Need to use Numpy testing functions to compare arrays
   npt.assert_array_equal(np.array([1, 2]), daily_min(test_array))

def test_daily_min_string():
   """Test for TypeError when passing strings. 
   
   checks this function gives a specific error when the wrong type is used  
   
   """
   from inflammation.models import daily_min
   from pytest import raises

   with raises(TypeError):
       daily_min([['Cannot', 'min'], ['string', 'arguments']]) #python would return a TypeError from this . Test passes
       #daily_min([[0, 0], [0, 0]]) # Test fails as all of correct type
       #daily_min([[a,c], [a, c]])

def test_daily_min_undefined_vals():
   """Test for TypeError when passing strings"""
   from inflammation.models import daily_min
   from pytest import raises

   with raises(NameError):
       #daily_min([['Cannot', 'min'], ['string', 'arguments']]) #python would return a TypeError from this . Test passes
       #daily_min([[0, 0], [0, 0]]) # Test fails as all of correct type
       daily_min([[a,c], [a, c]])

def test_val():
    """ Test of ValueError when passing value 
    
    Test passes when value is wrong - i.e. checks that ValueError is raised.

    """
    from pytest import raises

    val = 15
    with raises(ValueError):
        if val > 10:
            raise ValueError("value must be <= 10")

def test_daily_min_dict():
   """Test for TypeError when passing strings"""
   from inflammation.models import daily_min
   from pytest import raises

   with raises(TypeError):
       daily_min([['Cannot', 'min'], ['string', 'arguments']]) #python would return a TypeError from this . Test passes
       #daily_min([[0, 0], [0, 0]]) # Test fails as all of correct type
       #daily_min({"a":3, "b":3}) #dict instead of array