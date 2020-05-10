import pytest
import controllers.controller as controller

def test_confirm_availability():
    request_available = "{\"date\":\"2020-03-20\",\"time\":\"11:00:00\",\"phone\":\"+5511958139991\",\"command\": \"check_availability\"}"
    request_unavailable = "{\"date\":\"2020-04-03\",\"time\":\"13:00:00\",\"phone\":\"+5511982052477\",\"command\": \"check_availability\"}"
    assert(controller.receive(request_available)['available'] == True)
    assertRequestUnavailable(controller.receive(request_unavailable))

def assertRequestUnavailable(response):
    assert(response['available'] == False)
    assert(response['alternative_time_slots']['earlier'] != None)
    assert(response['alternative_time_slots']['later'] != None)

def test_alternative_time_slots():
    request = "{\"date\":\"2020-03-15\",\"time\":\"15:00:00\",\"phone\":\"+5511958139991\",\"command\": \"get_alternative_time_slots\"}"
    assert(controller.receive(request)['alternative_time_slots']['earlier'] != None)
    assert(controller.receive(request)['alternative_time_slots']['later'] != None)

def test_get_appointment():
    request = "{\"date\":\"2020-03-15\",\"time\":\"15:00:00\",\"phone\":\"+5511982052477\",\"command\": \"get_appointment\"}"
    request_empty = "{\"date\":\"2020-03-15\",\"time\":\"15:00:00\",\"phone\":\"+55\",\"command\": \"get_appointment\"}"
    assert(controller.receive(request)['appointments'][0]['phone']=="+5511982052477")
    assert(len(controller.receive(request_empty)['appointments'])==0)

def test_remove_appointment():
    request = "{\"date\":\"2020-03-15\",\"time\":\"15:00:00\",\"phone\":\"test_removal\",\"command\": \"remove_appointment\"}"
    request_empty = "{\"date\":\"2020-03-15\",\"time\":\"15:00:00\",\"phone\":\"test_removal\",\"command\": \"get_appointment\"}"
    controller.receive(request)
    assert(len(controller.receive(request_empty)['appointments'])==0)