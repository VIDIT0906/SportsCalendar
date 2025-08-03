import sqlite3
import json
from typing import List, Dict, Optional
from datetime import datetime

class TournamentDatabase:
    def __init__(self, db_path: str = "data/tournaments.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database with tournament table"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tournaments (
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
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def insert_tournament(self, tournament_data: Dict) -> int:
        """Insert a new tournament into the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO tournaments 
        (name, sport, level, start_date, end_date, official_url, 
         streaming_links, image_url, summary)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            tournament_data['name'],
            tournament_data['sport'],
            tournament_data['level'],
            tournament_data['start_date'],
            tournament_data['end_date'],
            tournament_data.get('official_url', ''),
            json.dumps(tournament_data.get('streaming_links', [])),
            tournament_data.get('image_url', ''),
            tournament_data.get('summary', '')
        ))
        
        tournament_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return tournament_id
    
    def get_all_tournaments(self) -> List[Dict]:
        """Retrieve all tournaments from the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM tournaments ORDER BY start_date')
        rows = cursor.fetchall()
        
        tournaments = []
        for row in rows:
            tournament = {
                'id': row[0],
                'name': row[1],
                'sport': row[2],
                'level': row[3],
                'start_date': row[4],
                'end_date': row[5],
                'official_url': row[6],
                'streaming_links': json.loads(row[7]) if row[7] else [],
                'image_url': row[8],
                'summary': row[9],
                'created_at': row[10],
                'updated_at': row[11]
            }
            tournaments.append(tournament)
        
        conn.close()
        return tournaments
    
    def filter_tournaments(self, sport: str = None, level: str = None) -> List[Dict]:
        """Filter tournaments by sport and/or level"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = 'SELECT * FROM tournaments WHERE 1=1'
        params = []
        
        if sport:
            query += ' AND sport = ?'
            params.append(sport)
        
        if level:
            query += ' AND level = ?'
            params.append(level)
        
        query += ' ORDER BY start_date'
        
        cursor.execute(query, params)
        rows = cursor.fetchall()
        
        tournaments = []
        for row in rows:
            tournament = {
                'id': row[0],
                'name': row[1],
                'sport': row[2],
                'level': row[3],
                'start_date': row[4],
                'end_date': row[5],
                'official_url': row[6],
                'streaming_links': json.loads(row[7]) if row[7] else [],
                'image_url': row[8],
                'summary': row[9]
            }
            tournaments.append(tournament)
        
        conn.close()
        return tournaments