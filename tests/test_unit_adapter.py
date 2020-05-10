from datetime import datetime
import pytest
import adapters.adapter as adapter
import config.formats as formats


def test_time_slot_dict_conversion():
    time_slot = {'date': "2020-03-15",
                 'time': "12:00:00", 'phone': "+5511958139991"}
    result_type = "<type 'datetime.datetime'>"
    assert(str(type(adapter.time_slot_dict_conversion(
        time_slot)['datetime'])) == result_type)


def test_convert_json_to_dict():
    json_example = "{\"data\": \"some-data\" }"
    dict_example = {'data': 'some-data'}
    assert(adapter.json_to_dict(json_example) == dict_example)


def test_convert_string_to_datetime():
    time = "2020-03-15 11:00:00"
    result_type = "<type 'datetime.datetime'>"
    assert(str(type(adapter.str_to_datetime(time))) == result_type)


def test_format_alternate_time_slots():
    alternative_time_slots = {
        'alternative_time_slots': {
            'earlier': [
                {
                    'datetime': datetime.strptime("2020-03-20 09:00:00", formats.time_slot_format)
                }
            ],
            'later': [
                {
                    'datetime': datetime.strptime("2020-03-20 14:00:00", formats.time_slot_format)
                }
            ]
        }
    }

    expected_result = {
        'earlier': [
            {
                'date': "20/03/2020",
                'time': "09:00:00"
            }
        ],
        'later': [
            {
                'date': "20/03/2020",
                'time': "14:00:00"
            }
        ]
    }

    assert(adapter.format_alternative_time_slots(
        alternative_time_slots) == expected_result)


def test_datetime_formatter():
    date_time = datetime.strptime(
        "2020-03-15 11:00:00", formats.time_slot_format)
    expected_format = {'date': "15/03/2020", 'time': "11:00:00"}
    assert(adapter.datetime_to_time_slot(date_time) == expected_format)


def test_format_appointments():
    input = [
        {
            "datetime": datetime.strptime("2020-03-20 11:00:00", formats.time_slot_format),
            "phone": "+5511982052477"
        }
    ]
    expected_output = [
        {
            'date': "20/03/2020",
            'time': "11:00:00",
            'phone': "+5511982052477"
        }
    ]
    assert(adapter.format_appointments(input) == expected_output)
