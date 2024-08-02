const $ = (selector) => document.querySelector(selector);

const adivinarNumeroForm = $('#adivinarNumeroForm');
const numeroInput = $('#numeroInput');

adivinarNumeroForm.addEventListener('submit', async event => {
	event.preventDefault();

	console.log(numeroInput.value);
	const formData = new FormData(adivinarNumeroForm);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    try {
    	
    	// const response = await fetch('https:/localhost/adivinar', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json',
        //     },
        //     body: JSON.stringify(data),
        // });

        // if (!response.ok) {
        //     throw new Error('Error en la solicitud: ' + response.statusText);
        // }

    	//const result = await response.json();
    	
    	//respuesta simulada
        const result = {
        	header: "hello world",
        	data: 1241441
        }
        console.log('Éxito:', result);

    } catch(e) {
    	console.error(e);
    }
})

console.log(numeroInput);