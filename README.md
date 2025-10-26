# IT Helpdesk Tracker

A simple web application to track IT support tickets, built with **Python** and **Flask**. Tickets are color-coded by priority (High, Medium, Low) and can be updated with status changes. This app is designed for local use and learning purposes.

---

## Features

- Add, view, and update IT support tickets  
- Automatic priority assignment based on ticket description  
- Tickets color-coded:  
  - High → Red  
  - Medium → Yellow  
  - Low → Green  
- Closed tickets remain in the system for record-keeping  
- Export tickets to CSV  

---

## Installation and Setup

Follow these steps to run the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/MitaliHukkeri/it-helpdesk-tracker.git
cd it-helpdesk-tracker

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate

# 4. Install dependencies
python -m pip install -r requirements.txt

# 5. Run the Flask application
python app.py

# 6. Open in your browser
# Navigate to http://127.0.0.1:5000

```markdown

Project Structure

it-helpdesk-tracker/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── templates/ # HTML templates
│ ├── index.html
│ ├── add_ticket.html
│ └── update_ticket.html
├── static/ # CSS and static files
│ └── style.css
└── .gitignore # Git ignore rules

