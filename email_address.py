import re
from operator import truediv


def validate_email_address(email):
    if "@" in email:
        return True
    else:
        return False


