#!/usr/bin/env python3
"""
Sports Tournament Calendar - Main Application
GenAI Intern Assignment Implementation
"""

import os
import sys
from src.database import TournamentDatabase
from src.data_collector import TournamentDataCollector
from src.api import app

def initialize_data():
    """Initialize the database with sample tournament data"""
    print("Initializing database...")
    
    # Create data directory
    os.makedirs('data', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    
    # Initialize database
    db = TournamentDatabase()
    
    # Check if we need to populate with sample data
    existing_tournaments = db.get_all_tournaments()
    
    if len(existing_tournaments) == 0:
        print("Populating database with sample tournaments...")
        
        # Collect tournament data
        collector = TournamentDataCollector()
        tournaments = collector.collect_real_tournament_data()
        
        # Insert tournaments into database
        for tournament in tournaments:
            if collector.validate_tournament_data(tournament):
                db.insert_tournament(tournament)
                print(f"Added: {tournament['name']} ({tournament['sport']})")
            else:
                print(f"Skipped invalid tournament: {tournament.get('name', 'Unknown')}")
        
        print(f"Successfully added {len(tournaments)} tournaments to the database.")
    else:
        print(f"Database already contains {len(existing_tournaments)} tournaments.")

def main():
    """Main application entry point"""
    print("=== Sports Tournament Calendar System ===")
    print()
    
    # Initialize data
    initialize_data()
    
    print("\n=== Starting Web Application ===")
    print("Access the application at: http://localhost:5000")
    print("API endpoints:")
    print("  GET /api/tournaments - Get all tournaments")
    print("  GET /api/tournaments?sport=Cricket - Filter by sport")
    print("  GET /api/tournaments?level=National - Filter by level")
    print("  GET /api/export/csv - Export to CSV")
    print("  GET /api/export/json - Export to JSON")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        # Start the Flask application
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n\nShutting down gracefully...")
        sys.exit(0)

if __name__ == "__main__":
    main()