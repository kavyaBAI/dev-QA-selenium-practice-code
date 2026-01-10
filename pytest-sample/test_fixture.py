import pytest

class TDatabase:
    def connect(self, config):
        print(f"--- Establishing real connection to {config['NAME']} ---")
        return {"session": "ID_12345", "config": config}

    def close(self):
        print("--- MySQL Connection Pool: Connection Released ---")

@pytest.fixture
def db_connection():
    db_config = {
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'seedar_v1',
        'USER': 'root',
        'PASSWORD': 'kavya1822',
    }
    db = TDatabase()
    connection = db.connect(db_config)
    yield connection  
    print(f"\n[Cleaning up session {connection['session']}...")
    db.close()



def test_database_identity(db_connection):
    print("Verify Database Name")
    assert db_connection['config']['NAME'] == 'seedar_v1'

def test_database_read_access(db_connection):
    print("Verify Session is Active")
    assert "ID_" in db_connection['session']