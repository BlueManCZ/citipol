from modules.core.types import Event


class AbstractObject:
    def __init__(self):
        self._event_parent: AbstractObject | None = None
        self._event_handlers = {}

    def emit(self, event: Event):
        event.register_object_to_path(self)

        event_name = event.get_name()

        print(f"{type(self).__name__} registered", event_name, event.get_all_data())

        if event_name in self._event_handlers:
            for handler in self._event_handlers[event_name]:
                handler(event)

        if event.should_propagate():
            if self._event_parent:
                self._event_parent.emit(event)

    def set_event_parent(self, event_parent):
        self._event_parent = event_parent

    def add_event_listener(self, event_name, handler):
        if event_name not in self._event_handlers:
            self._event_handlers[event_name] = []
        self._event_handlers[event_name].append(handler)
