"""
An implementation of the observer pattern
"""


class EventHandler:
    """A singleton class that allows the subscription to events."""
    _instance = None

    def __new__(cls):
        """Ensures only one instance of EventHandler can exist."""
        if cls._instance is None:
            print("Creating event handler")
            cls._instance = super(EventHandler, cls).__new__(cls)
            cls._events = {}
        return cls._instance

    def subscribe(self, event_name, callback):
        """Add a function callback to the event list."""
        if event_name not in self._events:
            self._events[event_name] = [callback]
        else:
            self._events[event_name].append(callback)

    def unsubscribe(self, event_name, callback):
        """Remove a function callback to the event list."""
        if event_name in self._events:
            self._events[event_name].remove(callback)

    def fire(self, event_name):
        """Fire off an event and call all functions subscribed."""
        if event_name in self._events:
            events = self._events.get(event_name)
            if events:  # only call if list isn't empty
                for event in events:
                    event()
            else:
                print(f"Event: {event_name} has no active listeners")
        else:
            print(f"Event: {event_name} has not been registered")
