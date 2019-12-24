from datetime import datetime

class Event(datetime):
    def __init__(self, date, replacements, times_tweeted, last_tweeted):
        self.date = date
        self.replacements = replacements
        self.times_tweeted = times_tweeted
        self.last_tweeted = last_tweeted

    def __new__(self, date, replacements, times_tweeted, last_tweeted):
        event_date = datetime.strptime(date, '%Y-%m-%d')
        return datetime.__new__(
            self,
            event_date.year,
            event_date.month,
            event_date.day)

    def get_midpoint(self, date):
        date_diff = date - self
        return self + (date_diff/2)

    def get_twicepoint(self, date):
        date_diff = date - self
        return self - date_diff

    def get_half_replacements(self, today):
        midpoint = self.get_midpoint(today)
        age = calculate_age_rounding_up(midpoint, today)

        calculated_replacements = {
            'midpoint_year': midpoint.year,
            'age': age,
            'double_age': age*2,
            'today_minus_age_years': datetime(today.year - age, today.month, today.day).strftime('%d %B %Y'),
            'midpoint': midpoint.strftime('%d %B %Y'),
            'day': today.strftime('%A')
        }

        return {**calculated_replacements, **self.replacements}

    def get_twice_replacements(self, today):
        twicepoint = self.get_twicepoint(today)
        age = calculate_age_rounding_up(twicepoint, today)

        calculated_replacements = {
            'twicepoint_year': twicepoint.year,
            'age': age,
            'half_age': age/2,
            'today_minus_age_years': datetime(today.year - age, today.month, today.day).strftime('%d %B %Y'),
            'twicepoint': twicepoint.strftime('%d %B %Y'),
            'day': today.strftime('%A')
        }

        return {**calculated_replacements, **self.replacements}

def calculate_age_rounding_up(born, today):
    return (1 + today.year - born.year - ((today.month, today.day) <= (born.month, born.day)))