import random
from string import Formatter
from datetime import datetime

class MessageBuilder():
    def __init__(self, messages, event, today):
        self.event = event
        self.messages_half, self.messages_twice = messages
        self.today = today

    def build_message(self):
        if (self.today.year - self.event.year) > 20:
            replacements = self.event.get_half_replacements(self.today)
            possible_messages = [x for x in self.messages_half if replacements_are_valid(x, replacements)]
            chosen_message = random.choice(possible_messages)

        else:
            replacements = self.event.get_twice_replacements(self.today)
            possible_messages = [x for x in self.messages_twice if replacements_are_valid(x, replacements)]
            chosen_message = random.choice(possible_messages)

        return MessageBuilderFormatter().format(chosen_message, **replacements)

def replacements_are_valid(message, replacements):
    return all(replacement in replacements for replacement in message.replacements)

class MessageBuilderFormatter(Formatter):
    def format_field(self, value, spec):
        if spec == 'capitalise':
            value = capitalise(value)
            spec = ''
        try:
            return super(MessageBuilderFormatter, self).format_field(value, spec)
        except ValueError as e:
            print('Invalid spec in formatter:', spec)
            raise

def capitalise(string):
    return f'{string[0].upper()}{string[1:]}'