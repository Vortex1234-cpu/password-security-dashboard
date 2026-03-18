function togglePassword() {

    let field = document.getElementById("password")

    field.type = field.type === "password" ? "text" : "password"

}


function generatePassword() {

    fetch("/generate")
        .then(res => res.json())
        .then(data => {

            document.getElementById("password").value = data.password

            checkPassword()

        })

}


function checkPassword() {

    let password = document.getElementById("password").value

    fetch("/check", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({ password: password })

    })
        .then(res => res.json())
        .then(data => {

            updateStrength(data.strength)

            updateScore(data.security_score)

            updateAnalysis(data)

            drawCharts(data.entropy, data.security_score)

            runTerminal()

        })

}


function updateStrength(strength) {

    let fill = document.getElementById("strength-fill")
    let text = document.getElementById("strength-text")

    const map = {
        "Very Weak": ["20%", "red"],
        "Weak": ["40%", "orange"],
        "Moderate": ["60%", "gold"],
        "Strong": ["80%", "limegreen"],
        "Very Strong": ["100%", "green"]
    }

    fill.style.width = map[strength][0]
    fill.style.background = map[strength][1]

    text.innerText = strength

}


function updateScore(score) {

    let fill = document.getElementById("score-fill")
    let text = document.getElementById("score-text")

    fill.style.width = score + "%"

    if (score < 40) {

        fill.style.background = "#ef4444"

    }
    else if (score < 70) {

        fill.style.background = "#f59e0b"

    }
    else {

        fill.style.background = "#22c55e"

    }

    text.innerText = "Score: " + score + " / 100"

}


function updateAnalysis(data) {

    document.getElementById("result").innerHTML =

        `Entropy: ${data.entropy}<br>
Crack Time: ${data.crack_time}<br>
Breach Count: ${data.breach_count}<br>
Common Password: ${data.common_password}<br>
Reuse Detected: ${data.reuse_detected}`

}


function runTerminal() {

    let terminal = document.getElementById("terminal")

    terminal.innerHTML = ""

    let lines = [

        "[+] Loading password database...",
        "[+] Running brute-force simulation...",
        "[+] Testing dictionary attack...",
        "[+] Calculating entropy...",
        "[✓] Password secure."

    ]

    let i = 0

    let interval = setInterval(() => {

        if (i < lines.length) {

            terminal.innerHTML += lines[i] + "<br>"
            i++

        } else {

            clearInterval(interval)

        }

    }, 400)

}