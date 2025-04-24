EduConnect: Smart Learning

Overview

EduConnect: Smart Learning is a web-based platform designed to streamline academic management and enhance the educational experience for administrators, teachers, students, and parents. Developed by Ajal P P at RISS Technologies, Thrissur, as part of a Bachelor of Computer Applications project at De Paul Institute of Science & Technology, this platform automates tasks like attendance tracking, assignment management, and assessments while integrating AI-driven features such as a chatbot for personalized doubt resolution. Built with scalability and user-friendliness in mind, EduConnect ensures seamless coordination, transparency, and accessibility across educational institutions.

Features

Admin Module:
Manage subjects, courses, teacher assignments, and system notifications.
Monitor academic processes and ensure secure data access.


Teacher Module:
Handle student profiles, attendance, lecture notes, and assessments.
Communicate with parents and provide feedback on assignments.


Student Module:
Access lecture notes, submit assignments, take assessments, and track progress.
Use an AI-powered chatbot for instant doubt resolution.


Parent Module:
View student profiles, attendance, and academic updates via real-time notifications.
Monitor progress and communicate with teachers.


General Features:
Real-time tracking of attendance, scores, and assignments.
Secure role-based authentication and data encryption.
Responsive design for web and Android accessibility.



Technologies Used

Frontend: HTML5, CSS, JavaScript, Bootstrap
Backend: Python (Django/Flask), MySQL
Mobile: Java (Android Studio for Parent Module)
Database: MySQL
Web Server: Apache/Nginx (XAMPP/WAMP for local deployment)
Development Tools: Visual Studio Code, PyCharm, Android Studio
Other: RESTful APIs, AI-driven chatbot integration

Installation
To set up the project locally, follow these steps:
Prerequisites

Hardware:
Processor: Intel or AMD Dual-Core or higher
RAM: 4GB or above
Storage: 128GB or above
Stable internet connection


Software:
Operating System: Windows 7+, macOS, or Linux
Python 3.7+
MySQL Server
Java 8+ (for Android app)
Git
XAMPP/WAMP (for local web server)



Steps

Clone the Repository:
git clone https://github.com/your-username/educonnect-smart-learning.git
cd educonnect-smart-learning


Set Up Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Configure Database:

Create a MySQL database named educonnect.
Update the database settings in settings.py (Django) or equivalent configuration file:DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'educonnect',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}




Run Migrations:
python manage.py makemigrations
python manage.py migrate


Set Up Android App (Optional for Parent Module):

Open the Android project in Android Studio.
Build and deploy the app to an emulator or Android device.


Start the Development Server:
python manage.py runserver


Access the web application at http://localhost:8000.



Usage

Admins:
Log in to manage courses, teachers, and notifications via the admin dashboard.


Teachers:
Upload resources, track attendance, grade assignments, and communicate with parents.


Students:
Access materials, submit assignments, take assessments, and use the chatbot for queries.


Parents:
Use the Android app or web platform to monitor student progress and receive updates.


Access:
Navigate to /admin for admin panel access (superuser credentials required).
Use role-based logins for respective modules.



Project Structure
educonnect-smart-learning/
├── manage.py               # Django project entry point
├── requirements.txt        # Python dependencies
├── educonnect_app/        # Main Django app
│   ├── migrations/         # Database migrations
│   ├── templates/         # HTML templates
│   ├── static/            # CSS, JS, and images
│   ├── models.py          # Database models
│   ├── views.py           # Request handlers
│   └── urls.py            # URL routing
├── android_app/           # Android Parent Module source
├── settings.py            # Django configuration
└── README.md              # Project documentation

Testing
The project includes:

Unit Testing: Validates individual components (e.g., authentication, chatbot responses).
Integration Testing: Ensures module interactions (e.g., assignment submission and grading).
System Testing: Verifies end-to-end workflows (e.g., resource access to notification).
Security Testing: Protects against unauthorized access and data breaches.
Performance Testing: Evaluates scalability and responsiveness.

Limitations

Internet Dependency: Requires stable connectivity for real-time features.
Limited AI: Chatbot handles predefined topics, struggles with complex queries.
No Offline Mode: Users cannot access or submit content without internet.
Manual Processes: Some tasks (e.g., pass approvals) require manual intervention.

Future Enhancements

Implement offline mode with smart caching for resource access and submissions.
Automate pass requests and complaint resolutions with AI-driven rules.
Enhance AI chatbot for broader query support and personalized learning plans.
Add advanced analytics for performance trends and resource optimization.
Introduce gamification (badges, points) to boost student engagement.

Contributors

Ajal P P (Developer, De Paul Institute of Science & Technology)

License
This project is licensed under the MIT License. See the LICENSE file for details.

References

Sommerville, Ian. Software Engineering, 10th Edition. Pearson Education, 2015.
Pressman, Roger S. Software Engineering: A Practitioner's Approach, 8th Edition. McGraw-Hill, 2014.
Django Documentation
Flask Documentation
W3Schools
Bootstrap Documentation
MySQL Documentation
DigitalOcean Django Tutorials
GeeksforGeeks
Draw.io

