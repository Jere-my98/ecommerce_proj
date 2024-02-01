// script.js

// Wait for the DOM content to be fully loaded
document.addEventListener("DOMContentLoaded", function() {
    // Select the navigation bar element
    const navbar = document.querySelector(".navbar");

    // Add scroll event listener
    window.addEventListener("scroll", function() {
        // Check if the user has scrolled beyond a certain point
        if (window.scrollY > 50) {
            // Add a class to the navigation bar to apply styles
            navbar.classList.add("scrolled");
        } else {
            // Remove the class if the user scrolls back to the top
            navbar.classList.remove("scrolled");
        }
    });
});
