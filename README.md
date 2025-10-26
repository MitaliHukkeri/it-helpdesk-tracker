# IT Helpdesk Tracker

## Project Description
The **IT Helpdesk Tracker** is a simple web application built using **Python and Flask** for managing IT support tickets. It allows users to:

- Add new support tickets with a title and description.  
- Automatically assign ticket priority based on the description.  
- Update ticket status and priority.  
- View all tickets in a clean, color-coded table for easy tracking.  
- Export tickets to CSV for reporting purposes. 
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
```

## Notes

- Tickets are color-coded by priority: High – red, Medium – yellow, Low – green.
- Closed tickets are kept for records and are not deleted.
- Intended for local use and learning purposes. For production deployment, use a proper web server and database.

## Author

Mitali Hukkeri  
GitHub: [https://github.com/MitaliHukkeri](https://github.com/MitaliHukkeri)

