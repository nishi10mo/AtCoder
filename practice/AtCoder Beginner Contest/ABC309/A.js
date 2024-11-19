// Nine
function Main(input) {
    input = input.replace(/\n/, "")
    input_obj = input.split(" ")
    let a = parseInt(input_obj[0])
    let b = parseInt(input_obj[1])
    if ((a%3 === 1 && b === a + 1) || (a%3 === 2 && b === a - 1) || (a%3 === 2 && b === a + 1) || (a%3 === 0 && b === a - 1)) {
        console.log("Yes")
    } else {
        console.log("No")
    }
}
Main(require("fs").readFileSync("/dev/stdin", "utf8"));
