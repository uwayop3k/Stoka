document.addEventListener("DOMContentLoaded", function () {
    fetch('/outputs') // Fetch report data from Flask app
        .then(response => response.json())
        .then(data => {
            let resultsHTML = "";
            // Loop through report data and generate HTML for each item
            data.forEach(item => {
                resultsHTML += `
                    <div class="results">
                        <div class="product-out">
                            Product: ${item.itemCode}
                        </div>
                        <div class="branch-out">
                            Branch: ${item.branch}
                        </div>
                        <div class="range">
                            Range: ${item.itemData.range}
                        </div>
                        <div class="total-purchase">
                            Total purchase: ${item.itemData.total_purchases}
                        </div>
                        <div class="total-sale">
                            Total sales: ${item.itemData.total_sales}
                        </div>
                        <div class="actual-oosd">
                            Out of stock days: ${item.itemData.actual_oosd}
                        </div>
                    </div><br>`;
            });
            document.getElementById("outputs").innerHTML = resultsHTML; // Display the generated HTML
        })
        .catch(error => console.error('Error:', error));
});
