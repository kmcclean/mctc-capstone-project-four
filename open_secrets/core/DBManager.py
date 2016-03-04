import sqlite3

class DBManager:

    def __init__(self):
        db = sqlite3.connect("open_secrets_info")
        cur = db.cursor()

        self.db = db
        self.cur = cur

    # This removes the old tables from the database, used primarily for testing.
    def drop_database(self):
        self.cur.execute('drop table if exists candidates')

    # This creates the tables that use this information.
    def startup_database(self):
        self.cur.execute('create table if not exists candidates (candidate_id text, candidate_first_name text, candidate_last_name text)')

    # this adds the data key for each of the individual candidate/members of Congress.
    def add_candidate_data(self):

        data_tuple_list = []
        f = open('candidate_data.txt', 'r')
        for line in f:
            line = line.strip("\n")
            line_list = line.split(",")
            line_tuple = tuple(line_list)
            data_tuple_list.append(line_tuple)

        f.close()

        self.cur.executemany('insert into candidates values (?, ?, ?)', data_tuple_list)

    # prints out the data.
    def print_out_data(self):
        self.cur.execute('select * from candidates')

        for item in self.cur:
            print(item)

    # closes the database.
    def close_database(self):
        try:
            self.db.close()
            print("Database closed")
        except Exception:
            pass