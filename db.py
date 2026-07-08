from sqlalchemy import create_engine, text

# Database
engine = create_engine("sqlite:///medical.db")


# -------------------------
# Patients Table
# -------------------------
def create_table():

    with engine.connect() as conn:

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            result TEXT,
            confidence REAL
        )
        """))

        conn.commit()


# -------------------------
# Users Table
# -------------------------
def create_users_table():

    with engine.connect() as conn:

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
        """))

        conn.commit()


# -------------------------
# Save Patient
# -------------------------
def save_patient(name, age, gender, result, confidence):

    sql = """
    INSERT INTO patients
    (name, age, gender, result, confidence)
    VALUES
    (:name, :age, :gender, :result, :confidence)
    """

    with engine.connect() as conn:
        conn.execute(
            text(sql),
            {
                "name": name,
                "age": age,
                "gender": gender,
                "result": result,
                "confidence": confidence,
            },
        )
        conn.commit()


# -------------------------
# Get Patients
# -------------------------
def get_patients():

    with engine.connect() as conn:

        result = conn.execute(
            text("""
            SELECT *
            FROM patients
            ORDER BY id DESC
            """)
        )

        return result.fetchall()