"""Hello World Multi Language.

depending on the language of environment, the program show a message
correspondent.
Usage:
You need to have the variable set correctly ex:

    export LANG=pt_BR

execution:

     python hello.py
    (or)
    python3 hello.py

end
"""
__version__ = "0.0.1"
__author__ = "Guilherme Luís"
__license__ = "Unlicensed"

import locale


current_language, _ = locale.getlocale()

msg = "Hello, World" #Default

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "en_US":
    msg = "Hello, World!"

print(msg)
