// AJAX for updating resume without page reload
document.getElementById("update-btn").addEventListener("click", function () {
    fetch("/update", {
        method: "POST"
    })
        .then(response => response.text())
        .then(data => {
            document.body.innerHTML = data;
            console.log("Resume updated successfully!");
        })
        .catch(error => console.error("Error updating resume:", error));
});

// Search filter for repositories
document.getElementById("repo-search").addEventListener("keyup", function () {
    let value = this.value.toLowerCase();
    let repos = document.querySelectorAll("#repo-list .col");

    repos.forEach(repo => {
        if (repo.textContent.toLowerCase().includes(value)) {
            repo.style.display = "";
        } else {
            repo.style.display = "none";
        }
    });
});
