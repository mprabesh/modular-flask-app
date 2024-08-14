### Semester End Project: AML 1204
**This project was created to fulfill the course requirements for Python Programming in Canada (AML 1204) at Lambton College, Toronto.**

**2024 Summer DOCT Group 2**

Project Details:
```
This demonstrates the simple URL shortner application.
A URL Shortener takes a long form of a URL, hashes it into 8 characters, and stores it in the database.
Flask a Python framework and SQlite for the purpose of storing the data.
```

### Step 1: Compute SHA-256 Hash
- **Process**:
  1. **Create a SHA-256 hash object** using `hashlib.sha256()`.
  2. **Update the hash object** with the bytes of the input string using `input_string.encode('utf-8')`.
  3. **Compute the SHA-256 digest** by calling `sha256_hash.digest()` which returns the hash as a bytes object.
  
### Step 2: Convert SHA-256 Hash to Integer
- **Process**:
  1. The SHA-256 digest (which is a 32-byte value) is converted to an integer using `int.from_bytes(sha256_result, byteorder='big')`. 
  2. This conversion interprets the bytes as a big-endian integer.
  3. The resulting large integer is reduced modulo \(2^{64}\) to fit into a 64-bit integer range: `int.from_bytes(sha256_result, byteorder='big') % (2**64)`.

### Step 3: Convert Integer to Bytes and Base58 Encode
- **Process**:
  1. The integer obtained in Step 2 is **converted to a string** using Python’s `str()` function.
  2. This string is then **encoded to bytes** using `.encode('utf-8')`.
  3. The bytes are then **Base58 encoded** using the `base58.b58encode()` function.
  4. The Base58 encoding is **decoded back to a string** using `.decode('utf-8')`.

### Step 4: Shorten the Encoded String
- **Process**:
  1. The resulting Base58 encoded string is **shortened** to the first 8 characters: `encoded[:8]`.
  2. This shortened string is returned as the final result.

### Purpose of Each Step:
1. **SHA-256 Hashing**: This ensures that the input string is converted into a unique and fixed-length 256-bit hash, which is a secure and collision-resistant representation.
2. **Integer Conversion**: Reducing the hash to a 64-bit integer makes it smaller and more manageable.
3. **Base58 Encoding**: This encodes the integer into a more compact, URL-safe string format, which avoids confusion with similar-looking characters (e.g., '0' and 'O').
4. **String Shortening**: The first 8 characters are taken to create a short, unique identifier that is likely to be unique enough for many practical purposes.

### UI developed on plain HTML

***Pyjwt is used for the purpose of authenticating API's.***

***An approach was taken to use the concept of [Blueprint](https://flask.palletsprojects.com/en/3.0.x/blueprints/) to make the flask app modular. Here, 3 module exists including `auth`,`urlshortner`,`urlredirection`***

***Create a `config.py` file to add `DATABASE` and `SECRET_KEY`***

***`init_db.py` file is present to initialize database entities. Run this script at first***

***API Endpoints***

POST http://127.0.0.1:5000/api/url/ --> generates the short URL </br>
GET http://127.0.0.1:5000/api/url/<username> --> gets all the URLs shorted by user <username> </br>
DELETE http://127.0.0.1:5000/api/url/<URL_ID> --> deletes the URL with id URL_ID </br>

GET http://127.0.0.1:5000/api/users/ --> Get all the user information from a database </br>
POST http://127.0.0.1:5000/api/users/ --> register user </br>
POST http://127.0.0.1:5000/api/auth/login --> login API </br>



