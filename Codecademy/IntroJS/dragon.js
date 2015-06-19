var slaying = true
var youHit = Math.floor(Math.random() * 2) == 1
var damageThisRound = Math.floor(Math.random() * 5 + 1)
var totalDamage = 0
while(slaying)
{
    if (youHit)
    {
        console.log("You hit the dragon!")
        totalDamage += damageThisRound
        if(totalDamage >= 4) 
        {
            console.log("The dragon's dead!")
            slaying = false
        }
    }
    else
    {
        console.log("The dragon kills you.")
    }
    youHit = Math.floor(Math.random() * 2) == 1
}
