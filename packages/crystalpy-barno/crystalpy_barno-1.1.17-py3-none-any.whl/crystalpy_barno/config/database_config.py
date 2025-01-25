class DatabaseConfig:
    server_name = None
    database_name = None
    user_id = None
    password = None

    @classmethod
    def get_database_name(cls):
        """Returns the currently set database name."""
        return cls.database_name

    @classmethod
    def set_connection_details(cls, server, database, user, password):
        cls.server_name = server
        cls.database_name = database
        cls.user_id = user
        cls.password = password

    @classmethod
    def get_connection_details(cls):
        if not all([cls.server_name, cls.database_name, cls.user_id, cls.password]):
            raise ValueError("Database connection details are incomplete.")
        return cls.server_name, cls.database_name, cls.user_id, cls.password
