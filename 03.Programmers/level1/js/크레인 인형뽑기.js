function solution(board, moves) {
	let boards = board;
	const n = board[0].length;
	const stack = [];
	let answer = 0;

	for (let i = 0; i < moves.length; i++) {
		let tmp = 0;
		for (let j = 0; j < n; j++) {
			if (boards[j][moves[i] - 1] !== 0) {
				tmp = boards[j][moves[i] - 1];
				boards[j][moves[i] - 1] = 0;
				break;
			}
		}

		if (tmp === 0) {
			continue;
		}

		if (stack.length === 0) {
			stack.push(tmp);
		} else {
			if (tmp === stack[stack.length - 1]) {
				answer += 2;
				stack.pop();
			} else {
				stack.push(tmp);
			}
		}
	}
	return answer;
}

console.log(
	solution(
		[
			[0, 0, 0, 0, 0],
			[0, 0, 1, 0, 3],
			[0, 2, 5, 0, 1],
			[4, 2, 4, 4, 2],
			[3, 5, 1, 3, 1],
		],
		[1, 5, 3, 5, 1, 2, 1, 4]
	)
);
