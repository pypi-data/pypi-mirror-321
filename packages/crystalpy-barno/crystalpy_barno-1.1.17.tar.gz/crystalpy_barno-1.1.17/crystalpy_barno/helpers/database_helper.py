from crystalpy_barno.config.database_config import DatabaseConfig

class DatabaseHelper:
    @staticmethod
    def apply_connection(crpt):
        server, database, user, password = DatabaseConfig.get_connection_details()
        for table in crpt.Database.Tables:
            logon_info = table.LogOnInfo
            logon_info.ConnectionInfo.ServerName = server
            logon_info.ConnectionInfo.DatabaseName = database
            logon_info.ConnectionInfo.UserID = user
            logon_info.ConnectionInfo.Password = password
            table.ApplyLogOnInfo(logon_info)
