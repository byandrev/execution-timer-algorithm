const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function solve(a, b, rows) {
  for (let i = 0; i < a; i++) {
    let r = "";
    for (let j = 0; j < b; j++) {
      let number = rows[i][j];

      if (i % 2 == 0) number += 1;
      if (j % 2 == 0) number += 2;
      if (i % 2 != 0 && j % 2 != 0) number -= 3;

      if (j < b - 1) {
        r += number + " ";
      } else r += number;
    }

    console.log(r);
  }
}

let rows = [];
let i = 0;
let a = 0,
  b = 0;
rl.on("line", (line) => {
  if (i == 0) {
    [a, b] = line.split(" ").map((n) => parseInt(n));
  }

  if (i > 0 && i <= a) {
    const row = line.split(" ").map((n) => parseInt(n));
    rows.push(row);
  }

  if (i == a) {
    solve(a, b, rows);
    rl.close();
  }

  i++;
});

rl.on("close", () => {});
