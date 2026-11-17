# CampusConnect — Smart Campus Placement & Job Tracking Portal

A responsive SESD academic project built using **HTML, CSS, JavaScript and Python Flask**. It does not require a database.

## Features
- Student dashboard with Applied, Shortlisted, Selected and Rejected statistics and chart
- Skill-based job recommendations ranked using skills entered in the student profile
- Searchable and filterable job/internship listings
- Job detail modal and quick-apply workflow
- Application tracking with demo status progression
- Placement drive, workshop and interview event listing
- Notification bell: students are notified when an application is marked Selected or Rejected
- Notify a known person (parent/friend/mentor) automatically when an application is Selected or Rejected, plus a "Notify contact" button per application
- Student profile form
- Browser `localStorage` persistence
- Flask server to run the website locally
- Responsive desktop, tablet and mobile layout

## Folder structure
```
smart_campus_placement_portal/
├── app.py
├── requirements.txt
├── index.html
├── style.css
├── script.js
└── README.md
```

## Run with Flask
1. Install Python 3.
2. Open a terminal in this project folder.
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Start the server:
   ```bash
   python app.py
   ```
5. Open this address in your browser:
   `http://127.0.0.1:5000`

The `/api/health` endpoint checks whether the server is running. A demo `/api/contact-placement-cell` endpoint validates a JSON contact request.

## Run without Flask
You can also open `index.html` directly in a browser, or use VS Code Live Server.

## Demo behavior and limitations
- The portal starts with sample companies, vacancies and placement events.
- Applying to a job adds it to **My Applications**.
- The **Update status** action cycles through sample statuses for demonstration. In a real deployment, only authorized placement staff should update application outcomes.
- Profile and application data are stored in the current browser using localStorage. They are not shared between devices or users.
- Skill-based recommendations compare the skills entered in My Profile with the skills listed for each vacancy. Add comma-separated skills such as Python, Machine Learning, SQL, Java, HTML, CSS or CNN to personalize the dashboard.
- The chart uses Chart.js from a CDN, so an internet connection is needed for the chart. The rest of the interface works locally.
- The Flask contact endpoint validates submitted details but does not email or persist them.
- This is a front-end academic prototype with a Flask server wrapper, not a production recruitment system. Real authentication, role-based access, secure resume uploads, server-side validation and a database would be needed for deployment.

## Technology stack
- HTML5 — page structure
- CSS3 — responsive design and styling
- JavaScript — navigation, filtering, application workflow and local storage
- Python Flask — local web server and sample API endpoints
- Chart.js — dashboard visualization
