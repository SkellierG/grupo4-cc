// script.js

document.addEventListener("DOMContentLoaded", function() {
    const $ = selector => document.querySelector(selector);
    const earlybox = $('#earlybox')
    const startButton = document.getElementById("startButton");
    const restartButton = document.getElementById("restartButton");
    const guessButton = document.getElementById("guessButton");
    const guessInput = document.getElementById("guessInput");
    const attemptsRemaining = document.getElementById("attemptsRemaining");
    const attemptsCount = document.getElementById("attemptsCount");
    const result = document.getElementById("result");
    const resultMessage = document.getElementById("resultMessage");
    const gameStatus = document.getElementById("gameStatus");

    let attemptsLeft = 3;

    function startGame() {
        fetch("http://localhost:8000/check", {
            method: "POST"
        }).then(response => {
            if (response.ok) {
                gameStatus.style.display = "block";
                startButton.style.display = "none";
                restartButton.style.display = "none";
                result.style.display = "none";
                attemptsLeft = 3;
                attemptsCount.textContent = attemptsLeft;
            }
        });
    }

    function makeGuess() {
        const guess = parseInt(guessInput.value, 10);

        fetch(`http://localhost:8000/adivinar`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({numero: guess}),
        }).then(async response => {

            //console.log(await response.json())

            const responseParsed = await response.json();

            //console.log(responseParsed)

            attemptsCount.textContent = responseParsed.attempts;
            earlybox.textContent = responseParsed.feedback;
            resultMessage.textContent = responseParsed.feedback;

            if (responseParsed.numberfinded == true) {
                attemptsCount.textContent = responseParsed.attempts;
                earlybox.textContent = responseParsed.feedback;
                resultMessage.textContent = responseParsed.feedback;
                result.style.display = "block";
                gameStatus.style.display = "none";
                startButton.style.display = "none";
                restartButton.style.display = "block";
            }

            if (responseParsed.attempts <= 0 && responseParsed.numberfinded == false) {
                attemptsCount.textContent = responseParsed.attempts;
                resultMessage.textContent = responseParsed.feedback;
                result.style.display = "block";
                gameStatus.style.display = "none";
                startButton.style.display = "none";
                restartButton.style.display = "block";
            }


        }).catch(error => {
            console.error('Error:', error);
        });
            // .then(text => {
            //     if (text.includes("Fin del juego")) {
            //         resultMessage.textContent = text;
            //         result.style.display = "block";
            //         gameStatus.style.display = "none";
            //         startButton.style.display = "none";
            //         restartButton.style.display = "block";
            //     } else {
            //         attemptsLeft--;
            //         attemptsCount.textContent = attemptsLeft;
            //         if (attemptsLeft <= 0) {
            //             resultMessage.textContent = "Fin del juego! El número era: " + text.split("El número era: ")[1];
            //             result.style.display = "block";
            //             gameStatus.style.display = "none";
            //             startButton.style.display = "none";
            //             restartButton.style.display = "block";
            //         } else {
            //             // Actualizar mensaje con el texto proporcionado por el servidor
            //             resultMessage.textContent = text;
            //         }
            //     }
            //}
            //);
    }

    function restartGame() {
        fetch("http://localhost:8000/retry", {
            method: "POST"
        }).then(response => {
            if (response.ok) {
                gameStatus.style.display = "block";
                restartButton.style.display = "none";
                result.style.display = "none";
                attemptsLeft = 3;
                attemptsCount.textContent = attemptsLeft;
            }
        });
    }

    startButton.addEventListener("click", startGame);
    guessButton.addEventListener("click", ()=>{
        if (parseInt(guessInput.value, 10) >= 1 && parseInt(guessInput.value, 10) <= 50) {
            makeGuess()
        } else {
            earlybox.textContent = "El numero debe ser entre 1 y 50!";
        }
    });
    restartButton.addEventListener("click", restartGame);
});
