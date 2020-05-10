from datetime import datetime
from datetime import timedelta
import config.formats as formats
import random

taken_time_slots = [
    { 
        'datetime': datetime.strptime('2020-12-03 10:00:00', formats.time_slot_format), 
        'phone': 'test_removal' 
    },
    { 
        'datetime': datetime.strptime('2020-04-03 13:00:00', formats.time_slot_format), 
        'phone': '+5511982052477' 
    }
]

def check_availability(time_slot):
    if(is_available(time_slot)):
        appointment_time_slot = create_appointment_time_slot(time_slot)
        schedule_appointment(appointment_time_slot)
        return { 'available': True, 'phone': time_slot['phone'] }
    return { 'available': False, 'alternative_time_slots': generate_alternative_time_slots(time_slot) }

def create_appointment_time_slot(time_slot):
    return { 
            'datetime': time_slot['datetime'], 
            'phone': time_slot['phone'] }

def schedule_appointment(time_slot):
    remove_appointments(time_slot['phone'])
    take_time_slot(time_slot)

def remove_appointments(phone):
    for taken_time_slot in taken_time_slots:
        if(taken_time_slot['phone'] == phone): 
            taken_time_slots.remove(taken_time_slot)

def take_time_slot(time_slot):
    taken_time_slots.append(time_slot)

def get_alternative_time_slots(time_slot):
    return { 'alternative_time_slots': generate_alternative_time_slots(time_slot) }

def generate_alternative_time_slots(time_slot):
    number_of_slots_in_each = 4
    alternative_time_slots = {  'earlier': get_available_earlier(time_slot, number_of_slots_in_each), 
        'later': get_available_later(time_slot, number_of_slots_in_each) }
    return alternative_time_slots

def get_available_earlier(time_slot, number_of_slots_in_each):
    earlier_time_slots = []

    for i in range(0,number_of_slots_in_each):
        earlier_time_slot = generate_earlier_time_slots(time_slot,number_of_slots_in_each-i)
        if(is_available(earlier_time_slot)): earlier_time_slots.append(earlier_time_slot)
    return earlier_time_slots

def get_available_later(time_slot, number_of_slots_in_each):
    later_time_slots = []

    for i in range(0,number_of_slots_in_each):
        later_time_slot = generate_later_time_slots(time_slot,i+1)
        if(is_available(later_time_slot)): later_time_slots.append(later_time_slot)
    return later_time_slots

def generate_earlier_time_slots(time_slot, hours_diff):
    return { 
        'datetime': time_slot['datetime'] - timedelta(hours=hours_diff) }

def generate_later_time_slots(time_slot, hours_diff):
    return { 
        'datetime': time_slot['datetime'] + timedelta(hours=hours_diff) }

def is_available(time_slot):
    for taken_time_slot in taken_time_slots:
        if(is_same_time_slot(time_slot, taken_time_slot)): return False
    return True

def is_same_time_slot(slot1, slot2):
    return slot1['datetime'] == slot2['datetime']

def get_appointments(phone):
    result = []
    for taken_time_slot in taken_time_slots:
        if(taken_time_slot['phone'] == phone): result.append(taken_time_slot)
    return { 'appointments': result }