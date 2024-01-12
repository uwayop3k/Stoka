

let resultHTML = `
    <div class="results">
        <div class="product-out">
            Product:
        </div>
        <div class="branch-out">
            Branch:
        </div>
        <div class="total-purchase">
            Total purchase:
        </div>
        <div class="total-sale">
            Total sales:
        </div>
        <div class="actual-oosd">
            Actual OOSD:
        </div>
        <div class="average-oosd">
            Average OOSD:
        </div>
    </div>
`;
let resultsHTML = "";
for (let i = 0; i < 20; i++) {
    resultsHTML += resultHTML + "<br>";
  }
document.getElementById("outputs").innerHTML = resultsHTML;

