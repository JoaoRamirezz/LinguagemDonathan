async function main() {
	let funcs = [1];
	let ascss = [116, 101, 115, 116, 101, 32, 116, 0];
	let onde_esta = 0;

	const fs = require('fs');

	try {
		const data = await new Promise((resolve, reject) => {
			fs.readFile('execute.txt', 'utf-8', (err, data) => {
				if (err) reject(err);
				else resolve(data);
			});
		});

		const txtSplit = data.split(', \r\n');
		funcs = txtSplit[0].split(',');
		ascss = txtSplit[1].split(',');

		for (let indexFunc = 0; indexFunc < funcs.length; indexFunc++) {
			funcs[indexFunc] = parseInt(funcs[indexFunc]);
		}
		for (let indexAscss = 0; indexAscss < ascss.length; indexAscss++) {
			ascss[indexAscss] = parseInt(ascss[indexAscss]);
		}

		function allReplace(str, obj) {
			for (const x in obj) {
				str = str.replace(new RegExp(x, 'g'), obj[x]);
			}
			return str;
		}

		for (let i = 0; i < funcs.length; i++) {
			switch (funcs[i]) {
				case 1:
					var word = [];
					while (ascss[onde_esta] !== 0) {
						word.push(String.fromCharCode(ascss[onde_esta]))
						onde_esta += 1;
					}
					var wordString = word.join('');
					wordString = allReplace(wordString, { ',': '' });
					console.log(wordString);
					onde_esta += 1
					break;
				
				case 2:
					var word = [];
					while (ascss[onde_esta] !== 0) {
						word.push(String.fromCharCode(ascss[onde_esta]))
						onde_esta += 1;
					}
					for (let indexA = 0; indexA < word.length; indexA++) {
						if(word[indexA] == "<")
						{
							var op1 = word[indexA-2] + word[indexA-1]
							var op2 = word[indexA+1] + word[indexA+2]
							op1 = parseInt(op1)
							op2 = parseInt(op2)
							if(op1 < op2)
							{
								break;
							}
							else
							{
								onde_esta +=2
								i+=1
							}
						}
					}
					onde_esta += 1
					break;

				default:
					break;
			}
		}
	} catch (err) {
		console.error(err);
	}
}

main();