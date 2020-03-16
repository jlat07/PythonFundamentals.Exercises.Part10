import json
import pickle



class PersistenceUtils:
# create PersistenceUtils static method

    def load_pickle():
        f = open(saved_accounts.pickle, 'rb')
        b = pickle.load(f)
        self.accounts = (eval(json.dumps(b)))
        f.close()
        f = open(saved_customers.pickle, 'rb')
        b = pickle.load(f)
        self.customers = (eval(json.dumps(b)))
        f.close()
    
        return self.accounts, self.customers


    def write_pickle():
        dbc = self.customers
        dba = self.accounts
        f = open(saved_accounts.pickle, 'wb')  # (wb) write-binary mode
        pickle.dump(dba, f)
        f.close()
        f = open(saved_customers.pickle, 'wb')  # (wb) write-binary mode
        pickle.dump(dbc, f)
        f.close()

def write_pickle(file_name, data):
    with open(file_name, "wb") as handler:
        pickle.dump(data, handler)


# PART D
def load_pickle(pickle_file):
    with open(pickle_file, 'rb') as handler:
        data = pickle.load(handler)
    return data
