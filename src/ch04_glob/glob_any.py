from .glob_null import Match

# class Any:
#     def __init__(self, rest=None):
#         self.rest = rest
#
#     def match(self, text, start=0):
#         if self.rest is None:
#             return True
#         for i in range(start, len(text)):
#             if self.rest.match(text, i):
#                 return True
#         return False


class Any(Match):
    def __init__(self, rest=None):
        super().__init__(rest)

    def _match(self, text, start):
        for i in range(start, len(text) + 1):
            end = self.rest._match(text, i)
            if end == len(text):
                return end
        return None
