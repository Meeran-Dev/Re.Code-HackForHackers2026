let buggyCodeText = "";

document.getElementById("generateBtn").addEventListener("click", async () => {
    const language = document.getElementById("language").value;
    const difficulty = document.getElementById("difficulty").value;

    document.getElementById("buggyCode").textContent = "Generating...";
    document.getElementById("feedback").textContent = "";

    const res = await fetch("/generate-bug", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ language, difficulty })
    });

    const data = await res.json();
    buggyCodeText = data.buggy_code;
    document.getElementById("buggyCode").textContent = buggyCodeText;
});

document.getElementById("submitFix").addEventListener("click", async () => {
    const userCode = document.getElementById("userCode").value;

    if (!userCode.trim()) {
        alert("Please enter your fixed code.");
        return;
    }

    document.getElementById("feedback").textContent = "Evaluating...";

    const res = await fetch("/evaluate-fix", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            buggy_code: buggyCodeText,
            user_code: userCode
        })
    });

    const data = await res.json();
    document.getElementById("feedback").textContent = data.feedback;
});
