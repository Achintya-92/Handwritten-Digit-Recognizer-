const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const imageData = canvas.toDataURL("image/png");

console.log(imageData);

let drawing = false;

// Canvas background = black
ctx.fillStyle = "black";
ctx.fillRect(0, 0, canvas.width, canvas.height);

// Drawing settings
ctx.strokeStyle = "white";
ctx.lineWidth = 20;
ctx.lineCap = "round";

// Mouse pressed
canvas.addEventListener("mousedown", (event) => {
    drawing = true;

    ctx.beginPath();
    ctx.moveTo(event.offsetX, event.offsetY);
});

// Mouse moved
canvas.addEventListener("mousemove", (event) => {

    if (!drawing) return;

    ctx.lineTo(event.offsetX, event.offsetY);
    ctx.stroke();
});

// Mouse released
canvas.addEventListener("mouseup", () => {
    drawing = false;
});

// Mouse leaves canvas
canvas.addEventListener("mouseleave", () => {
    drawing = false;
});


// Clear button
document.getElementById("clear").addEventListener("click", () => {

    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    document.getElementById("result").textContent =
        "--";
    document.getElementById("confidence").textContent =
        "--";
});


document.getElementById("predict").addEventListener("click", async (e) => {
    e.preventDefault();
    const imageData = canvas.toDataURL("image/png");

    try {
        const response = await fetch(
            "http://127.0.0.1:5000/api/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    image: imageData
                })
            }
        );

    const data = await response.json();

    document.getElementById("result").innerText = data.predicted_digit;
    document.getElementById("confidence").innerText = data.confidence;

    } catch (error) {
        console.error("API Error:", error);
    }
});