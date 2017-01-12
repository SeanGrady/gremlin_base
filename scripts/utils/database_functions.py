from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def establish_database_connection():
    """Setup database connection and sqlalchemy interface."""
    db_name = 'mission_data'
    db_url = 'mysql+mysqldb://root:password@localhost/' + db_name
    engine = create_engine(db_url)
    Session = sessionmaker(bind=self.engine)
    return engine, Session
