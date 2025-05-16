// main/static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    // Animate elements on scroll
    const animateElements = document.querySelectorAll('.animate-on-scroll');
    
    if (animateElements.length > 0) {
        // Add visible class to elements in viewport on page load
        checkVisibility();
        
        // Check visibility on scroll
        window.addEventListener('scroll', function() {
            checkVisibility();
        });
    }
    
    function checkVisibility() {
        animateElements.forEach(function(element) {
            if (isElementInViewport(element)) {
                element.classList.add('visible');
            }
        });
    }
    
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top <= (window.innerHeight || document.documentElement.clientHeight) * 0.8 &&
            rect.bottom >= 0
        );
    }
    
    // Active navigation link based on current page
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(function(link) {
        const linkPath = link.getAttribute('href');
        if (currentPath === linkPath || 
            (linkPath !== '/' && currentPath.startsWith(linkPath))) {
            link.classList.add('active');
        }
    });
    
    // Project filtering (for projects page)
    const filterBtns = document.querySelectorAll('.filter-btn');
    
    if (filterBtns.length > 0) {
        filterBtns.forEach(function(btn) {
            btn.addEventListener('click', function() {
                const filter = this.getAttribute('data-filter');
                
                // Remove active class from all buttons
                filterBtns.forEach(function(b) {
                    b.classList.remove('active');
                });
                
                // Add active class to clicked button
                this.classList.add('active');
                
                // Show/hide projects
                const projectItems = document.querySelectorAll('.project-item');
                
                projectItems.forEach(function(item) {
                    if (filter === 'all') {
                        item.style.display = 'block';
                    } else {
                        const categories = item.getAttribute('data-categories').toLowerCase();
                        if (categories.includes(filter)) {
                            item.style.display = 'block';
                        } else {
                            item.style.display = 'none';
                        }
                    }
                });
            });
        });
    }
    
    // Form validation for contact form
    const contactForm = document.querySelector('.contact-form form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            let isValid = true;
            
            // Simple validation example
            const name = document.getElementById('name');
            const email = document.getElementById('email');
            const message = document.getElementById('message');
            
            if (!name.value.trim()) {
                setInvalid(name, 'Please enter your name');
                isValid = false;
            } else {
                setValid(name);
            }
            
            if (!email.value.trim()) {
                setInvalid(email, 'Please enter your email');
                isValid = false;
            } else if (!isValidEmail(email.value)) {
                setInvalid(email, 'Please enter a valid email');
                isValid = false;
            } else {
                setValid(email);
            }
            
            if (!message.value.trim()) {
                setInvalid(message, 'Please enter your message');
                isValid = false;
            } else {
                setValid(message);
            }
            
            if (!isValid) {
                event.preventDefault();
            }
        });
    }
    
    function setInvalid(element, message) {
        element.classList.add('is-invalid');
        const feedback = document.createElement('div');
        feedback.className = 'invalid-feedback';
        feedback.textContent = message;
        
        // Remove existing feedback elements
        const existingFeedback = element.parentNode.querySelector('.invalid-feedback');
        if (existingFeedback) {
            existingFeedback.remove();
        }
        
        element.parentNode.appendChild(feedback);
    }
    
    function setValid(element) {
        element.classList.remove('is-invalid');
        element.classList.add('is-valid');
        const existingFeedback = element.parentNode.querySelector('.invalid-feedback');
        if (existingFeedback) {
            existingFeedback.remove();
        }
    }
    
    function isValidEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }
});