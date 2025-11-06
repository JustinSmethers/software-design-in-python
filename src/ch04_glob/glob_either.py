from collections.abc import Iterable
from .glob_null import Match

# class Either:
#     def __init__(self, left, right, rest=None):
#         self.left = left
#         self.right = right
#         self.rest = rest
#
#     def match(self, text, start=0):
#         return self.left.match(text, start) or \
#             self.right.match(text, start)


class Either(Match):
    def __init__(self, *alternatives, rest=None):
        super().__init__(rest)
        if len(alternatives) == 1 and isinstance(alternatives[0], Iterable):
            self.options = list(alternatives[0])
        else:
            self.options = list(alternatives)

    def _match(self, text, start):
        for pat in self.options:
            if pat is None:
                continue
            end = pat._match(text, start)
            if end is not None:
                end = self.rest._match(text, end)
                if end == len(text):
                    return end
        return None
