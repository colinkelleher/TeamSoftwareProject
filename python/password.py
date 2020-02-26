import hashlib
"""
TeamSoftwareProject (CK, JH, PO'D, CO'D, LdlC, KP)

This python file allows us to to generate a password which is sha256 encoded

Within this file we have
- Constructor for class: __init__
- method to generate password: _generate
- method to return string of hashed password: __str__
- method to compare to other passwords: __eq__
"""

class Password(object):
    """
    Class to represent a hashed password
    """

    def __init__(self,password):
        """
        Constructor for the class
        :param password: String representing password to be hashed
        """
        self._password = self._generate(str(password))

    @staticmethod
    def _generate(password):
        password = hashlib.sha256(password.encode()).hexdigest()
        return password

    def __str__(self):
        """
        :return: String of the hashed password
        """
        return str(self._password)

    def __eq__(self, clear_text):
        """
        :param other: password to compare
        :return: True if password matches the clear text
                 False if the do not match
        """
        return self._password == Password(clear_text)._password


