#!/usr/bin/env python

# https://www.reddit.com/r/GAMETHEORY/comments/1behsfl/is_it_true_that_theres_no_dominated_move_and_thus/

from pymnash.game import game_from_payoffs

# for payoffs
# innermost array is the payoffs themselves
# next out is C
# next out B
# outermost is a
# so


if __name__ == '__main__':

    # 0 = italian 1 = frenc
    payoffs = [[[[2,18,6], [2, 18, 8]], # A0 B0 C0 A0 B0 C1 
               [[18, -2, 6],[10, -2, 8]]], # A0 B1 C0 A0 B1 C1
               [[[0, 10, -2], [8, 10, 18]], 
               [[-8, 6, -2], [-8, 6, 18]]]]
    agame = game_from_payoffs(payoffs)
    print('slicex', agame.payoffs[0, :, :])
    print()
    print('slicey', agame.payoffs[:, 0, :])
    print()
    print('slicez', agame.payoffs[:, :, 0])
    print()

    for ne in agame.find_all_equilibria():
        print(ne)
