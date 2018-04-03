"""This module contains example data for testing."""

from serlo.model import Email, PhoneNumber

def generate_emails():
    """Returns examples of emails."""
    return [Email(address="hello@example.org"),
            Email(address="some-string-with-ü"),
            Email(address="")]

def generate_email_specs():
    """Returns XML specifications of emails corresponding to the results of
    `emails()`."""
    return ["""<email-address>
                <address>hello@example.org</address>
                <id type="integer">161561239</id>
                <location>Home</location>
               </email-address>""",
            """<email-address>
                <address>some-string-with-ü</address>
                <id type="integer">34567</id>
                <location>Work</location>
               </email-address>""",
            """<email-address><address /></email-address>"""]

def generate_phone_numbers():
    """Returns example phone numbers."""
    return [PhoneNumber(number="0123456789"),
            PhoneNumber(number="+490"),
            PhoneNumber(number="")]

def generate_phone_number_specs():
    """Returns XML specifications of phone number corresponding to the objects
    returned by `generate_phone_numbers()`."""
    return ["""<phone-number>
                <id type="integer">23144</id>
                <location>Mobile</location>
                <number>0123456789</number>
               </phone-number>""",
            """<phone-number>
                <id type="integer">0</id>
                <location>Work</location>
                <number>+490</number>
               </phone-number>""",
            """<phone-number><number /></phone-number>"""]
