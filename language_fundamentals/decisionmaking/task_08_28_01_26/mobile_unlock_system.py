db_unlock_pattern = 346890
db_fingerprint = "gdjkjll"

pattern = int(input("Enter unlock pattern:"))

if db_unlock_pattern == pattern:
    fingerprint = input("Enter fingerprint:")
    if fingerprint == db_fingerprint:
        print("Mobile unlocked")
    else:
        print("Fingerprint mismatch")
else:
    print("Wromg pattern")