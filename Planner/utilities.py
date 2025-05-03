import datetime

class ScheduleEvent():
    ###
    # username: username of user
    # id: id of event
    # start_time
    ###
    def __init__(self, username: str, event_id: int, start_time: datetime.datetime, end_time: datetime.datetime, location: str, description: str):
        self.username = username
        self.event_id = id
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.description = description

    def get_start_time(self):
        return self.start_time
    
    def get_end_time(self):
        return self.end_time
    
    def get_description(self):
        return self.description
    
    def get_dict(self):
        return {
            "username": self.username,
            "event_id": self.event_id,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "location": self.location,
            "description": self.description
        }