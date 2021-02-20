//Notes {[key]:value}
//const something = ok == yeah? alright:nope
// something = alright if ok is equal to yeah else nope
// need brakcets for following -> const [firsValue, secondValue] = [one, two]
// if (!(isTrue == yeah)){}; if statement not true do something else nothing

function tournamentWinner(competitions, results){
  const homeTeam = 1;
  let champion = "placeholder";
  const scores = {[champion]:0};

  for (let idx = 0; idx<competitions.length;idx++){
    const result = results[idx];
    const [home,away] = competitions[idx];

    const winner = result === homeTeam? home:away;
    updateStats(winner, scores);

    if (scores[winner] > scores[champion]){
      champion = winner;
    }
  }
  return champion;
};

function updateStats(team, scores){
  if (!(team in scores)) {scores[team] = 0};
  scores[team] +=3;
}
