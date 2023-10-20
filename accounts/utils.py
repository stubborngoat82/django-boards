import hashlib
from monsterid import Generator

def generate_monsterid_avatar(email):
    email_hash = hashlib.md5(email.encode('utf-8')).hexdigest()
    generator = Generator(email_hash)
    monsterid_url = generator.generate_url(size=80)  # You can adjust the size as needed
    return monsterid_url
