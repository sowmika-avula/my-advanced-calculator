from calculator.history_manager import HistoryManager
import pandas as pd
import os

def test_add_record():
    hm = HistoryManager()
    hm.add_record("2 + 3", 5)
    assert hm.history.iloc[0]["Operation"] == "2 + 3"
    assert hm.history.iloc[0]["Result"] == 5

def test_save_and_load_history():
    hm = HistoryManager()
    hm.add_record("3 * 4", 12)
    hm.save_history()

    hm2 = HistoryManager()
    hm2.load_history()
    assert not hm2.history.empty

    # Cleanup
    os.remove("history.csv")

def test_clear_history():
    hm = HistoryManager()
    hm.add_record("test", 0)
    hm.clear_history()
    assert hm.history.empty

def test_reset():
    hm = HistoryManager()
    hm.add_record("test", 0)
    hm.save_history()
    hm.reset()
    assert hm.history.empty
    assert not os.path.exists("history.csv")

def test_save_empty_history():
    hm = HistoryManager()
    hm.clear_history()
    hm.save_history()

    # Verify file exists with headers only
    assert os.path.exists("history.csv")
    with open("history.csv", "r") as f:
        content = f.read().strip()
        assert content == "Operation,Result"

    # Cleanup
    os.remove("history.csv")
