function check() {

    let password = document.getElementById("password").value

    fetch("http://127.0.0.1:5000/check", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({ password: password })

    })
        .then(res => res.json())
        .then(data => {

            document.getElementById("result").innerHTML =
                "Strength: " + data.strength

        })

}