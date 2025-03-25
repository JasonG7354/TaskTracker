# TaskTracker
This is based on this project https://roadmap.sh/projects/task-tracker.
CLI Python app that will track your tasks.
This project is based on the following website: https://roadmap.sh/projects/task-tracker

The purpose of this project is too get familiar with Python programming. I took a course on C, javascript and Python and programming language in 2020. I have not dabbled with a programming language since then. I also have knowledge of HTML/CSS/Javascript. I enjoy creating projects rather than learning from a tutorial. I feel like projects help you search for the answer your looking for and helps you think like a programmer. I plan to improve my projects once I get more knowledge and familiar with the language. As for now this is my first project. 

In this project I learned how to interact with a JSON file with python. The purpose of this project is to allow a user to add, update, and delete a task. The program will save the task into a JSON file. The program can then update or delete the task from the JSON file. Each task will have a unique ID and it will have the time it was created or updated. It also has the status of each task. 

**Instructions**
# Adding a new task
task-cli add "Buy groceries"

# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
