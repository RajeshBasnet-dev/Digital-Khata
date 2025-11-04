// Digital Khata - Main JavaScript File

// Initialize tooltips
document.addEventListener('DOMContentLoaded', function() {
    // Toggle sidebar on mobile
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebar = document.getElementById('sidebar');
    const sidebarOverlay = document.getElementById('sidebar-overlay');
    
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('open');
            sidebarOverlay.classList.toggle('open');
        });
    }
    
    // Close sidebar when clicking overlay
    if (sidebarOverlay) {
        sidebarOverlay.addEventListener('click', function() {
            sidebar.classList.remove('open');
            sidebarOverlay.classList.remove('open');
        });
    }
    
    // Close sidebar when clicking nav links (mobile)
    const navLinks = document.querySelectorAll('.sidebar a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            sidebar.classList.remove('open');
            sidebarOverlay.classList.remove('open');
        });
    });
    
    // Toast notifications
    const toastTriggers = document.querySelectorAll('[data-toast]');
    toastTriggers.forEach(trigger => {
        trigger.addEventListener('click', function() {
            const message = this.getAttribute('data-toast');
            const type = this.getAttribute('data-toast-type') || 'info';
            showToast(message, type);
        });
    });
    
    // Form validation
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
    
    // Dark mode toggle
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function() {
            document.documentElement.classList.toggle('dark');
            // Save preference to localStorage
            if (document.documentElement.classList.contains('dark')) {
                localStorage.setItem('darkMode', 'enabled');
            } else {
                localStorage.setItem('darkMode', 'disabled');
            }
        });
    }
    
    // Check for saved dark mode preference
    if (localStorage.getItem('darkMode') === 'enabled') {
        document.documentElement.classList.add('dark');
    }
    
    // Mobile menu toggle
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!mobileMenuButton.contains(event.target) && !mobileMenu.contains(event.target)) {
                mobileMenu.classList.add('hidden');
            }
        });
    }
});

// Show toast notification
function showToast(message, type = 'info') {
    const toastContainer = document.getElementById('toast-container') || createToastContainer();
    
    const toast = document.createElement('div');
    toast.className = `toast toast-${type} show`;
    toast.innerHTML = `
        <div class="flex items-start">
            <div class="flex-shrink-0">
                ${type === 'success' ? '<i class="bi bi-check-circle-fill text-green-500"></i>' : 
                  type === 'danger' ? '<i class="bi bi-exclamation-circle-fill text-red-500"></i>' : 
                  type === 'warning' ? '<i class="bi bi-exclamation-triangle-fill text-yellow-500"></i>' : 
                  '<i class="bi bi-info-circle-fill text-blue-500"></i>'}
            </div>
            <div class="ml-3">
                <p class="text-sm font-medium">${message}</p>
            </div>
            <div class="ml-auto pl-3">
                <button type="button" class="text-slate-400 hover:text-slate-500">
                    <i class="bi bi-x-lg"></i>
                </button>
            </div>
        </div>
    `;
    
    toastContainer.appendChild(toast);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        toast.remove();
    }, 5000);
    
    // Close button
    toast.querySelector('button').addEventListener('click', () => {
        toast.remove();
    });
}

// Create toast container if it doesn't exist
function createToastContainer() {
    const container = document.createElement('div');
    container.id = 'toast-container';
    container.className = 'fixed top-4 right-4 z-50 space-y-2';
    document.body.appendChild(container);
    return container;
}

// Format currency
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(amount);
}

// Format number
function formatNumber(num) {
    return new Intl.NumberFormat('en-IN').format(num);
}

// Toggle password visibility
function togglePasswordVisibility(inputId, buttonId) {
    const passwordInput = document.getElementById(inputId);
    const toggleButton = document.getElementById(buttonId);
    const eyeIcon = toggleButton.querySelector('i');
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        eyeIcon.classList.remove('bi-eye');
        eyeIcon.classList.add('bi-eye-slash');
    } else {
        passwordInput.type = 'password';
        eyeIcon.classList.remove('bi-eye-slash');
        eyeIcon.classList.add('bi-eye');
    }
}

// Confirmation dialog
function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}

// Print invoice
function printInvoice(invoiceId) {
    // In a real application, this would open a print-friendly version
    alert(`Printing invoice ${invoiceId}. In a real application, this would open a print dialog.`);
}

// Share via WhatsApp
function shareViaWhatsApp(message, phone = '') {
    const url = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
    window.open(url, '_blank');
}

// Export to CSV
function exportToCSV(data, filename) {
    let csvContent = "data:text/csv;charset=utf-8,";
    
    // Add headers
    if (data.length > 0) {
        const headers = Object.keys(data[0]).join(",");
        csvContent += headers + "\r\n";
        
        // Add rows
        data.forEach(row => {
            const values = Object.values(row).join(",");
            csvContent += values + "\r\n";
        });
    }
    
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", filename);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Search functionality
function initSearch(searchInputId, tableBodyId) {
    const searchInput = document.getElementById(searchInputId);
    const tableBody = document.getElementById(tableBodyId);
    
    if (searchInput && tableBody) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const rows = tableBody.querySelectorAll('tr');
            
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                if (text.includes(searchTerm)) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });
    }
}

// Initialize search for all tables with search functionality
document.addEventListener('DOMContentLoaded', function() {
    const searchInputs = document.querySelectorAll('[data-search-target]');
    searchInputs.forEach(input => {
        const target = input.getAttribute('data-search-target');
        initSearch(input.id, target);
    });
});