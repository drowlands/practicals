
from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)

new_list = []
new_list.append(ruby)
new_list.append(python)
new_list.append(visual_basic)

# Not sure if you wanted the objects by themselves or formatted, so I did both :)

# new_list.append(str(ruby))
# new_list.append(str(python))
# new_list.append(str(visual_basic))

print("The dynamically typed languages are:")
for language in new_list:
    if language.is_dynamic():
        print(language.name)

print(new_list)