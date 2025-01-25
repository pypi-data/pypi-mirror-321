import pytest

from seCronTab.cron_field import CronField
from seCronTab.crontab import CronTab


@pytest.fixture
def valid_cron_expression():
    # return "*/15 0 1,15 * 1-5 /usr/bin/find"
    return "23 0-11/2,12-23/3 * * * /usr/bin/find"

@pytest.fixture
def valid_cron_expression2():
    # return "*/15 0 1,15 * 1-5 /usr/bin/find"
    return "23 0-11/2,12-23/3/3 * * * /usr/bin/find"

@pytest.fixture
def valid_cron_expression3():
    # return "*/15 0 1,15 * 1-5 /usr/bin/find"
    return "23 0-11/2,12-24/3 * * * /usr/bin/find"

@pytest.fixture
def invalid_cron_expression():
    # return "*-/15 0 1,15 * 1-5 /usr/bin/find extra_field"
    return "*-/15 0-11/2,12-23/3/3 * * * /usr/bin/find"


def test_cron_field_parse_valid_star():
    field = CronField("*,*", "hour")
    field.parse()
    assert field.values == []

def test_cron_field_parse_range_bad():
    field = CronField("*, 1-5", "hour")
    field.parse()
    assert field.values == [1, 2, 3, 4, 5]

def test_cron_field_parse_range_invalid():
    try:
        field = CronField("*/50", "hour")
        field.parse()
    except ValueError as e:
        assert str(e) == "Invalid cron field value for hour: */50"

def test_cron_field_parse_range_invalid2():
    try:
        field = CronField("*/50/1", "hour")
        field.parse()
    except ValueError as e:
        assert str(e) == "Invalid cron field value for hour: */50/1"

def test_cron_field_parse_valid():
    field = CronField("*/15", "minute")
    field.parse()
    assert field.values == [0, 15, 30, 45]

def test_cron_field_parse_range():
    field = CronField("1-5", "hour")
    field.parse()
    assert field.values == [1, 2, 3, 4, 5]

def test_cron_field_parse_list():
    field = CronField("1,2,3", "day of month")
    field.parse()
    assert field.values == [1, 2, 3]

def test_cron_field_parse_step():
    field = CronField("*/2", "month")
    field.parse()
    assert field.values == [1, 3, 5, 7, 9, 11]

def test_cron_field_parse_invalid():
    field = CronField("*/15,1-8", "day of week")
    with pytest.raises(ValueError):
        field.parse()

def test_cron_expression_parse_valid(valid_cron_expression):
    expression = CronTab(valid_cron_expression)
    expression.parse()
    assert len(expression.fields) == 5

def test_cron_expression_parse_valid2(valid_cron_expression2):
    expression = CronTab(valid_cron_expression2)
    with pytest.raises(ValueError):
        expression.parse()

def test_cron_expression_parse_invalid(invalid_cron_expression):
    expression = CronTab(invalid_cron_expression)
    with pytest.raises(ValueError):
        expression.parse()

def test_cron_expression_parse_invalid2(invalid_cron_expression):
    expression = CronTab(invalid_cron_expression)
    with pytest.raises(ValueError):
        expression.parse()


def test_cron_expression_format_table(valid_cron_expression):
    expression = CronTab(valid_cron_expression)
    expression.parse()
    table = expression.format_as_json()
    _m = expression.cron_minute
    _h = expression.cron_hour
    _d = expression.cron_day_of_month
    _mo = expression.cron_month
    _dow = expression.cron_day_of_week
    _c = expression.cron_command

    expected_table = {'expression': '23 0-11/2,12-23/3 * * * /usr/bin/find', 'minute': '23', 'hour': '0 2 4 6 8 10 12 14 16 18 20 22 0 3 6 9 12 15 18 21', 'day of month': '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31', 'month': '1 2 3 4 5 6 7 8 9 10 11 12', 'day of week': '0 1 2 3 4 5 6', 'command': '/usr/bin/find'}
    assert table == expected_table