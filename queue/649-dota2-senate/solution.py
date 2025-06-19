import unittest


def get_winner_party(senate: str) -> str:
    radient_indexes = []
    dire_indexes = []
    n = len(senate)
    for i in range(n):
        if senate[i] == "R":
            radient_indexes.append(i)
        else:
            dire_indexes.append(i)
    while radient_indexes and dire_indexes:
        first_radient_index = radient_indexes.pop(0)
        first_dire_index = dire_indexes.pop(0)
        if first_radient_index < first_dire_index:  # REMEMBER: the smaller index wins
            # VERY IMPORTANT: the senator gets another turn ONLY AFTER all the rest senators make their move!
            # we add n to the senator's index (before readding it), so he moves AFTER anyone, who didn't have a turn yet
            # n.b. it can be any CONSTANT value bigger than n, but we use n to make sure it's not smaller
            radient_indexes.append(first_radient_index + n)
        else:
            dire_indexes.append(first_dire_index + n)
    return "Radiant" if radient_indexes else "Dire"


class TestGetWinnerParty(unittest.TestCase):
    def test_two_different_teams_members(self):
        self.assertEqual(get_winner_party(senate="RD"), "Radiant")

    def test_three_members(self):
        self.assertEqual(get_winner_party(senate="RDD"), "Dire")

    def test_one_member(self):
        self.assertEqual(get_winner_party(senate="R"), "Radiant")

    def test_two_same_team_members(self):
        self.assertEqual(get_winner_party(senate="RR"), "Radiant")

    def test_four_members_equal(self):
        self.assertEqual(get_winner_party(senate="RDDR"), "Radiant")


if __name__ == "__main__":
    unittest.main()
