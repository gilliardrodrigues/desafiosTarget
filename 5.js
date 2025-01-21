/**
 * Função para inverter uma string.
 *
 * @param {string} inputString - A string que será invertida.
 * @returns {string} - A string invertida.
 */
function reverseString(inputString) {

	let reversedString = "";
	for (let i = inputString.length - 1; i >= 0; i--) 
      reversedString += inputString[i];

	return reversedString;
}

// Testando:
let inputString = "GILLIARD"; // Apenas de exemplo.
let reversedString = reverseString(inputString);
console.log(`Ao reverter a string '${inputString}', obtemos: '${reversedString}'`);
