# Gold gain
"""
In some video games, especially rouge-like and rouge-lite, you are often presented with upgrades affecting your gold gain.
Most often these upgrades either a percentage increase of gold gained (e.g. 5% gold gained) or a flat amount earned per enemy defeated.
Sometimes you are presented with a third option: on defeating an enemy, gain a chance for a big extra payout.
Choosing between the chance for a big payout and earning a fixed extra amount can be tricky, so this script is designed to make this decision easy
 """

enemies = 0                                     # Number of defeated enemies
extra_gold_flat = 5                             # Amount of extra gold per defeated enemy
total_gold_flat = enemies * extra_gold_flat     # Total extra gold earned after defeating a number of enemies.
gamble_prob = 0.15                              # Probability of getting huge amount of bonus gold (extra_gold_gamble)
extra_gold_gamble = 40                          # Amount of extra gold earned by chance.


for i in range(100):
    enemies += 1
    total_gold_flat = enemies * extra_gold_flat
    total_gold_flat = round(total_gold_flat, 2)

    total_gold_gamble = enemies * gamble_prob * extra_gold_gamble
    total_gold_gamble = round(total_gold_gamble, 2)

    print(f"Flat extra gold earned: {total_gold_flat}, \nExtra gold earned by gamble: {total_gold_gamble}")

