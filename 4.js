/**
 * Calcula o total de faturamento.
 * @param {Object} revenue - Objeto contendo os valores de faturamento por estado.
 * @returns {number} O total de faturamento.
 */
function calculateTotalRevenue(revenue) {
	return Object.values(revenue).reduce((total, value) => total + value, 0);
}

/**
 * Calcula o percentual de representação de cada estado.
 * @param {Object} revenue - Objeto contendo os valores de faturamento por estado.
 * @param {number} totalRevenue - O total de faturamento.
 * @returns {Array} Lista de objetos com o estado e seu percentual de representação.
 */
function calculateRevenuePercentage(revenue, totalRevenue) {
	return Object.entries(revenue).map(([state, value]) => {
		const percentage = (value / totalRevenue) * 100;
		return { state, percentage: percentage.toFixed(2) };
	});
}

/**
 * Exibe os percentuais de faturamento no console.
 * @param {Array} percentages - Lista de objetos contendo o estado e seu percentual de representação.
 */
function displayPercentages(percentages) {
	percentages.forEach(({ state, percentage }) => {
		console.log(`Estado: ${state}, Percentual: ${percentage}%`);
	});
}

// Dados de faturamento por estado
const revenue = {
	SP: 67836.43,
	RJ: 36678.66,
	MG: 29229.88,
	ES: 27165.48,
	Others: 19849.53,
};

// Testando:
const totalRevenue = calculateTotalRevenue(revenue);
const revenuePercentages = calculateRevenuePercentage(revenue, totalRevenue);
displayPercentages(revenuePercentages);
