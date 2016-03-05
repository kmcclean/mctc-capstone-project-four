import sqlite3

class DBManager:

    def __init__(self):
        db = sqlite3.connect("open_secrets_info")
        cur = db.cursor()

        self.db = db
        self.cur = cur

    # This removes the old tables from the database, used primarily for testing.
    def drop_database(self):
        try:
            self.cur.execute('drop table if exists candidates')
        except Exception as e:
            print("Error in drop_database method: " + e)

    # This creates the tables that use this information.
    def startup_database(self):
        try:
            self.cur.execute('create table if not exists candidates (candidate_id text, candidate_first_name text, candidate_last_name text, candidate_full_name text)')
        except Exception as e:
            print("Error in startup_database method: " + e)

    # this adds the data key for each of the individual candidate/members of Congress.
    def add_candidate_data(self):
        try:
            data_tuple_list = []
            f = open('candidate_data.txt', 'r')
            for line in f:
                line = line.strip("\n")
                line_list = line.split(",")
                adjusted_first_name = line_list[1].strip()
                adjusted_last_name = line_list[2].strip()
                full_name = str(line_list[1]) + str(line_list[2])
                full_name = full_name.strip()
                db_tuple = (line_list[0], adjusted_first_name, adjusted_last_name, full_name)
                data_tuple_list.append(db_tuple)

            f.close()
            self.cur.executemany('insert into candidates values (?, ?, ?, ?)', data_tuple_list)

        except Exception as e:
            print("Error in add_candidate_data method: " + e)

    # prints out the data.
    def print_out_data(self):
        try:
            self.cur.execute('select * from candidates')
            for item in self.cur:
                print(item)
        except Exception as e:
            print("Error in print_out_data method: " + e)

    def candidate_search(self, search_name):
        try:
            search_name_adjusted = "%" + search_name + "%"
            results_list = self.cur.execute('select candidate_id from candidates where candidate_first_name like ? or candidate_last_name like ? or candidate_full_name like ?', [search_name_adjusted, search_name_adjusted, search_name_adjusted])

            return results_list

        except Exception as e:
            print("Error in candidate_search method: " + e)

    # closes the database.
    def close_database(self):
        try:
            self.db.close()
            print("Database closed")
        except Exception as e:
            print("Error in close_database method: " + e)