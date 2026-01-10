#suit level testing is importan when we want to try and rerun the all the transient functions.
# to run this file,pytest file_name --reruns 3 --reruns-delay 2
import random
import pytest


def test_data_fetch_flaky():

    if random.random() < 0.33:
        assert False, "Transient failure 1"
    assert True


def test_another_service_flaky():
    if random.random() < 0.5:
        assert False, "Transient failure 2"
    assert True