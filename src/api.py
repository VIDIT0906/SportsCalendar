from flask import Flask, jsonify, request, render_template
from src.database import TournamentDatabase
import csv
import json
import os

app = Flask(__name__, template_folder='ui/templates', static_folder='ui/static')
db = TournamentDatabase()

@app.route('/')
def index():
    """Serve the main UI"""
    return render_template('index.html')

@app.route('/api/tournaments', methods=['GET'])
def get_tournaments():
    """API endpoint to get tournaments with optional filtering"""
    sport = request.args.get('sport')
    level = request.args.get('level')
    
    if sport or level:
        tournaments = db.filter_tournaments(sport=sport, level=level)
    else:
        tournaments = db.get_all_tournaments()
    
    return jsonify({
        'status': 'success',
        'count': len(tournaments),
        'tournaments': tournaments
    })

@app.route('/api/sports', methods=['GET'])
def get_sports():
    """Get list of all sports"""
    sports = [
        "Cricket", "Football", "Badminton", "Running", "Gym",
        "Cycling", "Swimming", "Kabaddi", "Yoga", "Basketball",
        "Chess", "Table Tennis"
    ]
    return jsonify({'sports': sports})

@app.route('/api/levels', methods=['GET'])
def get_levels():
    """Get list of all tournament levels"""
    levels = [
        "Corporate", "School", "College/University", "Club/Academy",
        "District", "State", "Zonal/Regional", "National", "International"
    ]
    return jsonify({'levels': levels})

@app.route('/api/export/csv', methods=['GET'])
def export_csv():
    """Export tournaments to CSV format"""
    tournaments = db.get_all_tournaments()
    
    # Ensure output directory exists
    os.makedirs('output', exist_ok=True)
    
    with open('output/tournaments.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'Tournament Name', 'Sport', 'Level', 'Start Date', 'End Date',
            'Tournament Official URL', 'Streaming Partners/Links',
            'Tournament Image', 'Summary of Tournament'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for tournament in tournaments:
            writer.writerow({
                'Tournament Name': tournament['name'],
                'Sport': tournament['sport'],
                'Level': tournament['level'],
                'Start Date': tournament['start_date'],
                'End Date': tournament['end_date'],
                'Tournament Official URL': tournament['official_url'],
                'Streaming Partners/Links': ', '.join(tournament['streaming_links']),
                'Tournament Image': tournament['image_url'],
                'Summary of Tournament': tournament['summary']
            })
    
    return jsonify({'status': 'success', 'message': 'CSV exported successfully'})

@app.route('/api/export/json', methods=['GET'])
def export_json():
    """Export tournaments to JSON format"""
    tournaments = db.get_all_tournaments()
    
    # Ensure output directory exists
    os.makedirs('output', exist_ok=True)
    
    # Format for required output structure
    formatted_tournaments = []
    for tournament in tournaments:
        formatted_tournaments.append({
            'Tournament Name': tournament['name'],
            'Sport': tournament['sport'],
            'Level': tournament['level'],
            'Start Date': tournament['start_date'],
            'End Date': tournament['end_date'],
            'Tournament Official URL': tournament['official_url'],
            'Streaming Partners/Links': tournament['streaming_links'],
            'Tournament Image': tournament['image_url'],
            'Summary of Tournament': tournament['summary']
        })
    
    with open('output/tournaments.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(formatted_tournaments, jsonfile, indent=2, ensure_ascii=False)
    
    return jsonify({'status': 'success', 'message': 'JSON exported successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)