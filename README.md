# Sports Tournament Calendar System

A GenAI-powered solution for generating and managing up-to-date sports tournament calendars across multiple sports and competition levels — powered by **Python Flask** and **SQLite**.

Supports **12 sports** across **9 competition levels** with REST API and modern web interface.

---

# Features

* **Multi-sport tournament management** (Cricket, Football, Basketball, etc.)
* **Multiple competition levels** (Corporate to International)
* **REST API** with filtering capabilities
* **Modern responsive web interface**
* **SQLite database** for persistent storage
* **CSV and JSON export** functionality
* **Real-time tournament filtering and search**

---

# Project Structure

```text
sports-tournament-calendar/
├── main.py                       # Main application entry point
├── src/
│   ├── __init__.py
│   ├── data_collector.py         # Tournament data collection & validation
│   ├── database.py               # SQLite database operations
│   ├── api.py                    # Flask REST API server
│   └── ui/
│       ├── templates/
│       │   └── index.html        # Web interface template
│       └── static/
│           ├── style.css         # Modern responsive styling
│           └── script.js         # Frontend JavaScript logic
├── data/
│   └── tournaments.db            # SQLite database (auto-created)
├── output/
│   ├── tournaments.csv           # CSV export output
│   └── tournaments.json          # JSON export output
├── requirements.txt              # Python dependencies
└── README.md                     # This file  
```

---

# Setup Instructions
## 1. Clone/Download the Project
**Extract the provided zip file or clone if using git**
```bash
cd SportsCalendar
```

## 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

## 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 4. Set Up Environment
No additional environment variables needed. The application uses SQLite database which will be created automatically.  

## 5. Run the Application
```bash
python main.py
```

Open the links provided:
- Web Interface: http://localhost:5000
- API Base: http://localhost:5000/api

The application will automatically:
- Initialize the SQLite database
- Populate with sample tournament data
- Start the Flask web server

---

# How It Works
- **Data Initialization** → TournamentDataCollector generates sample tournaments
- **Database Storage** → SQLite stores all tournament information
- **Web Interface** → Modern UI for Browse and filtering tournaments
- **API Endpoints** → RESTful API for programmatic access
- **Export Functions** → Generate CSV/JSON outputs on demand
- **Real-time Filtering** → Dynamic search by sport and competition level

All tournament data follows the structured schema:  
```bash
{
  "Tournament Name": "IPL 2025",
  "Sport": "Cricket",
  "Level": "International",
  "Start Date": "2025-03-15",
  "End Date": "2025-05-30",
  "Tournament Official URL": "[https://example.com/ipl-2025](https://example.com/ipl-2025)",
  "Streaming Partners/Links": ["Star Sports", "Hotstar"],
  "Tournament Image": "[https://example.com/images/cricket.jpg](https://example.com/images/cricket.jpg)",
  "Summary of Tournament": "Premier cricket tournament featuring top teams."
}
```

---

# Supported Sports & Levels
## Sports Covered
- Cricket
- Football
- Badminton
- Running
- Gym
- Cycling
- Swimming
- Kabaddi
- Yoga
- Basketball
- Chess
- Table Tennis

## Competition Levels
- Corporate
- School
- College/University
- Club/Academy
- District
- State
- Zonal/Regional
- National
- International

---

# API Endpoints

## Get All Tournaments
```bash
GET /api/tournaments
```

## Filter Tournaments
```bash
GET /api/tournaments?sport=Cricket
GET /api/tournaments?level=National
GET /api/tournaments?sport=Football&level=International
```
## Export Data
```bash
GET /api/export/csv
GET /api/export/json
Get Available Options
```

```bash
GET /api/sports
GET /api/levels
```

---

# Sample Usage
After starting the application, try:
## Web Interface
- Browse tournaments by sport/level
- Export data using CSV or JSON buttons
- View detailed tournament information

## API Testing
```bash
# Test basic API
curl http://localhost:5000/api/tournaments

# Test filtering
curl "http://localhost:5000/api/tournaments?sport=Cricket"

# Test export
curl http://localhost:5000/api/export/csv
```

---

# System Architecture

```
┌─────────────────┐    ┌──────────────┐    ┌─────────────┐
│  Data Collector │────│  SQLite DB   │────│  Flask API  │
└─────────────────┘    └──────────────┘    └─────────────┘
                                                    │
                                            ┌─────────────┐
                                            │   Web UI    │
                                            └─────────────┘
                                                    │
                                            ┌─────────────┐
                                            │ Export Files│
                                            └─────────────┘
```

## Components:
- **Data Collector**: Handles tournament data gathering and validation
- **Database Manager**: SQLite operations with structured schema
- **API Server**: Flask-based REST endpoints
- **Web Interface**: Modern responsive UI with filtering
- **Export System**: CSV and JSON generation

---

# Current Limitations & Future Improvements
## Current Limitations
- Uses sample data instead of real tournament feeds
- No automatic data refresh mechanism
- Placeholder URLs for tournament images
- No authentication or API rate limiting

## Planned Improvements
- **Real Data Integration**: ESPN API, SportRadar, web scraping
- **Real-time Updates**: Scheduled data refresh and notifications
- **Mobile App**: Companion mobile application
- **Production Ready**: Docker, CI/CD, monitoring
- **Enhanced Search**: Advanced filtering and recommendations
- **User Features**: Favorites, personalized calendars

---
# Database Schema
```SQL
CREATE TABLE tournaments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sport TEXT NOT NULL,
    level TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    official_url TEXT,
    streaming_links TEXT,
    image_url TEXT,
    summary TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);
```

---

#  Output Files
The system generates:
- `output/tournaments.csv`: Structured CSV export
- `output/tournaments.json`: JSON format export
- `data/tournaments.db`: SQLite database file

---

# License
This project is licensed under the MIT License - see the LICENSE.md file for details.