class AbstractEntity:
    def __init__(self, char="."):
        self._char = char

    def __str__(self):
        return self._char
