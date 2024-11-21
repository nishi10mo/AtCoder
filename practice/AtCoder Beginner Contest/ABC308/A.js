// New Scheme
function Main(input) {
    input = input.replace(/\n/, "");
    input_obj = input.split(" ");
    for (let i=0; i < 7; i++) {
        if ((input_obj[i] > input_obj[i+1]) || (input_obj[i] < 100) || (input_obj[i] > 675) || (input_obj[i]%25 !== 0)) {
            console.log("No");
            return
        }
    }
    if ((input_obj[7] < 100) || (input_obj[7] > 675) || (input_obj[7]%25 !== 0)) {
        console.log("No");
        return
    }
    console.log("Yes");
}
Main(require("fs").readFileSync("/dev/stdin", "utf-8"))
