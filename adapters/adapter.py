from datetime import datetime
import config.formats as formats
import json

def time_slot_dict_conversion(time_slot_dict):
    datetime_str = time_slot_dict['date'] + " " + time_slot_dict['time']
    return { 'datetime': str_to_datetime(datetime_str), 'phone': time_slot_dict['phone'] }

def format_alternative_time_slots(alternative_time_slots):  
    alternative_time_slots = { 'earlier': convert_all_datetime_to_time_slot(alternative_time_slots['alternative_time_slots']['earlier']), 
             'later': convert_all_datetime_to_time_slot(alternative_time_slots['alternative_time_slots']['later']) }
    return alternative_time_slots

def convert_all_datetime_to_time_slot(time_slots):
    result = []
    for time in time_slots:
        result.append(datetime_to_time_slot(time['datetime']))
    return result

def format_appointments(appointments):
    result = []
    for appointment in appointments:
        formatted = datetime_to_time_slot(appointment['datetime'])
        result.append({ 'date': formatted['date'], 'time': formatted['time'], 'phone': appointment['phone']})
    return result
    
def datetime_to_time_slot(date_time):
    date = date_time.strftime(formats.datetime_date)
    time = date_time.strftime(formats.datetime_time)
    return { 'date': date, 'time': time }

def str_to_datetime(datetime_str):
    return datetime.strptime(datetime_str, formats.time_slot_format)

def json_to_dict(jsonStr):
    return json.loads(jsonStr)

def dict_to_json(dict):
    return json.dumps(dict)