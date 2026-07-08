import db

print(db.__file__)

print(hasattr(db, "create_table"))
print(hasattr(db, "create_users_table"))
print(hasattr(db, "save_patient"))

print(dir(db))