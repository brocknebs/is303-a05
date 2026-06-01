'''
Brock
IS 303 - A05

Event Planner
This program models a calendar that find events by date, checks for conflicts, finds the next upcoming event, and displays the calendar.

Inputs:
- Event name and event date

Processes:
- Event class: stores event name and date; display info
- Bookshelf class: stores events in a list; adds events; sorts events by date; checks for conflicts; finds the next event; displays all events

Outputs:
- Each events's info, conflictss (if any), and the next upcoming event
'''

class Event:
    def __init__(self, event_name, date):
        self.name = event_name
        self.date = date
        self.month = self.fix_date("m")
        self.day = self.fix_date("d")
        self.year = self.fix_date("y")

    def fix_date(self, date_type):
        dates = self.date.split("/")
        if date_type == "m":
            return int(dates[0])
        elif date_type == "d":
            return int(dates[1])
        elif date_type == "y":
            return int(dates[2])

    def __str__(self):
        return f"{self.name} ({self.date})"


class Calendar:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def find_conflicts(self):
        conflicts =[]
        conflict_names = []
        for event in self.events:
            event_name = event.name
            event_date = event.date
            for e in self.events:
                if e.name != event_name and e.name not in conflict_names:
                    if event_date == e.date:
                        conflicts.append([event, e])
                        conflict_names.append(event_name)
                        conflict_names.append(e.name)
        return conflicts
    
    def next_appointment(self):
        events = sorted(self.events, key=lambda e: (e.year, e.month, e.day))
        return events[0]
    
    def __str__(self):
        header = f"Calendar: {self.name} ({len(self.events)} events)"
        event_list = ""
        for event in self.events:
            event_list = event_list + f"\n - {event}"
        return header + event_list

# --- Main Flow ---
calendar = Calendar("My Calendar")

calendar.add_event(Event("Dentist", "10/21/25"))
calendar.add_event(Event("Dinner", "7/21/25"))
calendar.add_event(Event("Visit family", "9/8/25"))
calendar.add_event(Event("Go fishing", "9/8/25"))

print(calendar)
print()

conflicts = calendar.find_conflicts()
if len(conflicts) > 0:
    print("Conflicts:")
    for event in conflicts:
        for e in event:
            print(f" - {e}")
else:
    print("No conflicts.")
print()

next_appointment = calendar.next_appointment()
print(f"Next appointment: {next_appointment}")