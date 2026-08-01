const display = document.getElementById("display");
const history = document.getElementById("history");
const themeBtn = document.getElementById("themeBtn");

let darkMode = false;

// Add value
function appendValue(value) {
    display.value += value;
}

// Clear display
function clearDisplay() {
    display.value = "";
}

// Delete last character
function deleteLast() {
    display.value = display.value.slice(0, -1);
}

// Calculate
function calculate() {

    try {

        let expression = display.value;

        let result = eval(expression);

        history.innerText = expression + " =";

        display.value = result;

    }

    catch {

        display.value = "Error";

        setTimeout(() => {

            display.value = "";

        },1500);

    }

}

// Keyboard Support

document.addEventListener("keydown", function(event){

    const key = event.key;

    if(!isNaN(key) || "+-*/.%".includes(key)){

        appendValue(key);

    }

    else if(key==="Enter"){

        event.preventDefault();

        calculate();

    }

    else if(key==="Backspace"){

        deleteLast();

    }

    else if(key==="Escape"){

        clearDisplay();

    }

});

// Dark Mode

themeBtn.addEventListener("click",function(){

    darkMode=!darkMode;

    if(darkMode){

        document.body.style.background =
        "linear-gradient(135deg,#0f2027,#203a43,#2c5364)";

        themeBtn.innerHTML="☀️";

    }

    else{

        document.body.style.background =
        "linear-gradient(-45deg,#667eea,#764ba2,#6dd5ed,#2193b0)";

        themeBtn.innerHTML="🌙";

    }

});