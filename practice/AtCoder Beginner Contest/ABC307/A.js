// Weekly Records
function Main(input) {
    input = input.split("\n");
    let N = parseInt(input[0])
    let A = input[1].split(" ").map((str) => parseInt(str))
    let i = 0;
    let ans = 0;
    let resutls = [];
    A.forEach((element) => {
        ans += element
        i += 1
        if (i === 7) {
            i = 0
            resutls.push(ans)
            ans = 0
        }
    });
    console.log(resutls.join(" "));
}
Main(require("fs").readFileSync("/dev/stdin", "utf-8"))
