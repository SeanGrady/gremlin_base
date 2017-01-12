def establish_database_connection(obj):
    """Setup database connection and sqlalchemy interface."""
    db_name = 'mission_data'
    db_url = 'mysql+mysqldb://root:password@localhost/' + db_name
    obj.engine = create_engine(db_url)
    obj.Session = sessionmaker(bind=self.engine)
