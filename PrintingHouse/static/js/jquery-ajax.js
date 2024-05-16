document.addEventListener("DOMContentLoaded", function() {
    const quantityElement = document.getElementById("quantity");
    const incrementButton = document.getElementById("increment");
    const decrementButton = document.getElementById("decrement");

    function updateQuantity(operation) {
        fetch('{% url "cart_change" cart.id %}?operation=' + operation)
            .then(response => response.json())
            .then(data => {
                quantityElement.textContent = data.quantity;
            })
            .catch(error => console.error('Error:', error));
    }

    incrementButton.addEventListener("click", function() {
        updateQuantity('increment');
    });

    decrementButton.addEventListener("click", function() {
        updateQuantity('decrement');
    });
});
