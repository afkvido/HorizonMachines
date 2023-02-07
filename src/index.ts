import TrueRandom from "./trueRandom";

const times : number = parseInt(process.argv[2] ?? "1");


for (let i = 0; i <= times; i++) {
    console.log(TrueRandom())
}

