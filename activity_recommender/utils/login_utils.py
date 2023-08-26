import bcrypt
# password hashing functions
# creating the hashed password
def hash_password(password):
    # adding decode to make sure this can be saved ot the JSON file
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


# verifying the hashed password
def verify_password(password, hashed):
    # converting the stored string hashed password back to bytes for verification
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))