document.addEventListener('DOMContentLoaded', function() {
    const sideMenu = document.getElementById('side-menu');
    const menuToggle = document.getElementById('menu-toggle');

    menuToggle.addEventListener('click', function() {
        sideMenu.classList.toggle('open');
    });
});