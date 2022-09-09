class AbstractObject:
    def __init__(self) -> None:
        self._callbacks = []

    def add_event(self):
        pass

    def get_events(self):
        return self._events

    def set_parent(self, parent: Events) -> None:
        self._parent = parent

    def get_parent(self) -> Events:
        return self._parent
