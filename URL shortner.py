import hashlib

def shorten_url(long_url):
    # Generate a MD5 hash of the long URL
    hash_object = hashlib.md5(long_url.encode())
    hash_hex = hash_object.hexdigest()

    # Take the first 8 characters of the hash as the short code
    short_code = hash_hex[:8]

    # Construct the shortened URL
    short_url = f"http://short.url/{short_code}"

    return short_url

# Example usage
long_url = input("Enter the long URL: ")
short_url = shorten_url(long_url)
print("Shortened URL:", short_url)
