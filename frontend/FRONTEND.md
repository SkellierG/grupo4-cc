# Fetch
## /adivinar
POST
```javascript
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
```

```javascript
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
}
```

```javascript
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
```