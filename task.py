from datetime import time


class Task:
    def __init__(self, name, day, start_hours, start_minutes, end_hours, end_minutes):
        self.name = name
        self.day = day
        self.start_hours = start_hours
        self.start_minutes = start_minutes
        self.end_hours = end_hours
        self.end_minutes = end_minutes
