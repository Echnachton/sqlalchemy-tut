from sqlalchemy import create_engine, text
# from sqlalchemy.orm import Session
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

def main():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

    # Commit as you go - manual commits
    # with engine.connect() as conn:
    #     conn.execute(text("CREATE TABLE users (id int, name char)"))
    #     conn.execute(text("INSERT INTO users (id, name) VALUES (:x, :y)"), [{"x": 1, "y": "Ivo"}, {"x": 2, "y": "Emma"}])
    #     conn.commit()

    # [Preferred] Begin once - scoped auto commit/rollback
    # with engine.begin() as conn:
    #     conn.execute(text("CREATE TABLE users (id int, name char)"))
    #     conn.execute(text("INSERT INTO users (id, name) VALUES (:x, :y)"), [{"x": 1, "y": "Ivo"}])

    # Connection is the thin pipe to the database. You run SQL and get rows back. That’s what engine.connect() and engine.begin() give you.
    # Session sits on top of that. It still runs SQL (e.g. session.execute(stmt)), but it’s built for the ORM: loading/updating Python objects, tracking changes, and coordinating commits.
    # When to use which
    # Connection / engine.begin() — scripts, migrations, raw SQL, no ORM models.
    # Session — you have declarative models (class User(Base): ...), want session.add(user), relationships, and change tracking.
    # stmt = text("SELECT id, name FROM users WHERE id > :y ORDER BY id, name")
    # with Session(engine) as session:
    #     result = session.execute(stmt, {"y": 1})
    #     for id, name in result:
    #         print(f"id: {id} name: {name}")
    
    metadata_obj = MetaData()

    user_table = Table(
        "user_account",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("name", String(30)),
        Column("fullname", String)
    )

    address_table = Table(
        "address",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("user_id", ForeignKey("user_account.id"), nullable=False),
        Column("email_address", String, nullable=False)
    )

    metadata_obj.create_all(engine)

    # https://docs.sqlalchemy.org/en/20/tutorial/metadata.html

if __name__ == "__main__":
    main()
