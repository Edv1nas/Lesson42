"""Task Nr.2 : Write a User class that has a password property.
 The password property should be a computed property that checks whether the password is strong enough.
 A password is considered strong if it has at least 8 characters, contains at least one uppercase letter, one lowercase letter, and one number."""


class User:
    def __init__(self) -> None:
        self._password = None

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) >= 8 and any(i.isdigit()for i in value) and any(i.islower() for i in value) and any(i.isupper() for i in value):
            self._password = value
        else:
            print("\n!!!!Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number.!!!!")


user = User()
while True:
    user.password = input(
        "\nPlease enter strong password [8 characters, use uppercase, lowercase letters and numbers]: ")
    if user.password:
        print("Thank you for extraordinary password.")
        break
