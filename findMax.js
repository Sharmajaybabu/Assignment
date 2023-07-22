function findMax(numbers) {
	if (!Array.isArray(numbers) || numbers.length === 0) {
		return undefined;
	}

	let max = numbers[0];

	for (let i = 1; i < numbers.length; i++) {
		if (numbers[i] > max) {
			max = numbers[i];
		}
	}
	console.log(max);
	return max;
}

findMax([20, 5, 25, 9, 8, 1]);
