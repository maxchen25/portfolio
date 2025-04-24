from sqlalchemy import create_engine, text
from pathlib import Path

# 1. Configure your database
DB_PATH = "pokemondb.db"
SQL_SCRIPT = "pokemon.sql"


def reset_database():
    """Deletes and recreates all tables using SQLAlchemy"""
    engine = create_engine(f"sqlite:///{DB_PATH}")

    # Delete old database (if exists)
    Path(DB_PATH).unlink(missing_ok=True)

    # Execute your SQL script
    with engine.connect() as conn:
        # Read and execute your SQL file
        with open(SQL_SCRIPT, "r") as f:
            sql_commands = f.read()

            # SQLAlchemy requires executing commands separately
            for command in sql_commands.split(";"):
                stripped_command = command.strip()
                if stripped_command:  # Skip empty statements
                    conn.execute(text(stripped_command))

        conn.commit()  # Commit all changes
        print(f"Database reset using {SQL_SCRIPT}")

    # Verify
    with engine.connect() as conn:
        tables = conn.execute(
            text("SELECT name FROM sqlite_master WHERE type='table';")
        ).fetchall()
        print("Current tables:", [t[0] for t in tables])


if __name__ == "__main__":
    reset_database()
