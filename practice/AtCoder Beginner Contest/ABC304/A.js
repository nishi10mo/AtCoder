// First Player
function Main(input) {
    input = input.split("\n");
    let N = input[0];
    let SA = input.slice(1, N);
    console.log(SA);
}
Main(require("fs").readFileSync("/dev/stdin", "utf-8"))
