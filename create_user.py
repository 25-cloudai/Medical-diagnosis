from db import *

conn = engine.connect()

conn.execute(
    users.insert().values(
        email="admin@gmail.com",
        password="admin123"
    )
)

conn.commit()

print("User Created Successfully")