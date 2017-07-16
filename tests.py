import json
import random
from datetime import datetime
from classes import event

def test_old_enough(age, d1):
    twoageyearsago = datetime(today.year - 2*age, today.month, today.day)
    return twoageyearsago <= d1

def test_age(age, d1):
    assert(test_old_enough(age, d1) and not test_old_enough(age-1, d1))

def event_from_json(json_event):
    date = datetime.strptime(json_event['date'], '%Y-%m-%d')

    return event.Event(
        date,
        json_event['noun_phrase'],
        json_event['past_historic'],
        json_event['replacements'] if 'replacements' in json_event else {},
    )

def reference_changes_propagate():
    with open('events.json', 'r') as eventsfile:
        eventsjson = json.load(eventsfile)
        events = [event_from_json(a) for a in eventsjson]

    event = random.choice(events)

    event.noun_phrase = 'Googly Bear'

    print([e.noun_phrase for e in events])