document.addEventListener('DOMContentLoaded', function() {
    const allLinks = document.querySelectorAll('a.dock');
    const currentLink = document.querySelector('a.current');
    
    if (currentLink) {
        currentLink.classList.remove('current');
    }

    allLinks.forEach(link => {
        try {
            const url = new URL(link.href);
            
            // Более точное сравнение путей (учитывает trailing slash)
            if (url.pathname.replace(/\/$/, '') === window.location.pathname.replace(/\/$/, '')) {
                link.classList.add('current');
            }
        } catch (e) {
            // console.error('Invalid URL in link:', link.href, e);
        }
    });
});