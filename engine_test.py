from sqlalchemy.engine import create_engine
#engine = create_engine(mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>, echo=True)
engine = create_engine('mysql://username:password@localhost/Thumm')

connection = engine.connect()
connection.execute(
    """
    CREATE TABLE users (
        username VARCHAR PRIMARY KEY,
        password VARCHAR NOT NULL
    );
    """
)
connection.execute(
    """
    INSERT INTO users (username, password) VALUES (?, ?);
    """,
    "foo", "bar"
)
result = connection.execute("SELECT username FROM users")
for row in result:
    print "username:", row['username']
connection.close()
