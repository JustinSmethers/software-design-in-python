from .glob_null import Match

# class Lit:
#     def __init__(self, chars, rest=None):
#         self.chars = chars
#         self.rest = rest
#
#     def match(self, text, start=0):
#         end = start + len(self.chars)
#         if text[start:end] != self.chars:
#             return False
#         if self.rest:
#             return self.rest.match(text, end)
#         return end == len(text)


class Lit(Match):
    def __init__(self, chars, rest=None):
        super().__init__(rest)
        self.chars = chars

    def _match(self, text, start):
        end = start + len(self.chars)
        if text[start:end] != self.chars:
            return None
        return self.rest._match(text, end)
