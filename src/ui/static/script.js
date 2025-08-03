$(document).ready(function() {
    // Load initial data
    loadSports();
    loadLevels();
    loadTournaments();

    // Event handlers
    $('#filter-btn').click(function() {
        const sport = $('#sport-filter').val();
        const level = $('#level-filter').val();
        loadTournaments(sport, level);
    });

    $('#clear-filters').click(function() {
        $('#sport-filter').val('');
        $('#level-filter').val('');
        loadTournaments();
    });

    $('#export-csv').click(function() {
        exportData('csv');
    });

    $('#export-json').click(function() {
        exportData('json');
    });
});

function loadSports() {
    $.get('/api/sports', function(data) {
        const sportFilter = $('#sport-filter');
        data.sports.forEach(function(sport) {
            sportFilter.append(`<option value="${sport}">${sport}</option>`);
        });
    });
}

function loadLevels() {
    $.get('/api/levels', function(data) {
        const levelFilter = $('#level-filter');
        data.levels.forEach(function(level) {
            levelFilter.append(`<option value="${level}">${level}</option>`);
        });
    });
}

function loadTournaments(sport = '', level = '') {
    $('#loading').show();
    $('#tournament-grid').empty();

    let url = '/api/tournaments';
    const params = [];
    
    if (sport) params.push(`sport=${encodeURIComponent(sport)}`);
    if (level) params.push(`level=${encodeURIComponent(level)}`);
    
    if (params.length > 0) {
        url += '?' + params.join('&');
    }

    $.get(url, function(data) {
        $('#loading').hide();
        
        if (data.tournaments.length === 0) {
            $('#tournament-grid').html('<div class="no-tournaments">No tournaments found.</div>');
            return;
        }

        data.tournaments.forEach(function(tournament) {
            const tournamentCard = createTournamentCard(tournament);
            $('#tournament-grid').append(tournamentCard);
        });
    }).fail(function() {
        $('#loading').hide();
        $('#tournament-grid').html('<div class="no-tournaments">Error loading tournaments.</div>');
    });
}

function createTournamentCard(tournament) {
    const streamingLinks = tournament.streaming_links
        .map(link => `<a href="#" class="tournament-link">${link}</a>`)
        .join('');

    return `
        <div class="tournament-card">
            <div class="tournament-header">
                <div class="tournament-name">${tournament.name}</div>
                <div>
                    <span class="tournament-sport">${tournament.sport}</span>
                    <span class="tournament-level">${tournament.level}</span>
                </div>
            </div>
            
            <div class="tournament-dates">
                <div class="date-row">
                    <strong>Start Date:</strong>
                    <span>${formatDate(tournament.start_date)}</span>
                </div>
                <div class="date-row">
                    <strong>End Date:</strong>
                    <span>${formatDate(tournament.end_date)}</span>
                </div>
            </div>
            
            <div class="tournament-summary">
                ${tournament.summary || 'No description available.'}
            </div>
            
            <div class="tournament-links">
                ${tournament.official_url ? `<a href="${tournament.official_url}" class="tournament-link" target="_blank">Official Site</a>` : ''}
                ${streamingLinks}
            </div>
        </div>
    `;
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

function exportData(format) {
    $.get(`/api/export/${format}`, function(data) {
        alert(`${format.toUpperCase()} exported successfully!`);
    }).fail(function() {
        alert(`Error exporting ${format.toUpperCase()}`);
    });
}