// Portfolio JavaScript Functions

// Smooth scrolling function
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Initialize page functionality when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize navigation
    initializeNavigation();
    
    // Initialize progress bars
    initializeProgressBars();
    
    // Initialize scroll animations
    initializeScrollAnimations();
    
    // Initialize mobile menu (if needed)
    initializeMobileMenu();
    
    // Initialize card animations
    initializeCardAnimations();
    
    // Add smooth scroll behavior to all anchor links
    initializeSmoothScroll();
});

// Navigation functionality
function initializeNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Get the target section from data attribute or onclick attribute
            const onclick = this.getAttribute('onclick');
            if (onclick) {
                // Extract section ID from onclick attribute
                const match = onclick.match(/getElementById\('([^']+)'\)/);
                if (match) {
                    const sectionId = match[1];
                    scrollToSection(sectionId);
                }
            }
        });
    });
    
    // Add active state to navigation based on scroll position
    window.addEventListener('scroll', updateActiveNavigation);
}

// Update active navigation based on scroll position
function updateActiveNavigation() {
    const sections = ['about', 'projects', 'experience', 'education', 'contact'];
    const navLinks = document.querySelectorAll('.nav-link');
    
    let currentSection = '';
    
    sections.forEach(sectionId => {
        const section = document.getElementById(sectionId);
        if (section) {
            const rect = section.getBoundingClientRect();
            if (rect.top <= 100 && rect.bottom >= 100) {
                currentSection = sectionId;
            }
        }
    });
    
    // Update active nav link
    navLinks.forEach(link => {
        link.classList.remove('active');
        const onclick = link.getAttribute('onclick');
        if (onclick && onclick.includes(currentSection)) {
            link.classList.add('active');
        }
    });
}

// Initialize progress bars with animation
function initializeProgressBars() {
    const progressBars = document.querySelectorAll('.progress-bar');
    
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const progressObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBar = entry.target;
                const width = progressBar.style.width;
                
                // Reset width and animate
                progressBar.style.width = '0%';
                setTimeout(() => {
                    progressBar.style.width = width;
                }, 100);
            }
        });
    }, observerOptions);
    
    progressBars.forEach(bar => {
        progressObserver.observe(bar);
    });
}

// Initialize scroll animations
function initializeScrollAnimations() {
    const animatedElements = document.querySelectorAll('.card, .education-card, .timeline-item');
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const animationObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    animatedElements.forEach(element => {
        // Set initial state
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        element.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        
        animationObserver.observe(element);
    });
}

// Initialize mobile menu functionality
function initializeMobileMenu() {
    // Create mobile menu button if it doesn't exist
    const navContainer = document.querySelector('.nav-container');
    if (navContainer && !document.querySelector('.mobile-menu-btn')) {
        const mobileMenuBtn = document.createElement('button');
        mobileMenuBtn.className = 'mobile-menu-btn';
        mobileMenuBtn.innerHTML = '☰';
        mobileMenuBtn.style.cssText = `
            display: none;
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: hsl(var(--foreground));
        `;
        
        // Add mobile menu functionality
        mobileMenuBtn.addEventListener('click', toggleMobileMenu);
        
        const navContent = document.querySelector('.nav-content');
        if (navContent) {
            navContent.appendChild(mobileMenuBtn);
        }
    }
    
    // Show mobile menu button on small screens
    updateMobileMenuVisibility();
    window.addEventListener('resize', updateMobileMenuVisibility);
}

// Toggle mobile menu
function toggleMobileMenu() {
    const navLinks = document.querySelector('.nav-links');
    if (navLinks) {
        navLinks.classList.toggle('mobile-active');
    }
}

// Update mobile menu visibility based on screen size
function updateMobileMenuVisibility() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    
    if (window.innerWidth <= 768) {
        if (mobileMenuBtn) mobileMenuBtn.style.display = 'block';
        if (navLinks) {
            navLinks.style.display = navLinks.classList.contains('mobile-active') ? 'flex' : 'none';
            navLinks.style.flexDirection = 'column';
            navLinks.style.position = 'absolute';
            navLinks.style.top = '100%';
            navLinks.style.left = '0';
            navLinks.style.right = '0';
            navLinks.style.background = 'hsl(var(--card))';
            navLinks.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
            navLinks.style.padding = '1rem';
        }
    } else {
        if (mobileMenuBtn) mobileMenuBtn.style.display = 'none';
        if (navLinks) {
            navLinks.style.display = 'flex';
            navLinks.style.flexDirection = 'row';
            navLinks.style.position = 'static';
            navLinks.style.background = 'none';
            navLinks.style.boxShadow = 'none';
            navLinks.style.padding = '0';
        }
    }
}

// Initialize card hover animations
function initializeCardAnimations() {
    const cards = document.querySelectorAll('.card, .education-card, .contact-card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-4px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
}

// Initialize smooth scroll for all internal links
function initializeSmoothScroll() {
    const buttons = document.querySelectorAll('.btn, [onclick*="scrollIntoView"]');
    
    buttons.forEach(button => {
        if (button.getAttribute('onclick')) {
            button.addEventListener('click', function(e) {
                const onclick = this.getAttribute('onclick');
                if (onclick.includes('scrollIntoView')) {
                    e.preventDefault();
                    const match = onclick.match(/getElementById\('([^']+)'\)/);
                    if (match) {
                        scrollToSection(match[1]);
                    }
                }
            });
        }
    });
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Add debounced scroll listener
window.addEventListener('scroll', debounce(updateActiveNavigation, 100));

// Handle external links
function handleExternalLinks() {
    const externalLinks = document.querySelectorAll('a[href^="http"], a[href^="mailto:"]');
    
    externalLinks.forEach(link => {
        if (link.href.startsWith('mailto:')) {
            return; // Skip mailto links
        }
        
        link.addEventListener('click', function(e) {
            // Add any analytics or tracking here if needed
            console.log('External link clicked:', this.href);
        });
    });
}

// Initialize external link handling
document.addEventListener('DOMContentLoaded', handleExternalLinks);

// Add CSS classes dynamically if needed
function addDynamicStyles() {
    const style = document.createElement('style');
    style.textContent = `
        .nav-link.active {
            color: hsl(var(--foreground)) !important;
            font-weight: 600;
        }
        
        .mobile-active {
            display: flex !important;
        }
        
        @media (max-width: 768px) {
            .nav-links {
                flex-direction: column !important;
                position: absolute !important;
                top: 100% !important;
                left: 0 !important;
                right: 0 !important;
                background: hsl(var(--card)) !important;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
                padding: 1rem !important;
                display: none !important;
            }
            
            .mobile-menu-btn {
                display: block !important;
            }
        }
    `;
    document.head.appendChild(style);
}

// Initialize dynamic styles
document.addEventListener('DOMContentLoaded', addDynamicStyles);

// Performance optimization: Lazy load images if any
function initializeLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Initialize lazy loading when DOM is ready
document.addEventListener('DOMContentLoaded', initializeLazyLoading);

// Export functions for global access
window.portfolioJS = {
    scrollToSection,
    initializeNavigation,
    initializeProgressBars,
    initializeScrollAnimations,
    toggleMobileMenu
};