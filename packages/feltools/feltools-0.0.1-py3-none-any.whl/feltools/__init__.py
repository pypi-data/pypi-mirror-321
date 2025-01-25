import hashlib

def spec_hash(text: str) -> str:
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    sha256_digest = sha256.hexdigest()
    
    sha512 = hashlib.sha512()
    sha512.update(text.encode('utf-8'))
    sha512_digest = sha512.hexdigest()
    
    sha512_digest = sha512_digest[:len(sha256_digest)]
    return sha512_digest + sha256_digest