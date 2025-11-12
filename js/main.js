// ========================================
// Mobile Menu Toggle
// ========================================

const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const navMenu = document.querySelector('.nav-menu');

if (mobileMenuToggle) {
  mobileMenuToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    mobileMenuToggle.classList.toggle('active');
  });

  // Close menu when clicking on a nav link
  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      navMenu.classList.remove('active');
      mobileMenuToggle.classList.remove('active');
    });
  });

  // Close menu when clicking outside
  document.addEventListener('click', (e) => {
    if (!navMenu.contains(e.target) && !mobileMenuToggle.contains(e.target)) {
      navMenu.classList.remove('active');
      mobileMenuToggle.classList.remove('active');
    }
  });
}

// ========================================
// Header Scroll Effect
// ========================================

const header = document.getElementById('header');

window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    header.classList.add('scrolled');
  } else {
    header.classList.remove('scrolled');
  }
});

// ========================================
// Smooth Scroll for Anchor Links
// ========================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const href = this.getAttribute('href');

    // Skip if it's just "#" or empty
    if (href === '#' || href === '') {
      e.preventDefault();
      return;
    }

    const target = document.querySelector(href);

    if (target) {
      e.preventDefault();
      const headerOffset = 80;
      const elementPosition = target.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    }
  });
});

// ========================================
// Scroll Animations (Intersection Observer)
// ========================================

const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
    }
  });
}, observerOptions);

// Observe all elements with animate-on-scroll class
const animatedElements = document.querySelectorAll('.animate-on-scroll');
animatedElements.forEach(el => observer.observe(el));

// ========================================
// Back to Top Button
// ========================================

const backToTopButton = document.getElementById('backToTop');

if (backToTopButton) {
  window.addEventListener('scroll', () => {
    if (window.scrollY > 500) {
      backToTopButton.classList.add('show');
    } else {
      backToTopButton.classList.remove('show');
    }
  });

  backToTopButton.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

// ========================================
// Newsletter Form Handler
// ========================================

const newsletterForms = document.querySelectorAll('.newsletter-form');

newsletterForms.forEach(form => {
  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const emailInput = form.querySelector('.newsletter-input');
    const email = emailInput.value.trim();

    if (email && validateEmail(email)) {
      // Store email in localStorage for now (replace with actual backend later)
      const subscribers = JSON.parse(localStorage.getItem('newsletter_subscribers') || '[]');

      if (!subscribers.includes(email)) {
        subscribers.push(email);
        localStorage.setItem('newsletter_subscribers', JSON.stringify(subscribers));

        // Show success message
        showNotification('Success! You\'ll be notified when we publish new content.', 'success');
        emailInput.value = '';
      } else {
        showNotification('This email is already subscribed!', 'info');
      }
    } else {
      showNotification('Please enter a valid email address.', 'error');
    }
  });
});

// Email validation helper
function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

// ========================================
// Notification System
// ========================================

function showNotification(message, type = 'info') {
  // Remove existing notification if any
  const existingNotification = document.querySelector('.notification');
  if (existingNotification) {
    existingNotification.remove();
  }

  // Create notification element
  const notification = document.createElement('div');
  notification.className = `notification notification-${type}`;
  notification.textContent = message;

  // Add styles
  Object.assign(notification.style, {
    position: 'fixed',
    top: '20px',
    right: '20px',
    padding: '1rem 1.5rem',
    borderRadius: '0.5rem',
    color: 'white',
    fontWeight: '600',
    boxShadow: '0 10px 15px rgba(0, 0, 0, 0.1)',
    zIndex: '9999',
    animation: 'slideInRight 0.3s ease',
    maxWidth: '400px'
  });

  // Set background color based on type
  const colors = {
    success: '#10b981',
    error: '#ef4444',
    info: '#2563eb',
    warning: '#f59e0b'
  };
  notification.style.backgroundColor = colors[type] || colors.info;

  // Add animation keyframes if not already added
  if (!document.querySelector('#notification-animations')) {
    const style = document.createElement('style');
    style.id = 'notification-animations';
    style.textContent = `
      @keyframes slideInRight {
        from {
          transform: translateX(100%);
          opacity: 0;
        }
        to {
          transform: translateX(0);
          opacity: 1;
        }
      }
      @keyframes slideOutRight {
        from {
          transform: translateX(0);
          opacity: 1;
        }
        to {
          transform: translateX(100%);
          opacity: 0;
        }
      }
    `;
    document.head.appendChild(style);
  }

  // Add to DOM
  document.body.appendChild(notification);

  // Auto remove after 5 seconds
  setTimeout(() => {
    notification.style.animation = 'slideOutRight 0.3s ease';
    setTimeout(() => {
      notification.remove();
    }, 300);
  }, 5000);
}

// ========================================
// Affiliate Link Tracking (Optional)
// ========================================

// Track clicks on affiliate links
document.addEventListener('click', (e) => {
  const link = e.target.closest('a[data-affiliate="true"]');

  if (link) {
    const productName = link.getAttribute('data-product-name') || 'Unknown Product';
    const href = link.getAttribute('href');

    // Log to console (replace with analytics service later)
    console.log('Affiliate link clicked:', {
      product: productName,
      url: href,
      timestamp: new Date().toISOString()
    });

    // Store in localStorage for now (replace with analytics API later)
    const clicks = JSON.parse(localStorage.getItem('affiliate_clicks') || '[]');
    clicks.push({
      product: productName,
      url: href,
      timestamp: new Date().toISOString()
    });
    localStorage.setItem('affiliate_clicks', JSON.stringify(clicks));
  }
});

// ========================================
// Active Nav Link Highlighting
// ========================================

function updateActiveNavLink() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  let currentSection = '';

  sections.forEach(section => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;

    if (window.scrollY >= sectionTop - 100) {
      currentSection = section.getAttribute('id');
    }
  });

  navLinks.forEach(link => {
    link.classList.remove('active');
    const href = link.getAttribute('href');

    if (href === `#${currentSection}`) {
      link.classList.add('active');
    } else if (href === 'index.html' && window.scrollY < 100) {
      link.classList.add('active');
    }
  });
}

window.addEventListener('scroll', updateActiveNavLink);
window.addEventListener('load', updateActiveNavLink);

// ========================================
// Parallax Effect for Hero Background
// ========================================

const heroBackground = document.querySelector('.hero-background');

if (heroBackground) {
  window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    const parallaxSpeed = 0.5;

    if (scrolled < window.innerHeight) {
      heroBackground.style.transform = `translateY(${scrolled * parallaxSpeed}px)`;
    }
  });
}

// ========================================
// Loading Animation (Remove after page load)
// ========================================

window.addEventListener('load', () => {
  document.body.classList.add('loaded');
});

// ========================================
// Prevent Flash of Unstyled Content
// ========================================

document.documentElement.style.visibility = 'visible';

// ========================================
// Console Message
// ========================================

console.log('%c🏢 TerraLogic Tech', 'font-size: 24px; font-weight: bold; color: #2563eb;');
console.log('%cWebsite loaded successfully!', 'font-size: 14px; color: #64748b;');
console.log('%cBuilt with modern web technologies', 'font-size: 12px; color: #94a3b8;');

// ========================================
// Performance Monitoring (Optional)
// ========================================

if ('performance' in window) {
  window.addEventListener('load', () => {
    setTimeout(() => {
      const perfData = window.performance.timing;
      const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;

      console.log(`⚡ Page loaded in ${pageLoadTime}ms`);
    }, 0);
  });
}

// ========================================
// Utility Functions
// ========================================

// Debounce function for performance optimization
function debounce(func, wait = 20, immediate = true) {
  let timeout;
  return function() {
    const context = this;
    const args = arguments;
    const later = function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    const callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
}

// Throttle function for scroll events
function throttle(func, limit) {
  let inThrottle;
  return function() {
    const args = arguments;
    const context = this;
    if (!inThrottle) {
      func.apply(context, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// Apply throttle to scroll-heavy functions for better performance
window.addEventListener('scroll', throttle(() => {
  // Scroll-dependent code here runs at most every 100ms
}, 100));
