import hashlib

def create_hash(text) -> str:
    text = str(text)
    text += "3886go@fcbE7QukKNxXNWNkxfndsZUxLh9sZjNg82VDWCN_2.se39g4JN*hmieJBg8kkovY_EeyKTi3DDJhaLmJA*pQsQxFP9CynwA3a"
    text_bytes = text.encode("utf-8")
    return hashlib.sha256(text_bytes).hexdigest()

def verify_hash(original, hash) -> bool:
    generated = create_hash(original)
    return generated == hash
