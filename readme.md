# **Hairdresser App**

The **Hairdresser App** is a comprehensive web-based platform built using Django to facilitate the interaction between hairdressers and clients. The application allows clients to schedule appointments, manage their bookings, and leave reviews, while hairdressers can handle their schedules, manage their clients, and receive feedback. The app is designed with a focus on ease of use, responsiveness, and security.

---

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Application Structure](#application-structure)
4. [Database Models](#database-models)
5. [Features and Functionality](#features-and-functionality)
    - [User Registration](#user-registration)
    - [User Login](#user-login)
    - [Dashboard (Client and Hairdresser)](#dashboard-client-and-hairdresser)
    - [Profile Management](#profile-management)
    - [Appointment Management](#appointment-management)
    - [Review System](#review-system)
    - [Logout and Error Handling](#logout-and-error-handling)
6. [Interactive Components](#interactive-components)
7. [Security and Authentication](#security-and-authentication)
8. [Deployment and Setup](#deployment-and-setup)


---

## **Project Overview**

The **Hairdresser App** serves as a platform that bridges the gap between hairdressers and clients, allowing clients to book services, manage appointments, and leave feedback, while providing hairdressers with tools to organize their availability, handle appointments, and review client feedback.

The platform consists of two primary user types:

- **Clients**: Users who can book appointments and leave reviews.
- **Hairdressers**: Professionals who provide services and manage client appointments.

The app includes a user-friendly interface, appointment scheduling through a calendar, and an integrated review system to enhance user experience on both ends.

---

## **Technologies Used**

### **Backend**

- **Python 3.x**: Main programming language.
- **Django 4.2.6**: Web framework providing routing, ORM, and admin interface.
- **Django ORM**: To interact with the PostgreSQL database.
- **PostgreSQL**: Relational database management system for storing data.
- **Django Crispy Forms**: For better form handling and rendering.
- **Django Auth**: For secure user authentication and session management.

### **Frontend**

- **HTML/CSS**: For page structuring and design.
- **Bootstrap 4.5.2**: CSS framework for responsive design.
- **Font Awesome**: For icons and design enhancements.
- **JavaScript**: For adding interactivity to the application.
- **jQuery 3.5.1**: For simplified DOM manipulation and AJAX handling.
- **FullCalendar 6.1.15**: JavaScript library for interactive calendar management.
- **Animate.css**: For smooth animations to enhance user experience.

### **Other**
- **Gunicorn**: WSGI HTTP server for running the Django application in production.
- **Nginx**: Reverse proxy server.
- **SSL**: For secure communication over HTTPS.

---

## **Application Structure**

The project is organized into the following Django apps:

1. **hairdressers/**: Manages hairdresser profiles, schedules, and reviews.
2. **clients/**: Handles client profiles and appointment bookings.
3. **appointments/**: Manages the creation, modification, and deletion of appointments.
4. **reviews/**: Manages the review system, allowing clients to leave feedback for hairdressers.

The main directories and files are:

- `manage.py`: The command-line utility for running the project.
- `settings.py`: Contains configuration settings, including the database, static files, and installed applications.
- `urls.py`: The root URL configuration file, routing all incoming requests to the appropriate views.

---

## **Database Models**

The application uses PostgreSQL to store data, and Django ORM manages the interactions. Key models are:

1. **User Model**: Handles user authentication, linked to the `Client` and `Hairdresser` models.
2. **Hairdresser Model**:
   - Linked to the `User` model via a `ForeignKey`.
   - Stores specialization, experience, and availability.
3. **Client Model**:
   - Linked to the `User` model via a `ForeignKey`.
   - Represents users who book appointments.
4. **Appointment Model**:
   - Links `Client` and `Hairdresser`.
   - Contains appointment details like service, date, time, and duration.
5. **Review Model**:
   - Links `Client` and `Hairdresser`.
   - Stores reviews and ratings (1-5 stars).

---

## **Features and Functionality**

### **User Registration**

- **Home Page**: Provides buttons for users to register or log in.
- **Registration Page**:
  - The user selects their role (Client or Hairdresser).
  - The registration form is customized based on the selected role.
  - Validation ensures correct and complete input.
- **Outcome**:
  - Valid: Creates a new `User` and either a `Client` or `Hairdresser` object.
  - Invalid: Errors are displayed, and the user remains on the registration page.

### **User Login**

- **Home Page**: The user can click **Login**.
- **Login Page**:
  - Users input their email and password.
  - If the login is successful, the user is redirected to the appropriate dashboard.

### **Dashboard (Client and Hairdresser)**

#### **Client Dashboard**
- Displays upcoming appointments with options to view, edit, and cancel.
- The client can create a new appointment, filling out the necessary details like date, time, service, and selecting a hairdresser.

#### **Hairdresser Dashboard**
- Displays all appointments associated with the hairdresser.
- Options to view, edit, and delete appointments.
- The hairdresser can manage services and view client reviews.

### **Profile Management**

- **Profile Page**: The user can view and edit their profile.
- **Role Switching**: Users can switch between being a client or hairdresser. When switching roles, they are prompted for confirmation.

### **Appointment Management**

- **Appointment Creation Page**:
  - Users select date, time, service, and hairdresser.
  - Appointments are saved in the database and displayed on the dashboard.
- **Appointment Edit Page**:
  - Users can modify existing appointments and save changes.
- **Appointment Delete Page**:
  - Users can delete appointments with a confirmation.

### **Review System**

- **Clients**: Can leave reviews for hairdressers.
- **Hairdressers**: Can view reviews and ratings from clients.
  
### **Logout and Error Handling**

- **Logout**: Users can log out from anywhere in the application.
- **Error Handling**: The application shows error messages during form submissions (e.g., invalid data or incorrect credentials).

---

## **Interactive Components**

- **FullCalendar**: Used in both client and hairdresser dashboards to display and manage appointments.
  - Users can view, create, and edit appointments through the calendar interface without page reloads.
  - AJAX is used to fetch, update, and manage appointment data in real-time.
  
- **Bootstrap & Responsive Design**: Ensures that the application works seamlessly on all devices, including mobile phones and tablets.

---

## **Security and Authentication**

- **Django Auth**: Provides secure user authentication and session management.
- **CSRF Protection**: CSRF tokens are used to secure forms and prevent CSRF attacks.
- **Password Hashing**: Passwords are stored using Django’s built-in hashing mechanism.
- **Role-based Access Control**: Based on the user role (Client or Hairdresser), different permissions and views are assigned.

---

## **Deployment and Setup**

### **Prerequisites**

- **Python 3.x** installed.
- **PostgreSQL** installed and configured.

### **Installation Steps**

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-repository/hairdresser-app.git
   cd hairdresser-app

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
    pip install -r requirements.txt
