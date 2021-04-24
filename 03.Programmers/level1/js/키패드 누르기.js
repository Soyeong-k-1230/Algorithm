function solution(numbers, hand) {
	const position = {
		1: [0, 0],
		2: [0, 1],
		3: [0, 2],
		4: [1, 0],
		5: [1, 1],
		6: [1, 2],
		7: [2, 0],
		8: [2, 1],
		9: [2, 2],
		"*": [3, 0],
		0: [3, 1],
		"#": [3, 2],
	};
	const left = [1, 4, 7];
	const right = [3, 6, 9];
	let answer = "";
	let leftP = position["*"];
	let rightP = position["#"];

	for (let i = 0; i < numbers.length; i++) {
		let leftGap = 0;
		let rightGap = 0;
		if (left.includes(numbers[i])) {
			answer += "L";
			leftP = position[numbers[i]];
		} else if (right.includes(numbers[i])) {
			answer += "R";
			rightP = position[numbers[i]];
		} else {
			let tmp = position[numbers[i]];
			leftGap = Math.abs(leftP[0] - tmp[0]) + Math.abs(leftP[1] - tmp[1]);
			rightGap = Math.abs(rightP[0] - tmp[0]) + Math.abs(rightP[1] - tmp[1]);
			if (leftGap > rightGap) {
				answer += "R";
				rightP = position[numbers[i]];
			} else if (leftGap < rightGap) {
				answer += "L";
				leftP = position[numbers[i]];
			} else if (leftGap === rightGap) {
				if (hand === "left") {
					answer += "L";
					leftP = position[numbers[i]];
				} else {
					answer += "R";
					rightP = position[numbers[i]];
				}
			}
		}
	}
	return answer;
}

console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"));
