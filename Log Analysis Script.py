"""
Log Analysis Utility
Description: Processes system logs to track current users on various machines.
"""

def get_event_date(event):
    """Helper function to extract date for sorting."""
    return event.date

def current_users(events):
    """
    Analyses a list of events and returns a dictionary of machines
    and the users currently logged into them.
    """
    # Sort events by date to ensure we process them in chronological order
    events.sort(key=get_event_date)
    
    machines = {}
    for event in events:
        # Initialise the set for a machine if it hasn't been seen yet
        if event.machine not in machines:
            machines[event.machine] = set()
            
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            # Only attempt to remove if the user is actually recorded as logged in
            # This handles potential "logout" events with missing "login" data
            if event.user in machines[event.machine]:
                machines[event.machine].remove(event.user)
                
    return machines

def generate_report(machines):
    """Prints a formatted report of users currently active on each machine."""
    print("--- Current User Report ---")
    report_generated = False
    
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print(f"{machine}: {user_list}")
            report_generated = True
            
    if not report_generated:
        print("No users currently logged in.")

class Event:
    """Represents a single login or logout event."""
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

# Sample Data for Demonstration
if __name__ == "__main__":
    events = [
        Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
        Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
        Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
        Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
        Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
        Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
    ]

    # Process events and generate the report
    active_users = current_users(events)
    generate_report(active_users)