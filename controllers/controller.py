import adapters.adapter as adapter
import logic.main as logic

def receive(request):
    request_dict = adapter.json_to_dict(request)
    if(request_dict['command'] == "check_availability"):
        return check_availability(request_dict)
    elif(request_dict['command'] == "get_alternative_time_slots"):
        return get_alternative_time_slots(request_dict)
    elif(request_dict['command'] == "get_appointment"):
        return get_appointments(request_dict)
    elif(request_dict['command'] == "remove_appointment"):
        return remove_appointments(request_dict)
    else:
        raise Exception('Invalid command')

def check_availability(time_slot):
    time_slot_dict = adapter.time_slot_dict_conversion(time_slot)
    result = logic.check_availability(time_slot_dict)
    if('alternative_time_slots' in result):
        result['alternative_time_slots'] = adapter.format_alternative_time_slots(result)
    return result

def get_alternative_time_slots(time_slot):
    time_slot_dict = adapter.time_slot_dict_conversion(time_slot)
    alternative_time_slots = logic.get_alternative_time_slots(time_slot_dict)
    formatted_result = { 'alternative_time_slots': adapter.format_alternative_time_slots(alternative_time_slots) }
    return formatted_result

def get_appointments(request_dict):
    result = logic.get_appointments(request_dict['phone'])
    result['appointments'] = adapter.format_appointments(result['appointments'])
    return result

def remove_appointments(request_dict):
    logic.remove_appointments(request_dict['phone'])
    return { 'status': '200' }