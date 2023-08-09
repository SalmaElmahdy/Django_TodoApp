# Django TODO App :alarm_clock: :memo:
The Django TODO App is a simple web application that allows users to manage their tasks and stay organized. It provides basic CRUD (Create, Read, Update, Delete) functionalities, empowering users to create new tasks, view existing tasks, update task details, and delete tasks, and move to completed section  when they are marked as completed.

## Main Features
- **Create**: Users can easily create new tasks by providing a title and by default it marked as not completed task.
- **Read**: The app displays a list of all tasks, showing important information such as the task title, due date, and completion status.
- **Update**: Users can modify task details, such as the title.
- **Delete**: When a task is completed or no longer needed, users can delete it from the app, decluttering their task list.
- **Mark as Completed Task** :white_check_mark: : when user click on completed buttons its move to completed section
- **Undo Completed Task**:x: :when user make the task completed and that moved to completed section, they could undo that action by press marked as not completed task

## Folder Structure

The project follows the following folder structure:

- `TODOAPP/`: The main project directory.
  - `templates/`:
    - `edit_task.html`: Form to edit specific task
    -  `home.html`: Display all pending and completed tasks
  - `todo/`: Django app directory containing all the app-specific files.
    - `admin.py`: Change admin model to display task list in admin view to show task status and date of update
    - `models.py`: Contains the database models for TODO items. Defines the structure of the task data and handles interactions with the database.
    - `urls.py`: Contains all HTTP endpoints requests on task 
    - `views.py`: Defines the views and logic for handling HTTP requests. Contains functions or classes that handle the creation, updating, and deletion of tasks.
  - `todo_main/`:
      - `urls.py`: Contains all main HTTP end points such as admin/ and todo/
      - `views.py`: Contain retrival data from Database to display at home page
  - `manage.py`: Django management script. Provides various commands for managing the Django project, such as running the development server, applying database migrations, and creating new app components.

The folder structure is organized in a way that separates the app-specific files, such as models, views, templates, and static assets, within the `TODOAPP/` directory. This modular structure allows for better organization and separation of concerns, making it easier to maintain and extend the application.
