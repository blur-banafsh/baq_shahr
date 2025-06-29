document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling for navigation links
    document.querySelectorAll('.smooth-scroll').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            const headerOffset = document.querySelector('.custom-navbar').offsetHeight; // Get dynamic header height
            const elementPosition = targetElement.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset - 20; // -20px for extra padding

            window.scrollTo({
                top: offsetPosition,
                behavior: "smooth"
            });

            // Close navbar on mobile after clicking a link
            const navbarCollapse = document.getElementById('navbarNav');
            const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
            if (bsCollapse) {
                bsCollapse.hide();
            }
        });
    });

    // Intersection Observer for fade-in animations on scroll
    const observerOptions = {
        root: null, // viewport
        rootMargin: '0px',
        threshold: 0.1 // 10% of element visible to trigger
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // For menu items (slide-in)
                if (entry.target.classList.contains('menu-item')) {
                    entry.target.classList.add('active');
                }
                // For section titles (fade-in-up)
                if (entry.target.classList.contains('fade-in-up')) {
                    entry.target.classList.add('active');
                }
                observer.unobserve(entry.target); // Stop observing once animated
            }
        });
    }, observerOptions);

    // Observe all menu items and section titles
    document.querySelectorAll('.menu-item').forEach(item => {
        observer.observe(item);
    });
    document.querySelectorAll('.section-title').forEach(title => {
        observer.observe(title);
    });

    // Optional: Add a class to navbar on scroll for a subtle change
    const navbar = document.querySelector('.custom-navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) { // After scrolling 50px
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
});