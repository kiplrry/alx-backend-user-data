# 0x00. Personal Data Project

## 📚 Resources

To get the most out of this project, please read or watch the following materials:

- [What Is PII, non-PII, and Personal Data?](https://example.com/pii-info)
- [Logging Documentation](https://example.com/logging-docs)
- [bcrypt Package](https://example.com/bcrypt-package)
- [Logging to Files, Setting Levels, and Formatting](https://example.com/logging-files)

## 🧠 Learning Objectives

By the end of this project, you will be able to confidently explain and demonstrate the following concepts:

1. **Examples of Personally Identifiable Information (PII)**
   - Understand what constitutes PII and differentiate it from non-PII and general personal data.
   - Examples include names, Social Security numbers, biometric records, etc.

2. **Implementing a Log Filter to Obfuscate PII Fields**
   - Learn how to create a log filter that masks PII fields in log files to protect sensitive information.
   - Ensure compliance with privacy regulations by properly handling PII in logs.

3. **Encrypting Passwords and Validating Input Passwords**
   - Use the `bcrypt` package to securely encrypt passwords.
   - Validate user input passwords against encrypted passwords to ensure security.

4. **Authenticating to a Database Using Environment Variables**
   - Securely store and use environment variables for database authentication.
   - Prevent hardcoding sensitive information directly in the source code.

## 🚀 Getting Started

1. **Setup Environment**
   - Ensure you have Python installed.
   - Install necessary packages using pip:
     ```sh
     pip install bcrypt
     ```

2. **Understanding PII**
   - Read the provided resource on PII to familiarize yourself with what constitutes PII and the importance of protecting it.

3. **Logging with Obfuscation**
   - Implement a custom log filter to obfuscate PII in your logs. Refer to the logging documentation for guidance on setting up loggers, handlers, and formatters.

4. **Password Encryption**
   - Use the `bcrypt` package to hash passwords securely. Follow the tutorial to learn how to hash a password and check its validity.

5. **Database Authentication**
   - Learn to use environment variables to store database credentials securely. Use `os.getenv()` in your Python scripts to access these variables.

## 📝 Example Code Snippets

### Log Filter Example
```python
import logging

class PIIObfuscationFilter(logging.Filter):
    def filter(self, record):
        if hasattr(record, 'message'):
            record.message = self.obfuscate_pii(record.message)
        return True

    def obfuscate_pii(self, message):
        # Simple example: Replace all digits with '*'
        return ''.join('*' if char.isdigit() else char for char in message)

logger = logging.getLogger('my_logger')
logger.addFilter(PIIObfuscationFilter())
```

### Password Encryption Example
```python
import bcrypt

# Encrypting a password
password = b"super_secret_password"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Checking password
if bcrypt.checkpw(password, hashed):
    print("Password matches")
else:
    print("Password does not match")
```

### Using Environment Variables for Database Authentication
```python
import os
import psycopg2

DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)
