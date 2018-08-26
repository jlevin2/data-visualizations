## A Brief Look Into PUBG

For this experiment, I wanted to look at how PUBG strategy and gameplay evolved as
the game progessed. To investigate with the kaggle data provided, I looked at
where players killed one another and how they did it over time. Using these figures,
we might understand how PUBG evolves.

All data, code, and visualizations are available inside *visualization* directory.

# Where do players kill over time?

Let's look at where players kill by game period. I chose to look at 3 periods.
- Pre 10 min (**Blue**)
- Between 10-20 min (**Green**)
- Post 20 min (**Orange**)

![All 3]('visualization/all_3.png')

Takeaways:
1. Early game kills are generally in highly urban areas, specifically Pochinki, School, and over by Mylta.
2. Mid game is slighly broader with players venturing outside the highly urban areas
3. End game is very spread out and this is logical since the players have little control over where
the end-game takes place so it is not skewed to any particular city

To better see the contrast, please see the appendix where all 3 time periods are shown
independently.

# How do they kill over time?

Rather than look at kills by individual weapons, we can look at weapon types (AR, Sniper, etc.).

There use over time can show how players chose loadouts further into the game.

![Weapon Types]('visualization/weapon_type.png')

Takeaways:
1. ARs are the most popular weapon from start to end; they offer so much flexibility and
utility that players use them from the start
2. The environment (bluezone, fall damage, drowning) is the next biggest killer; which is surprising
since skilled players can generally avoid dying to these things.
3. It is also interesting to see how the environment spikes in kills when the circle moves,
see time windows 1500, 1600 etc.
4. Shotguns are used for the first 10 min or so, but then are rarely used again
5. SMGs follow a similar arc as Shotguns, but at slightly higher levels
6. Snipers and DMRs seem to only be used (or effective, rather) after 12 min, but still remain
< 20% of kills at all points. This is interesting as many players feel snipers are crucial tools;
but the data shows a good AR is always are best.
7. Though, after ~12 min Snipers/DMRs make up the second highest % of kills to ARs

Next, let's look at where weapons are sourced. This meaning either from spawn or from crates.
Crate weapons are generally stronger, but let's see if they are used most late into games.

![Weapon Source]('visualization/weapon_source.png')

It appears that despite their popularity, crate weapons don't make up a significant share of
kills. Though, they are definitely used at a higher rate the later the game goes on.

Is there skew in where crate weapons are used to kill?

![Crate Kills]('visualization/crate_kills.png')

As can be seen, crate kills are pretty evenly spread out. This makes sense for 2 reasons,
first we already showed that kills are more even in the late game (when Crates drop) and because
crates are random we would expect their kills to be semi-random across the map.

## Appendix

![Early Game]('visualization/early_game.png')

![Mid Game]('visualization/mid_game.png')

![Late Game]('visualization/late_game.png')

