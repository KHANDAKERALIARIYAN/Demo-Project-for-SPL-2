// Auto-hide alerts after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            alert.classList.remove('show');
            setTimeout(function() {
                alert.remove();
            }, 150);
        }, 5000);
    });
});

// Confirm delete actions
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-confirm');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });
});

// Dynamic form handling
document.addEventListener('DOMContentLoaded', function() {
    const addItemButtons = document.querySelectorAll('.add-item');
    addItemButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const formset = this.closest('.formset');
            const totalForms = formset.querySelector('#id_form-TOTAL_FORMS');
            const formCount = parseInt(totalForms.value);
            const emptyForm = formset.querySelector('.empty-form').cloneNode(true);
            
            // Update form index
            emptyForm.innerHTML = emptyForm.innerHTML.replace(/__prefix__/g, formCount);
            formset.querySelector('.forms').appendChild(emptyForm);
            totalForms.value = formCount + 1;
        });
    });
});

// Price calculation
document.addEventListener('DOMContentLoaded', function() {
    const quantityInputs = document.querySelectorAll('.quantity-input');
    const priceInputs = document.querySelectorAll('.price-input');
    
    function calculateTotal() {
        let total = 0;
        quantityInputs.forEach(function(input, index) {
            const quantity = parseFloat(input.value) || 0;
            const price = parseFloat(priceInputs[index].value) || 0;
            total += quantity * price;
        });
        document.getElementById('total-amount').value = total.toFixed(2);
    }
    
    quantityInputs.forEach(function(input) {
        input.addEventListener('input', calculateTotal);
    });
    
    priceInputs.forEach(function(input) {
        input.addEventListener('input', calculateTotal);
    });
}); 