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
            'today_minus_age_years': datetime(today.year - age, today.month, today.day).strftime('%e %B %Y').strip(),
            'midpoint': midpoint.strftime('%e %B %Y').strip(),
            'day': today.strftime('%A'),
            'event_date': self.strftime('%e %B %Y').strip()
        }

        return {**calculated_replacements, **self.replacements}

    def get_twice_replacements(self, today):
        twicepoint = self.get_twicepoint(today)
        age = calculate_age_rounding_up(twicepoint, today)

        calculated_replacements = {
            'twicepoint_year': twicepoint.year,
            'age': age,
            'half_age': age/2,
            'today_minus_age_years': datetime(today.year - age, today.month, today.day).strftime('%e %B %Y').strip(),
            'twicepoint': twicepoint.strftime('%e %B %Y').strip(),
            'day': today.strftime('%A'),
            'event_date': self.strftime('%e %B %Y').strip(),
            'years_and_months': self.get_years_and_months(today)
        }

        return {**calculated_replacements, **self.replacements}

    def get_years_and_months(self, today):
        months = 1 + today.month - self.month - (today.day <= self.day)
        month_string = f' and {months % 12} months' if months > 0 else ''
        return f'{today.year - self.year - (months <= 0)} years{month_string}'

def calculate_age_rounding_up(born, today):
    return (1 + today.year - born.year - ((today.month, today.day) <= (born.month, born.day)))
