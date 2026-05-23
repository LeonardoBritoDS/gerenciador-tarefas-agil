import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture(autouse=True)
def setup_test_db(monkeypatch, tmp_path):
    db_file = tmp_path / "test_tasks.db"
    db_path = str(db_file)
    
    monkeypatch.setenv("DATABASE_PATH", db_path)
    
    from src.database import init_db
    init_db()
    
    yield
