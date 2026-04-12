async function getRecommendations() {
    const queryInput = document.getElementById('query');
    const query = queryInput.value.trim();
    const resultsDiv = document.getElementById('results');

    if (!query) {
        resultsDiv.innerHTML = '<div class="error-message">Please enter something to search for!</div>';
        return;
    }

    resultsDiv.innerHTML = '<div class="loading-message">Searching for the perfect quotes</div>';

    try {
        const response = await fetch('http://localhost:8000/recommend?query=' + encodeURIComponent(query) + '&top_k=5');
        
        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();

        if (!data.results || data.results.length === 0) {
            resultsDiv.innerHTML = '<div class="empty-message">No quotes found for that search. Try something different!</div>';
            return;
        }

        let html = '';
        data.results.forEach((item, index) => {
            const tagsHtml = item.tags 
                ? item.tags.split(',').map(tag => 
                    `<span class="tag">${tag.trim()}</span>`
                  ).join('')
                : '';

            html += `
                <div class="quote-card">
                    <p class="quote-text">"${escapeHtml(item.quote || 'No quote available')}"</p>
                    <div class="quote-meta">
                        <span class="author">— ${escapeHtml(item.author)}</span>
                        <span class="similarity-badge">Match: ${Math.round(item.similarity * 100)}%</span>
                    </div>
                    ${tagsHtml ? `<div class="tags">${tagsHtml}</div>` : ''}
                </div>
            `;
        });

        resultsDiv.innerHTML = html;
    } catch (error) {
        console.error('Error:', error);
        resultsDiv.innerHTML = `<div class="error-message">⚠️ Error connecting to server: ${error.message}</div>`;
    }
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Allow pressing Enter to search
document.getElementById('query').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        getRecommendations();
    }
});

// Clear results on input change for better UX
document.getElementById('query').addEventListener('input', function() {
    if (this.value.trim() === '') {
        document.getElementById('results').innerHTML = '';
    }
});

// Click on hint items to search
document.querySelectorAll('.hint-item').forEach(hint => {
    hint.addEventListener('click', function() {
        const text = this.textContent.replace(/^[^:]+:\s*/, '').trim();
        document.getElementById('query').value = text;
        getRecommendations();
    });
});