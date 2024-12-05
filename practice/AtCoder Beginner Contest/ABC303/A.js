// Similar String
function Main(input) {
    input = input.split("\n");
    N = parseInt(input[0]);
    S = input[1];
    T = input[2];
    for (i=0; i<N; i++) {
        if (S[i] === T[i]) {
            continue;
        } else if ((S[i] === "l" && T[i] === "1") || (S[i] === "1" && T[i] === "l")) {
            continue;
        } else if ((S[i] === "0" && T[i] === "o") || (S[i] === "o" && T[i] === "0")) {
            continue;
        } else {
            console.log("No");
            return;
        }
    }
    console.log("Yes");
}
Main(require("fs").readFileSync("/dev/stdin", "utf-8"))