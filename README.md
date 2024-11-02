Task Management Web App with Django
===================================

This project is a web application built with Django to manage tasks efficiently using CRUD operations. It includes both traditional web views and REST API endpoints for flexible task management. The application leverages Django’s powerful features and the Django REST Framework to provide a robust backend.

----------------------------------------------
Table of Contents
----------------------------------------------
1. Project Overview
2. Features
3. Technology Stack
4. Project Structure
5. Detailed Descriptions
6. How to Run the Project
7. Future Enhancements

----------------------------------------------
1. Project Overview
----------------------------------------------
The Task Management Web App is designed to facilitate task management by offering both a web-based interface and a set of RESTful API endpoints. Users can create, read, update, and delete tasks seamlessly, with a well-structured data model to support efficient data handling.

----------------------------------------------
2. Features
----------------------------------------------
- **Task CRUD Operations**: Create, view, update, and delete tasks through web views and API endpoints.
- **API Endpoints**: RESTful API support using the Django REST Framework for external integrations or mobile app backends.
- **Interactive Web Interface**: User-friendly task management through a web interface built with Django views.
- **Data Validation**: Ensures proper data input and validation for reliable performance.

----------------------------------------------
3. Technology Stack
----------------------------------------------
- **Backend**: Python, Django, Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS (for Django templates)
- **Others**: Django’s built-in authentication, CSRF protection

----------------------------------------------
4. Project Structure
----------------------------------------------
- **models.py**: Defines the `Tache` model with fields for `titre`, `description`, `date_de_creation`, and `statut`.
- **views.py**: Contains class-based views for handling CRUD operations and API views using Django REST Framework.
- **urls.py**: Maps URL patterns to the corresponding views for both web and API routes.
- **serializers.py**: Implements the `TacheSerializer` to transform the `Tache` model into JSON for API responses.

----------------------------------------------
5. Detailed Descriptions
----------------------------------------------
### 5.1 Models
The `Tache` model represents a task, including attributes like title, description, creation date, and status. It serves as the primary data structure for the project.

### 5.2 Views
- **TacheListView**: Lists all tasks in the web view.
- **TacheDetailView**: Displays details of a specific task.
- **TacheCreateView**: Allows users to create a new task.
- **TacheUpdateView**: Enables task editing.
- **TacheDeleteView**: Handles task deletion.

### 5.3 API Views
- **TacheListCreateAPIView**: Provides a RESTful API for listing and creating tasks.
- **TacheRetrieveUpdateDestroyAPIView**: Handles retrieving, updating, and deleting tasks via the API.

----------------------------------------------
6. How to Run the Project
----------------------------------------------
### Prerequisites
- Python 3.10+
- PostgreSQL database setup
- Django 5.1
- Django REST Framework

### Steps to Run
1. **Clone the repository**
2. **Install dependencies** 
3. **Configure the database settings** in `settings.py` with your PostgreSQL credentials.
4. **Apply migrations**: `python manage.py migrate`
5. **Run the server**: `python manage.py runserver`
6. **Access the web app** at `http://localhost:8000`

----------------------------------------------
7. Future Enhancements
----------------------------------------------
- **User Authentication**: Add user login and permissions for task management.
- **Enhanced UI**: Improve the frontend with JavaScript frameworks like React or Vue.js.
- **Task Filters**: Implement filters based on status, date, and other criteria.
- **Email Notifications**: Add email reminders for upcoming tasks.

