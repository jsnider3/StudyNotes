//Untested optimized version of the Rock Paper Scissors lesson.
var options = ['rock', 'paper', 'scissors']
var userChoice = prompt("Do you choose rock, paper or scissors?");
var computerChoice = options[Math.floor(Math.random() * 3)]
console.log("Computer: " + computerChoice);

function compare(choice1, choice2) {
  choice1 = Array.FindIndex(options, option => option == choice1);
  choice2 = Array.FindIndex(options, option => option == choice2);
  if (choice1 == choice2) 
  {
    return "The result is a tie!"
  }
  else if (choice2 - choice1 == 1 || choice2 - choice1 == -2) 
  {
    return options[choice2] + " wins"
  }
  else
  {
    return options[choice1] + " wins"
  }
}
compare(userChoice, computerChoice)
