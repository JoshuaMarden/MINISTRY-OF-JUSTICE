"""unit tests for thrid test"""
from test_3 import *

def test_basic_sum_time_1():
    """check `sum_current_time` adds correctly"""
    time_string = "01:02:03"
    expected_result = 6

    result = sum_current_time(time_string)

    assert result == expected_result

def test_basic_sum_time_2():
    """check `sum_current_time` adds correctly"""
    time_string = "11:22:33"
    expected_result = 66

    result = sum_current_time(time_string)

    assert result == expected_result

def test_basic_sum_time_3():
    """check `sum_current_time` adds correctly"""
    time_string = "00:00:00"
    expected_result = 0

    result = sum_current_time(time_string)

    assert result == expected_result

def test_basic_sum_time_4():
    """check `sum_current_time` adds correctly"""
    time_string = "23:59:59"
    expected_result = 141

    result = sum_current_time(time_string)

    assert result == expected_result

def test_time_in_correct_format_1():
    """check `sum_current_time` returns correctly formatted time"""

    result = get_system_time()
    expected_lenght = 8

    assert len(result) == expected_lenght

def test_time_in_correct_format_2():
    """check `sum_current_time` returns correctly formatted time"""

    result = get_system_time()
    expected_colons = 2

    assert result.count(":") == expected_colons

def test_time_in_correct_format_3():
    """check `sum_current_time` returns correctly formatted time"""

    result = get_system_time()
    fragments = result.split(":")

    all_integers = True
    try:
        [int(fragment) for fragment in fragments]
    except ValueError:
        all_integers = False

    assert all_integers is True

def test_time_in_correct_range():
    """check `sum_current_time` adds correctly"""
    max_for_quadrivigesimal_system = 24
    max_for_sexagesimal_system = 60

    result = get_system_time()

    fragments = result.split(":")
    fragments = [int(fragment) for fragment in fragments]

    assert 0 <= fragments[0] < max_for_quadrivigesimal_system
    assert 0 <= fragments[1] < max_for_sexagesimal_system
    assert 0 <= fragments[2] < max_for_sexagesimal_system
