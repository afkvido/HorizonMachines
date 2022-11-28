import RandomMachine from "./generator";
import r from "just-random";
import { MachineTheme, MachineClass } from "./names";

export default function CompletleyRandomMachine () : string {

    const Theme : MachineTheme = r(["FIRE", "FROST", "SHOCK", "EARTH", "ACID", "COMBAT"]);
    const Class : MachineClass = r(["FLYING", "WATER", "LAND"]);

    return RandomMachine(Theme, Class);
}