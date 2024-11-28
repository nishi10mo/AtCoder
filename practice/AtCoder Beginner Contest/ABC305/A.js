// Water Station
function Main(input) {
    input = parseInt(input.replace("\n", ""));
    quotient = Math.floor(input/5);
    remainder = input%5;
    if (remainder === 0 || remainder === 1 || remainder ===2) {
        ans = 5*quotient;
    } else {
        ans = 5*(quotient + 1);
    }
    console.log(ans);
}
Main(require("fs").readFileSync("/dev/stdin", "utf-8"))
