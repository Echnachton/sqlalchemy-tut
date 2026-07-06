from sqlalchemy import create_engine, text

def main():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
    
    # Commit as you go - manual commits
    # with engine.connect() as conn:
    #     conn.execute(text("CREATE TABLE users (id int, name char)"))
    #     conn.execute(text("INSERT INTO users (id, name) VALUES (:x, :y)"), [{"x": 1, "y": "Ivo"}])
    #     conn.commit()

    # [Preferred] Begin once - scoped auto commit/rollback
    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE users (id int, name char)"))
        conn.execute(text("INSERT INTO users (id, name) VALUES (:x, :y)"), [{"x": 1, "y": "Ivo"}])


if __name__ == "__main__":
    main()
