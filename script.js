document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch("/process_audio", {
        method: "POST",
        body: formData,
    });
    const data = await response.json();
    const output = document.getElementById("output");
    if (data.sign) {
        output.innerHTML = `<img src="${data.sign}" alt="Sign Language Translation">`;
    } else {
        output.innerHTML = `<p>${data.error}</p>`;
    }
});
