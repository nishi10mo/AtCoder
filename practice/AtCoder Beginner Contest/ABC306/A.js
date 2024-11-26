// Echo
function Main(input) {
    input = input.split("\n");
    let N = input[0]
    let S = input[1].split("")
    let results = []
    S.forEach((s) => {
        for (i=0; i<2; i++) {
            results.push(s)
        }
    })
    let ans = results.join("")
    console.log(ans)
}
Main(require("fs").readFileSync("/dev/stdin", "utf-8"))
