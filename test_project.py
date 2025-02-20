import pytest
from datetime import datetime
from project import add_goal, mark_as_completed, update_progress, goals

@pytest.fixture
def reset_goals():
    """Fixture to reset goals list before each test"""
    global goals
    goals.clear()  # Reset the goals list before each test

def test_add_goal_valid_date(reset_goals):
    """Test adding a goal with a valid date"""
    response = add_goal("Learn Python", "20-12-2025")
    assert "Goal added" in response
    assert len(goals) == 1
    assert goals[0]["description"] == "Learn Python"
    assert goals[0]["due_date"] == datetime.strptime("20-12-2025", "%d-%m-%Y")
    assert goals[0]["completed"] is False
    assert goals[0]["progress"] == 0

def test_add_goal_invalid_date(reset_goals):
    """Test adding a goal with an invalid date format"""
    response = add_goal("Invalid Date Goal", "2025/12/20")
    assert response == "Invalid date format! Please enter the date in the format DD-MM-YYYY."
    assert len(goals) == 0  # Goal should not be added

def test_mark_as_completed(reset_goals):
    """Test marking a goal as completed"""
    add_goal("Read 10 books", "15-11-2025")
    response = mark_as_completed(1)
    assert response == "Goal 1 marked as completed."
    assert goals[0]["completed"] is True

def test_mark_as_completed_invalid(reset_goals):
    """Test marking a non-existent goal as completed"""
    response = mark_as_completed(1)
    assert response == "Invalid goal number."

def test_update_progress_valid(reset_goals):
    """Test updating progress of a goal with a valid percentage"""
    add_goal("Go to the gym", "10-08-2025")
    response = update_progress(1, 50)
    assert response == "Goal 1 progress updated to 50%."
    assert goals[0]["progress"] == 50

def test_update_progress_out_of_range(reset_goals):
    """Test updating progress with an out-of-range percentage"""
    add_goal("Save money", "01-01-2026")
    response = update_progress(1, 150)  # Invalid progress value
    assert response == "Progress must be between 0 and 100."
    assert goals[0]["progress"] == 0  # Should not have changed

def test_update_progress_invalid_goal(reset_goals):
    """Test updating progress for a non-existent goal"""
    response = update_progress(1, 30)
    assert response == "Invalid goal number."
