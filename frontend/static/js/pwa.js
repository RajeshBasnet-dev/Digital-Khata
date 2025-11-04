// Digital Khata - PWA JavaScript File

// Register service worker
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/sw.js').then(function(registration) {
            console.log('ServiceWorker registration successful with scope: ', registration.scope);
        }, function(err) {
            console.log('ServiceWorker registration failed: ', err);
        });
    });
}

// Install PWA prompt
let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
    // Prevent Chrome 67 and earlier from automatically showing the prompt
    e.preventDefault();
    // Stash the event so it can be triggered later.
    deferredPrompt = e;
    // Show the install button
    showInstallPromotion();
});

function showInstallPromotion() {
    // Show the install promotion button
    const installBtn = document.getElementById('install-pwa');
    if (installBtn) {
        installBtn.classList.remove('hidden');
        installBtn.addEventListener('click', installPWA);
    }
}

function installPWA() {
    // Hide the install button
    const installBtn = document.getElementById('install-pwa');
    if (installBtn) {
        installBtn.classList.add('hidden');
    }
    
    // Show the prompt
    deferredPrompt.prompt();
    // Wait for the user to respond to the prompt
    deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
            console.log('User accepted the A2HS prompt');
        } else {
            console.log('User dismissed the A2HS prompt');
        }
        deferredPrompt = null;
    });
}

// Offline functionality
window.addEventListener('online', function() {
    showToast('You are now online', 'success');
});

window.addEventListener('offline', function() {
    showToast('You are offline. Changes will be synced when you\'re back online.', 'warning');
});

// IndexedDB for offline invoice creation
const DB_NAME = 'DigitalKhataDB';
const DB_VERSION = 1;
const INVOICES_STORE = 'invoices';

let db;

// Open database
function openDB() {
    return new Promise((resolve, reject) => {
        const request = indexedDB.open(DB_NAME, DB_VERSION);
        
        request.onerror = function(event) {
            console.error('Database error:', event.target.error);
            reject(event.target.error);
        };
        
        request.onsuccess = function(event) {
            db = event.target.result;
            resolve(db);
        };
        
        request.onupgradeneeded = function(event) {
            db = event.target.result;
            
            // Create invoices object store
            if (!db.objectStoreNames.contains(INVOICES_STORE)) {
                const objectStore = db.createObjectStore(INVOICES_STORE, { keyPath: 'id', autoIncrement: true });
                objectStore.createIndex('customer', 'customer', { unique: false });
                objectStore.createIndex('date', 'date', { unique: false });
                objectStore.createIndex('status', 'status', { unique: false });
            }
        };
    });
}

// Save invoice offline
function saveInvoiceOffline(invoice) {
    if (!db) {
        console.error('Database not initialized');
        return Promise.reject('Database not initialized');
    }
    
    return new Promise((resolve, reject) => {
        const transaction = db.transaction([INVOICES_STORE], 'readwrite');
        const objectStore = transaction.objectStore(INVOICES_STORE);
        const request = objectStore.add({
            ...invoice,
            date: new Date().toISOString(),
            status: 'pending'
        });
        
        request.onsuccess = function(event) {
            resolve(event.target.result);
        };
        
        request.onerror = function(event) {
            reject(event.target.error);
        };
    });
}

// Get all offline invoices
function getOfflineInvoices() {
    if (!db) {
        console.error('Database not initialized');
        return Promise.reject('Database not initialized');
    }
    
    return new Promise((resolve, reject) => {
        const transaction = db.transaction([INVOICES_STORE], 'readonly');
        const objectStore = transaction.objectStore(INVOICES_STORE);
        const request = objectStore.getAll();
        
        request.onsuccess = function(event) {
            resolve(event.target.result);
        };
        
        request.onerror = function(event) {
            reject(event.target.error);
        };
    });
}

// Delete offline invoice
function deleteOfflineInvoice(id) {
    if (!db) {
        console.error('Database not initialized');
        return Promise.reject('Database not initialized');
    }
    
    return new Promise((resolve, reject) => {
        const transaction = db.transaction([INVOICES_STORE], 'readwrite');
        const objectStore = transaction.objectStore(INVOICES_STORE);
        const request = objectStore.delete(id);
        
        request.onsuccess = function(event) {
            resolve();
        };
        
        request.onerror = function(event) {
            reject(event.target.error);
        };
    });
}

// Initialize database when page loads
document.addEventListener('DOMContentLoaded', function() {
    openDB().catch(error => {
        console.error('Failed to initialize database:', error);
    });
});

// Sync offline invoices when online
function syncOfflineInvoices() {
    if (!navigator.onLine) return;
    
    getOfflineInvoices().then(invoices => {
        if (invoices.length === 0) return;
        
        // In a real application, you would send these to your server
        console.log('Syncing offline invoices:', invoices);
        
        // For demonstration, we'll just show a toast
        if (invoices.length > 0) {
            showToast(`Synced ${invoices.length} offline invoices`, 'success');
            
            // Clear synced invoices
            invoices.forEach(invoice => {
                deleteOfflineInvoice(invoice.id);
            });
        }
    }).catch(error => {
        console.error('Failed to sync offline invoices:', error);
    });
}

// Check for sync when coming online
window.addEventListener('online', syncOfflineInvoices);

// Periodically check for sync
setInterval(syncOfflineInvoices, 30000); // Every 30 seconds