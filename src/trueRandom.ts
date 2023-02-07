import RandomMachine from "./generator";
import { MachineClass, MachineTheme } from "./names";
import r from "just-random";

const Themes : MachineTheme[] = ["FIRE", "FROST", "SHOCK", "EARTH", "ACID", "COMBAT"];
const Classes : MachineClass[] = ["FLYING", "WATER", "LAND"];

export default function TrueRandom () : string {

    const Theme = r(Themes)!;
    const Class = r(Classes)!;

    return RandomMachine(Theme, Class)
}