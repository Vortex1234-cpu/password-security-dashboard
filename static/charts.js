let attackChart
let radarChart

function drawCharts(entropy, score) {

    if (attackChart) attackChart.destroy()

    attackChart = new Chart(

        document.getElementById("attackChart"),

        {
            type: "bar",

            data: {
                labels: ["Dictionary", "Brute Force", "GPU"],
                datasets: [{
                    label: "Attack Difficulty",
                    data: [entropy * 0.3, entropy * 0.8, entropy * 0.6],
                    backgroundColor: ["#ef4444", "#f59e0b", "#22c55e"]
                }]
            },

            options: {
                plugins: { legend: { display: false } }
            }

        })


    if (radarChart) radarChart.destroy()

    radarChart = new Chart(

        document.getElementById("radarChart"),

        {
            type: "radar",

            data: {
                labels: ["Entropy", "Security Score", "Attack Resistance"],

                datasets: [{

                    label: "Security",

                    data: [Math.min(entropy, 100), score, score],

                    backgroundColor: "rgba(34,197,94,0.2)",
                    borderColor: "#22c55e"

                }]
            }

        })

}