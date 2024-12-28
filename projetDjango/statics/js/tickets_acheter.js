function decrementQuantity(i) {
    var currentValue = parseInt(i.value);
    if (currentValue > 1) {
        i.value = currentValue - 1;
    }
    updateTotal();
}

function incrementQuantity(i) {
    var currentValue = parseInt(i.value);
    i.value = currentValue + 1;
    updateTotal();
}

function updatePrice(i) {
    var row = i.parentNode.parentNode;
    var ticketType = i.value;
    var priceCell = row.querySelectorAll("td")[2];
    var quantityInput = row.querySelectorAll("td")[3].querySelector("input[type='text']");
    var quantity = parseInt(quantityInput.value);
    // var price = ticketType === "VIP" ? 200 : 120;

    var price = 120;
    if (ticketType === "VIP") price = 200;
    

    priceCell.textContent = price.toFixed(2) + " €";
    var rowTotal = quantity * price;
    row.querySelectorAll("td")[4].textContent = rowTotal.toFixed(2) + " €";
    updateTotal();
}


function updateTotal() {
    var total = 0;
    var rows = document.querySelectorAll("table tr");
    for (var i = 1; i < rows.length; i++) {
        var quantityInput = rows[i].querySelectorAll("td")[3].querySelector("input[type='text']");
        var quantity = parseInt(quantityInput.value);
        var price = parseFloat(rows[i].querySelectorAll("td")[2].textContent.replace(" €", "€"));
        var rowTotal = quantity * price;
        rows[i].querySelectorAll("td")[4].textContent = rowTotal.toFixed(2) + " €";
        total += rowTotal;
    }
}
