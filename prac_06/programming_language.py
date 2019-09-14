
class ProgrammingLanguage:
    def __init__(self, typing, reflection, year):
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if (str(self.typing).lower() == "dynamic"):
            return True
        else:
            return False