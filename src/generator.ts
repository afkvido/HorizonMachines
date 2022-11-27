import { acidNames, combatNames, earthNames, fireNames, flyingNames, frostNames, landNames, MachineClass, MachineTheme, shockNames, waterNames } from "./names";
import r from "just-random";

export default function RandomMachine (Theme : MachineTheme, Class : MachineClass) : string {

    let Output : string = "";


    switch (Theme) {
        case "ACID" : Output += r(acidNames); break;
        case "COMBAT": Output += r(combatNames); break;
        case "EARTH": Output += r(earthNames); break;
        case "FIRE": Output += r(fireNames); break;
        case "FROST": Output += r(frostNames); break;
        case "SHOCK": Output += r(shockNames); break;
        case null: console.log("This shouldn't be happening."); break;
        default: throw new Error("This shouldn't be happening.");
    }

    switch (Class) {
        case "FLYING": Output += r(flyingNames); break;
        case "LAND": Output += r(landNames); break;
        case "WATER": Output += r(waterNames); break;
        case null: console.log("This shouldn't be happening."); break;
        default: throw new Error("This shouldn't be happening.");
    }

    return Output;
}