const loadBtn = document.getElementById("loadBtn");
const toggleBtn = document.getElementById("toggleBtn");
const results = document.getElementById("results");
const metrics = document.getElementById("metrics");
const errorList = document.getElementById("errorList");
let visible = true;

loadBtn.onclick = async () => {
  try {
    const response = await fetch("dashboard_data.json");
    const data = await response.json();
    metrics.innerHTML = `
      <p>Math Questions: ${data.question_counts.Math || 0}</p>
      <p>Coding Questions: ${data.question_counts.Coding || 0}</p>
      <p>Accuracy: ${data.accuracy ?? "N/A"}</p>
      <p>Precision: ${data.precision ?? "N/A"}</p>
      <p>Recall: ${data.recall ?? "N/A"}</p>
      <p>F1 Score: ${data.f1 ?? "N/A"}</p>
    `;
    errorList.innerHTML = `<h3>Error Analysis</h3>${data.errors.map(e => `<p>${e.question}<br>true: ${e.true}, pred: ${e.predicted}</p>`).join("")}`;
  } catch (error) {
    metrics.textContent = "Failed to load dashboard data.";
  }
};

toggleBtn.onclick = () => {
  visible = !visible;
  results.classList.toggle("hidden", !visible);
  toggleBtn.textContent = visible ? "Hide Results" : "Show Results";
};
