# Python Switch Case Using Python Class
class SwitchLanguage:
    """ A sample of Language switch cases """
    def language(self, language):
        default = "Invalid Language!.."
        return getattr(self, "case_"+str(language).lower(), lambda : default, )()

    def case_python(self):
        return "Python language selected"

    def case_java(self):
        return "Java language selected"

    def case_cpp(self):
        return "C++ language selected"


# Create an object
switch = SwitchLanguage()
print(switch.language("Python"))
print(switch.language("java"))
print(switch.language("cpp"))


# OUTPUT
#Python language selected
#Java language selected
#C++ language selected
