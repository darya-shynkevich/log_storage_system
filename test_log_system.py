import pytest
from collections import Counter

from log_system import LogSystem


@pytest.fixture
def log_system():
    return LogSystem()


def test_put_and_retrieve_year(log_system):
    log_system.put(1, "2017:01:01:23:59:59")
    log_system.put(2, "2016:01:01:00:00:00")
    result = log_system.retrieve("2016:01:01:00:00:00", "2017:12:31:23:59:59", "Year")
    assert set(result) == {1, 2}


def test_retrieve_month(log_system):
    log_system.put(1, "2017:05:01:12:00:00")
    log_system.put(2, "2017:06:01:12:00:00")
    result = log_system.retrieve("2017:05:01:00:00:00", "2017:05:31:23:59:59", "Month")
    assert result == [1]


def test_retrieve_day(log_system):
    log_system.put(1, "2017:01:01:00:00:00")
    log_system.put(2, "2017:01:02:00:00:00")
    result = log_system.retrieve("2017:01:02:00:00:00", "2017:01:02:23:59:59", "Day")
    assert result == [2]


def test_retrieve_hour(log_system):
    log_system.put(1, "2017:01:01:01:23:45")
    log_system.put(2, "2017:01:01:02:00:00")
    result = log_system.retrieve("2017:01:01:01:00:00", "2017:01:01:01:59:59", "Hour")
    assert result == [1]


def test_retrieve_minute(log_system):
    log_system.put(1, "2017:01:01:01:23:45")
    log_system.put(2, "2017:01:01:01:24:00")
    result = log_system.retrieve("2017:01:01:01:23:00", "2017:01:01:01:23:59", "Minute")
    assert result == [1]


def test_retrieve_second(log_system):
    log_system.put(1, "2017:01:01:01:23:45")
    log_system.put(2, "2017:01:01:01:23:46")
    result = log_system.retrieve("2017:01:01:01:23:45", "2017:01:01:01:23:45", "Second")
    assert result == [1]


def test_no_results(log_system):
    log_system.put(1, "2017:01:01:00:00:00")
    result = log_system.retrieve("2018:01:01:00:00:00", "2018:12:31:23:59:59", "Year")
    assert result == []


def test_multiple_ids_same_timestamp(log_system):
    log_system.put(1, "2017:01:01:12:00:00")
    log_system.put(2, "2017:01:01:12:00:00")
    result = log_system.retrieve("2017:01:01:00:00:00", "2017:01:01:23:59:59", "Day")
    assert set(result) == {1, 2}


def test_duplicate_id_different_timestamps(log_system):
    # Putting the same id at two different timestamps
    log_system.put(1, "2017:01:01:00:00:00")
    log_system.put(1, "2017:01:02:00:00:00")
    result = log_system.retrieve("2017:01:01:00:00:00", "2017:01:02:23:59:59", "Day")
    # Expect two entries of id 1
    assert Counter(result).get(1) == 2
