// script.js
const display = document.querySelector(".display");
const buttons = document.querySelectorAll("button");

let currentInput = "";
let currentOperator = "";
let shouldClearDisplay = true;

buttons.forEach((button) => {
    button.addEventListener("click", () => {
        const buttonText = button.textContent;

        if (buttonText.match(/[0-9]/)) {
            if (shouldClearDisplay) {
                display.textContent = "";
                shouldClearDisplay = false;
            }
            display.textContent += buttonText;
        } else if (buttonText === "AC") {
            display.textContent = "0";
            currentInput = "";
            currentOperator = "";
            shouldClearDisplay = true;
        } else if (buttonText === "DEL") {
                display.textContent = "0";
        } else if (buttonText === "=") {
            if (currentOperator && currentInput) {
                const result = calculate(parseFloat(currentInput), currentOperator, parseFloat(display.textContent));
                display.textContent = result;
                currentInput = result;
                currentOperator = "";
                shouldClearDisplay = true;
            }
        } else {
            currentOperator = buttonText;
            currentInput = display.textContent;
            shouldClearDisplay = true;
        }
    });
});

function borrar() {
    let texto = display.textContent;
    
}

function calculate(num1, operator, num2) {
    switch (operator) {
        case "+":
            return num1 + num2;
        case "-":
            return num1 - num2;
        case "*":
            return num1 * num2;
        case "/":
            if (num2 !== 0) {
                return num1 / num2;
            } else {
                return "Error";
            }
        case "^":
            return Math.pow(num1, num2);
        case "√":
            return num1 >= 0 ? Math.sqrt(num1) : "Error";
        
        default:
            return num2;
    }
}