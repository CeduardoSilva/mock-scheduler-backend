from datetime import datetime
from datetime import timedelta
import logic.main as logic
import config.formats as formats
import pytest

time_slot = { 
    'datetime': datetime.strptime('2020-03-15 11:00:00', formats.time_slot_format), 
    'code': 'A0444' }

def test_get_alternative_time_slots():
    received_time_slots = logic.get_alternative_time_slots(time_slot)
    
    assert_earlier_time_slots(received_time_slots)
    assert_later_time_slots(received_time_slots)
    assert(len(received_time_slots['alternative_time_slots']['later']) > 0 and len(received_time_slots['alternative_time_slots']['earlier']) > 0)

def assert_earlier_time_slots(received_time_slots):
    for earlier_time_slot in received_time_slots['alternative_time_slots']['earlier']:
        assert(earlier_time_slot['datetime'] < time_slot['datetime'])

def assert_later_time_slots(received_time_slots):
    for later_time_slot in received_time_slots['alternative_time_slots']['later']:
        assert(later_time_slot['datetime'] > time_slot['datetime'])

def test_check_availability():
    time_slot = { 'datetime': datetime.strptime('2020-03-15 11:00:00', formats.time_slot_format), 'phone': "+5511958139991" }
    assert(logic.check_availability(time_slot)['available'] != None)

def test_get_appointments():
    phone = "+5511982052477"
    assert(len(logic.get_appointments(phone)['appointments'])==1)
    assert(len(logic.get_appointments(phone+"1")['appointments'])==0)

def test_remove_appointments():
    phone = "test_removal"
    logic.remove_appointments(phone)
    assert(len(logic.get_appointments(phone)['appointments'])==0)