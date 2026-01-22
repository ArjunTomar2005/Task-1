# Task-1
📋 Project Overview
A modern, responsive portfolio website built with Flask backend and custom HTML/CSS frontend. This application showcases professional skills, experience, projects, and contact information with an elegant design and interactive features.

🚀 Live Demo
Local: http://localhost:5000

Network: http://[your-ip]:5000

✨ Features
Responsive Design: Mobile-friendly layout with CSS media queries

Modern UI: Gradient backgrounds, animations, and interactive elements

Multi-section Layout:

Hero section with profile introduction

Technical skills showcase

Professional experience timeline

Projects portfolio

Education and certifications

Core strengths display

Awards and leadership

Contact section

Flask Backend:

Dynamic routing

Resume PDF download functionality

Contact form handling (ready for integration)

Local network accessibility

🛠️ Technologies Used
Backend:
Python 3.x

Flask - Web framework

Socket Programming - Network accessibility

Frontend:
HTML5 - Semantic markup

CSS3 - Custom styling with animations

JavaScript - Interactive features

Font Awesome - Icons library

📁 Project Structure
text
portfolio-website/
│
├── app.py                    # Main Flask application
├── Arjun_Tomar_Resume.pdf    # Resume PDF file
├── requirements.txt          # Python dependencies
└── templates/
    └── index.html           # Main HTML template
⚙️ Installation & Setup
Prerequisites
Python 3.7 or higher

pip (Python package manager)

Step-by-Step Installation
Clone the Repository

bash
git clone https://github.com/your-username/portfolio-website.git
cd portfolio-website
Create Virtual Environment (Recommended)

bash
python -m venv venv
On Windows: venv\Scripts\activate

On Mac/Linux: source venv/bin/activate

Install Dependencies

bash
pip install -r requirements.txt
If requirements.txt doesn't exist, install Flask directly:

bash
pip install flask
Add Your Resume

Place your resume PDF in the project root as Arjun_Tomar_Resume.pdf

Or update the filename in app.py line 24:

python
resume_path = os.path.join(os.path.dirname(__file__), 'YOUR_RESUME.pdf')
Run the Application

bash
python app.py
Access the Website

Open your browser and navigate to:

Local: http://localhost:5000

Network: http://[your-ip]:5000 (as shown in terminal)

🎨 Customization Guide
1. Personal Information
Edit templates/index.html to update:

Name and title (line 400-410)

Contact information (line 395-405)

Profile picture/initials (line 385)

About/summary text (line 410-425)

2. Professional Sections
Update content in respective sections:

Skills: Lines 490-630

Experience: Lines 640-730

Projects: Lines 740-810

Education: Lines 820-870

Strengths: Lines 880-950

Awards: Lines 960-1010

3. Styling
Modify CSS in the <style> section (lines 15-380):

Colors: Update gradient backgrounds and theme colors

Layout: Adjust padding, margins, and grid layouts

Animations: Customize keyframes and transitions

4. Resume/PDF
Replace Arjun_Tomar_Resume.pdf with your own resume file

🔧 Technical Details
Flask Routes
/ - Home page (renders index.html)

/download-cv - Resume PDF download endpoint

/submit-contact - Contact form submission (POST endpoint)

Responsive Design
Mobile-first approach

Media queries for different screen sizes

Flexible grid layouts

Features Implementation
Smooth Scrolling: JavaScript for navigation

Scroll Animations: Intersection Observer API

Active Navigation: Dynamic class toggling

Download Functionality: Flask send_file for PDFs

🐛 Troubleshooting
Common Issues:
"Port already in use" error

bash
# Kill process on port 5000
# Windows:
netstat -ano | findstr :5000
taskkill /PID [PID] /F

# Mac/Linux:
lsof -i :5000
kill -9 [PID]
ModuleNotFoundError: No module named 'flask'

bash
pip install flask
Resume not downloading

Ensure Arjun_Tomar_Resume.pdf exists in project root

Check file permissions

Styles not loading

All CSS is inline in index.html

No external dependencies needed

📱 Browser Compatibility
Chrome 60+

Firefox 55+

Safari 12+

Edge 79+

Mobile browsers (iOS Safari, Chrome for Android)

🔄 Future Enhancements
Database integration for dynamic content

Admin panel for content management

Blog section

Dark/Light mode toggle

Contact form with email integration

Project filtering by category

Multi-language support

Analytics integration

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Font Awesome for icons

Flask community for excellent documentation

All contributors and testers

📞 Contact
Arjun Tomar - tomararjun162@gmail.com

Project Link: https://github.com/ArjunTomar2005/portfolio-website

⭐ Support
If you like this project, please give it a star on GitHub!

Note: Remember to update the following before deployment:

Contact information in HTML

GitHub repository links

Resume/CV file

Any personal/confidential information

Social media links

Happy coding! 🚀
