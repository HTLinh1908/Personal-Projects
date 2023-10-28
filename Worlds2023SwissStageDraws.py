"As League of Legends Worlds 2023 is happening, and Swiss stage matches are drawn, I wanted to see all the possible matches that could happen"
from itertools import permutation

class Team:
  def __innit__(self, name, region, pool):
    self.name = name
    self.region = region
    self.pool = pool

  def __repr__(self):
    return self.name


teams = [Team( "GenG", "LCK", 1), Team("NRG", "LCS", 1), Team("JDG","LPL", 1), Team("G2", "LEC", 1), Team("GAM", "VCS", 4), Team("BDS", "LEC", 4), Team("DK", "LCK", 4), Team("WBG", "LPL", 4), Team("BLG", "LPL", 2), Team("KT", "LCK", 3), Team("LNG", "LPL", 3), Team("FNC", "LEC", 2), Team("C9", "LCS", 2), Team("MAD", "LEC", 3), Team("T1", "LCK", 2), Team("TL", "LCS", 3)]



pool1 = [team for team in teams if team.pool == 1]
pool4 = [team for team in teams if team.pool == 4]

all_matches = []

for perm in permutation(pool4):
  matches = [(team1,team4} for team1, team4 in zip(pool1,perm) if team1.region != team4.region
  if len(matches) == len(pool1):
    all_matches.append(matches)

for i, matches in enumerate(all_matches, start=1):
  print(f"Case {i}:"
  for match in matches:
    print(f"{match[0]} vs {match[1]}")
  print()

print(f"Total number of cases: {len(all_mathces)}")
