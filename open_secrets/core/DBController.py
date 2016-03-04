from open_secrets.core.DBManager import DBManager
manager = DBManager()
manager.drop_database()
manager.startup_database()
manager.add_candidate_data()
manager.print_out_data()
manager.close_database()