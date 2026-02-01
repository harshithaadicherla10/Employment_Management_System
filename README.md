# Employee Management System

A full-stack web application built using Flask and MySQL to manage employee records with authentication and CRUD operations.

## Features
- User registration and login
- Forgot password functionality
- Add, update, and delete employee records
- Dashboard to view employees
- Session-based authentication
- Clean and simple UI

## Project Structure

employment-management-system/

├── app.py

├── requirements.txt

├── templates/

│ ├── register.html

│ ├── login.html

│ ├── forgot_password.html

│ ├── add_employee.html

│ ├── dashboard.html

│ └── edit_employee.html

├── static/

│ └── style.css


## Tech Stack
- Python
- Flask
- MySQL
- HTML
- CSS

## How to Run Locally
1. Clone the repository  
   git clone https://github.com/harshithaadicherla10/employee-management-system.git

2. Navigate to project directory  
   cd employee-management-system

3. Install dependencies  
   pip install -r requirements.txt

4. Run the application  
   python app.py

5. Open browser and visit  
   http://127.0.0.1:5000/

## Future Enhancements
- Role-based access (Admin / Employee)
- Search and pagination
- Password reset via email
