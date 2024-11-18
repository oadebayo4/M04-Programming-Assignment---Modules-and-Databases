# 11.1 Create a file called Zoo and define a function called hours. Then use the interactive interpreter to import the zoo module and call its hours function.

def hours():
    print("Open 9-5 Daily")

# 11.2 11.2 In the interactive interpreter, import the Zoo modules as menagerie and call its hours function.

import Zoo as menagerie
menagerie.hours()

# Using the interpreter, explicitly import and call the hours() function from zoo.
from Zoo import hours
hours()

# Import the hours() function as info and call it.

from Zoo import hours as info
info()


