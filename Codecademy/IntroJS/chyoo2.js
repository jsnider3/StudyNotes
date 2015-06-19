
var user = prompt("You're a member of an Inquisitor's Retinue. You've been sneaking \
around the hive, but have spotted a secret Slaaneshi cult in the underhive. Do you \
RETREAT, FIGHT them, or WAIT for reinforcement?").toUpperCase()

function yesno (quest) {
    return prompt(quest).toUpperCase() == "YES"   
}

switch (user) {
    case "RETREAT":
        var mercy = yesno("Is your inquisitor a merciful man?")
        var charm = yesno("Are you at least moderately charming?")
        if (mercy && charm) {
            console.log("Yeah, no. You're dead.")
        } else {
            console.log("Well, you're shot for incompetence. No surprises, there.")
        }
        break;
    case "FIGHT":
        var gun = yesno("Do you have a gun?")
        var psyker = yesno("Do they have a psyker?")
        if (gun || !psyker) {
            console.log("You end up wiping them out with heavy casualties.")
        } else {
            console.log("After a merciless and brutal fight, your team is wiped out to a man")
        }
        break;
    case "WAIT":
        console.log("While you're waiting one of the guards spots you.");
        console.log("They ambush you from behind and then sacrifice you to a demon.");
        break;
    default:
        console.log("That's not a real choice. The Inquisition shoots you for incompetence.");
        break
    
}
