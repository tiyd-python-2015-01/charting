from dice_simulation import *

sim = flip_simulation(10)
le_sim = int(len(sim))


def test_coin_flip():
    assert flipcoin() in ["H", "T"]


def test_flip_simulation():
    assert le_sim == 5


def test_minus():
    minuslist = head_minus_tail(sim)
    assert minuslist[0] == sim[0]['Heads'] - sim[0]['Tails']
    assert len(minuslist) == len(sim)


def test_ratios():
    ratiolist = ratios(sim)
    assert ratiolist[0] == (sim[0]['Heads']
                            / (sim[0]['Heads'] + sim[0]['Tails']))
    assert len(ratiolist) == le_sim


def test_run_trial():
    trials = run_trial(2, 10)
    assert len(trials) == 2
    assert len(trials[0]) == le_sim


def test_trial_ratios():
    trials = run_trial(2, 10)
    trial_ratios = trial_ratio(trials)
    assert len(trial_ratios[0]) == le_sim


def test_means():
    a = [[1, 2, 3, 4], [5, 6, 7, 6]]
    assert means(a) == [2.5, 6]


def test_st_dev():
    a = [[1, 2, 3, 4], [5, 6, 7, 6]]
    assert std_dev(a) == [1.2909944487358056, 0.816496580927726]
