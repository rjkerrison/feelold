from datetime import datetime
from event import Event
from messagetemplate import MessageTemplate
from messagebuilder import MessageBuilder
import random
import json

def event_from_json(json_event):
    return Event(
        json_event['date'],
        json_event['replacements'] if 'replacements' in json_event else {},
        json_event['times_tweeted'] if 'times_tweeted' in json_event else 0,
        json_event['last_tweeted'] if 'last_tweeted' in json_event else '1899-01-01 00:00:00',
    )

def weighted_choice(choices):
    # https://stackoverflow.com/a/3679747/4099675
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"

def get_events():
    with open('json/events.json', 'r') as eventsfile:
        eventsjson = json.load(eventsfile)
        events = [event_from_json(a) for a in eventsjson]

    return events

def get_messages():
    with open('json/messages.json', 'r') as messagesfile:
        messagesjson = json.load(messagesfile)
        messages_half = [MessageTemplate(m) for m in messagesjson["you_are_more_than_half_as_old_as"]]
        messages_twice = [MessageTemplate(m) for m in messagesjson["you_are_less_than_twice_as_old_as"]]

    return messages_half, messages_twice

def update_events_json(events):
    with open('json/events.json', 'w') as eventsfile:
        eventsjson = json.dump([ob.__dict__ for ob in events], eventsfile, indent=4)

def get_random_message():

    events = get_events()
    messages = get_messages()
    today = datetime.today()

    events = sorted(events, key=lambda x: datetime.strptime(x.last_tweeted, '%Y-%m-%d %H:%M:%S'))
    nonrecent_events = events[:5]

    event = weighted_choice([(event, 100 / (event.times_tweeted + 1)) for event in nonrecent_events])
    builder = MessageBuilder(messages, event, today)

    event.times_tweeted += 1
    event.last_tweeted = today.strftime('%Y-%m-%d %H:%M:%S')

    update_events_json(events)

    return builder.build_message()

def main():
    print(get_random_message())

if __name__ == "__main__":
    main()