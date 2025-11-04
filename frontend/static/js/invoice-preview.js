// Digital Khata - Invoice Preview JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Update preview when customer changes
    document.getElementById('customer')?.addEventListener('change', updatePreview);
    
    // Update preview when invoice date changes
    document.getElementById('invoice_date')?.addEventListener('change', updatePreview);
    
    // Update preview when due date changes
    document.getElementById('due_date')?.addEventListener('change', updatePreview);
    
    // Update preview when items change
    document.addEventListener('input', function(e) {
        if (e.target.classList.contains('item-quantity') || 
            e.target.classList.contains('item-price') || 
            e.target.classList.contains('item-name')) {
            updatePreview();
        }
    });
    
    // Initialize preview
    updatePreview();
});

function updatePreview() {
    // Update customer info
    const customerSelect = document.getElementById('customer');
    if (customerSelect) {
        const customerName = customerSelect.options[customerSelect.selectedIndex].text;
        document.querySelector('.invoice-preview-customer')?.forEach(el => {
            el.textContent = customerName;
        });
    }
    
    // Update dates
    const invoiceDate = document.getElementById('invoice_date')?.value;
    if (invoiceDate) {
        document.querySelector('.invoice-preview-date')?.forEach(el => {
            el.textContent = new Date(invoiceDate).toLocaleDateString();
        });
    }
    
    // Update due date
    const dueDate = document.getElementById('due_date')?.value;
    if (dueDate) {
        document.querySelector('.invoice-preview-due')?.forEach(el => {
            el.textContent = new Date(dueDate).toLocaleDateString();
        });
    }
    
    // Update items
    updatePreviewItems();
    
    // Update totals
    updatePreviewTotals();
}

function updatePreviewItems() {
    const container = document.getElementById('items-container');
    const previewContainer = document.querySelector('.invoice-preview-items');
    
    if (!container || !previewContainer) return;
    
    // Clear existing items
    previewContainer.innerHTML = '';
    
    // Add items to preview
    const rows = container.querySelectorAll('.item-row');
    rows.forEach(row => {
        const name = row.querySelector('[name="item_name[]"]')?.value || '';
        const quantity = row.querySelector('[name="item_quantity[]"]')?.value || '1';
        const price = row.querySelector('[name="item_price[]"]')?.value || '0';
        const total = (parseFloat(quantity) * parseFloat(price)).toFixed(2);
        
        if (name) {
            const itemElement = document.createElement('div');
            itemElement.className = 'flex justify-between mb-2';
            itemElement.innerHTML = `
                <span>${name} (x${quantity})</span>
                <span>₹${total}</span>
            `;
            previewContainer.appendChild(itemElement);
        }
    });
}

function updatePreviewTotals() {
    let subtotal = 0;
    const totals = document.querySelectorAll('.item-total');
    totals.forEach(total => {
        subtotal += parseFloat(total.value) || 0;
    });
    
    const tax = subtotal * 0.05;
    const discount = 0;
    const total = subtotal + tax - discount;
    
    // Update preview totals
    document.querySelector('.invoice-preview-subtotal')?.forEach(el => {
        el.textContent = '₹' + subtotal.toFixed(2);
    });
    
    document.querySelector('.invoice-preview-tax')?.forEach(el => {
        el.textContent = '₹' + tax.toFixed(2);
    });
    
    document.querySelector('.invoice-preview-total')?.forEach(el => {
        el.textContent = '₹' + total.toFixed(2);
    });
}

// Print invoice
function printInvoice() {
    window.print();
}

// Share via WhatsApp
function shareViaWhatsApp() {
    const message = "Please find the attached invoice.";
    const phone = "";
    const url = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
    window.open(url, '_blank');
}