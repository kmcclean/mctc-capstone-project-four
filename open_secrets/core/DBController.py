from open_secrets.core.DBManager import DBManager


class DBController:

    def __init__(self):
        manager = DBManager()
        self.manager = manager

        self.manager.drop_database()
        self.manager.startup_database()
        self.manager.add_candidate_data()

    #searches the database and returns the results.
    def db_search(self, search_term):
        db_results = self.manager.candidate_search(search_term)
        return db_results

    #closes the database
    def db_close(self):
        self.manager.close_database()