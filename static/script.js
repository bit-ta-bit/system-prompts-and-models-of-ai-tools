document.addEventListener('DOMContentLoaded', () => {
    const feedContainer = document.getElementById('feed-container');

    fetch('/api/feed')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(entries => {
            if (entries.length === 0) {
                feedContainer.innerHTML = '<p>No feed entries found.</p>';
                return;
            }

            entries.forEach(entry => {
                const card = document.createElement('div');
                card.className = 'card';

                const source = document.createElement('p');
                source.className = 'source';
                source.textContent = entry.source;

                const title = document.createElement('h2');
                title.className = 'title';

                const link = document.createElement('a');
                link.href = entry.link;
                link.textContent = entry.title;
                link.target = '_blank'; // Open in new tab
                link.rel = 'noopener noreferrer';

                title.appendChild(link);

                const published = document.createElement('p');
                published.className = 'published';
                published.textContent = `Published: ${entry.published}`;

                card.appendChild(source);
                card.appendChild(title);
                card.appendChild(published);

                feedContainer.appendChild(card);
            });
        })
        .catch(error => {
            console.error('Error fetching feed:', error);
            feedContainer.innerHTML = `<p>Error loading feed. Please check the console for details.</p>`;
        });
});
