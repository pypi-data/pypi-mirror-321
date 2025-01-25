from ttask_manager import TaskManager
import pytest

# def test_class_instantiation():
#     with pytest.raises(ValueError):
#         TaskManager(priority_levels=[1,2,3,4,5,"hello"])
#     with pytest.raises(ValueError):
#         TaskManager(default_priority="Breaking the rules")
#
# def test_add_task():
#     task_manager = TaskManager()
#     assert task_manager.add_task("test the project") in "test the project (Priority: medium) added successfully."

task_manager = TaskManager()

task_manager.add_task(("Buy groceries", "high"), ("Clean the house", "medium"), ("Complete homework", "low"), ("Go to the gym", "high"))
task_manager.add_task(("Buy groceries", "high"), ("Clean the house", "medium"), ("Complete homework", "low"), ("Go to the gym", "high"))
task_manager.add_task("Walk the dog")  # Should take the default priority



# task_manager.add_task(("Cook dinner", "urgent"))  # Invalid priority
# task_manager.add_task(("Study for exam", 5)) # Invalid numerical priority if "5" is not in the predefined levels

task_manager.remove_task("Go to the gym","Nonexistent task")

task_manager.task_done("Buy groceries","Complete homework")

task_manager.current_state('both')

task_manager.save_current_state('./empty.json')  # Save current state

