
const backendURL = "https://sturdy-system-pjjvpgjvgpgv3rr4v-5000.app.github.dev/predict";

// Show image preview
function previewImage() {
    const input = document.getElementById("imageInput");
    const preview = document.getElementById("previewImage");

    const file = input.files[0];
    if (!file) return;

    preview.src = URL.createObjectURL(file);
    preview.style.display = "block";
}

// Send image to backend
function predict() {
    const input = document.getElementById("imageInput");
    const file = input.files[0];

    if (!file) {
        alert("Please upload an image first");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    document.getElementById("result").innerHTML = "🔍 Predicting...";

    fetch(backendURL, {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerHTML = `
            <h3>Result</h3>
            <p><b>Disease:</b> ${data.prediction}</p>
            <p><b>Confidence:</b> ${data.confidence}%</p>
            <p><b>Remedy:</b> ${data.remedy}</p>
        `;
    })
    .catch(err => {
        console.error(err);
        document.getElementById("result").innerHTML =
            "<span style='color:red;'>Error connecting to server</span>";
    });
}