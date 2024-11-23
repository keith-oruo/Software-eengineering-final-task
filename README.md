# Customer Feedback System

## Overview

This project is a simple Django-based application for managing customer feedback. Users can submit their feedback through a web form, and administrators can view the feedback reports. This system supports feedback submission, retrieval, and reporting.

## Features

- **Feedback Submission**: Customers can submit feedback with their name, email, and message.
- **Feedback Report**: Admins can view all submitted feedback in a report format.
- **REST API Endpoints**:
  - `POST /feedback/submit-feedback/`: Submit feedback.
  - `GET /feedback/feedback-report/`: View all submitted feedback.

## Requirements

- Python 3.x
- Django 3.x or higher
- Django REST Framework (for API endpoints)

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/customer-feedback-system.git
   cd customer-feedback-system
   ```

2. **Install dependencies**:

   It's recommended to create a virtual environment before installing the dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Apply migrations**:

   Set up the database and apply migrations:

   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional)**:

   If you'd like to create an admin account to access the admin panel, run:

   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**:

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

6. **Access the application**:

   - For the feedback form: `http://127.0.0.1:8000/feedback/submit-feedback/`
   - For the feedback report: `http://127.0.0.1:8000/feedback/feedback-report/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## API Endpoints

- **POST /feedback/submit-feedback/**: Submit a feedback message.
  - **Request body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane@example.com",
      "message": "Excellent experience!"
    }
    ```
  - **Response**:
    ```json
    {
      "message": "Feedback submitted successfully!"
    }
    ```

- **GET /feedback/feedback-report/**: Retrieve a list of all feedback submissions.
  - **Response**:
    ```json
    [
      {
        "name": "John Doe",
        "email": "john@example.com",
        "message": "Great service!"
      },
      {
        "name": "Jane Smith",
        "email": "jane@example.com",
        "message": "Excellent experience!"
      }
    ]
    ```

## Running Tests

To run the tests, make sure to have all dependencies installed and then use the following command:

```bash
python manage.py test
```

## Test Cases

The following test cases are included:

- **test_feedback_submission**: Tests the submission of feedback via the `POST /feedback/submit-feedback/` endpoint.
- **test_feedback_report**: Tests the retrieval of feedback using the `GET /feedback/feedback-report/` endpoint.

