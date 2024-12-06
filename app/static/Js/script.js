// Function to switch between pages
function goToPage(pageId) {
    // Hide all pages
    const pages = document.querySelectorAll('.page');
    pages.forEach(page => {
        page.classList.add('hidden');
        page.classList.remove('active');
    });

    // Show the selected page
    const targetPage = document.getElementById(pageId);
    targetPage.classList.remove('hidden');
    targetPage.classList.add('active');
}

// Set default page to welcome page
document.getElementById('welcome-page').classList.add('active');
