import hashlib


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


    def _generate(self,password):
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


if __name__ == "__main__":
    print(Password("123"))
    print(Password("123") == "123")

