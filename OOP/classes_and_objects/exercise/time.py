class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        if hours <= Time.max_hours and minutes <= Time.max_minutes and seconds <= Time.max_seconds:
            hour = ''
            minute = ''
            second = ''
            if hours < 10:
                hour = hour + ('0' + str(hours))
            else:
                hour = hour + str(hours)
            if minutes < 10:
                minute = minute + ('0' + str(minutes))
            else:
                minute = minute + str(minutes)
            if seconds < 10:
                second = second + ('0' + str(seconds))
            else:
                second = second + str(seconds)

            self.hours = int(hour)
            self.minutes = int(minute)
            self.seconds = int(second)

            return f'{hour}:{minute}:{second}'

    def get_time(self):
        hour = ''
        minute = ''
        second = ''
        if self.hours < 10:
            hour = hour + ('0' + str(self.hours))
        else:
            hour = hour + str(self.hours)
        if self.minutes < 10:
            minute = minute + ('0' + str(self.minutes))
        else:
            minute = minute + str(self.minutes)
        if self.seconds < 10:
            second = second + ('0' + str(self.seconds))
        else:
            second = second + str(self.seconds)

        return f'{hour}:{minute}:{second}'

    def next_second(self):
        new_seconds = self.seconds + 1
        new_minutes = self.minutes
        new_hours = self.hours
        if new_seconds > Time.max_seconds:
            new_seconds = 0
            new_minutes += 1
            if new_minutes > Time.max_minutes:
                new_minutes = 0
                new_hours += 1
                if new_hours > Time.max_hours:
                    new_hours = 0
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds
        return self.get_time()


time = Time(9, 30, 59)

print(time.set_time(7, 5, 6))
print(time.next_second())

