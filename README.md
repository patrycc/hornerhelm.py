# Hornerhelm [Working title]

My try at a tactical fighting game. Currently in the conceptual phase only. I plan to write the game in python + pygame.

## Planned Features

Hornerhelm will feature tactical battles against monsters which require the player to set up a team specifically planned for a certain situation.

###Battle

While the fights will remember of round-based RPGs, the game will NOT contain the typical RPG elements: Leveling the characters, looting treasures and equipping items on the characters. Instead, the game will require the player to set up a team of fighters (named 'Einherjar' in the game) specifically for every monster encounter. A lot of try and error will be necessary for the player to win a battle. 

####The 'aspects' of an einherjar

A team may consist of at max five einherjar. (But is not needed and not always recommended.) One einherjar has five slots for five different 'aspects'. An aspect defines the role and abilities an einherjar has in battle. One can give the same five aspects to one einherjar to make him/her especially suited for that role, or mix it up to create synergies with others aspects.
Here is a list of the five aspects and how they influence the einherjar.

#####Aspect of war
Raises melee attack power and life of the einherjar. Does not raise the ability to perform any healing or rune magic.

#####Aspect of the guardian
Raises the life points and the ability to distract monsters from other einherjar.

#####Aspect of might
Raises the potency to perform devastating rune magic, which damages all enemies. Life points will raised only a little, so be careful about attracting monster attacks.

#####Aspect of healing
Raises the efficiency to heal. Life points will also be raised only a little.

#####Aspect of the trickster
This aspect raises all abilities, but only moderatly. But in addition, the bearer of this aspect may have the chance to perform abilities with thrice the efficiency or avoid being dealt any damage.

####Abilities in battle
Per round, every einherjar can perform one action. Some of them require points in that certain ability to be able to be performed.

#####Attack
Melee attacks one target.

#####Defend
Goes into a defensive stance for one round, reducing all incoming damage by 50%.

#####Rune magic
Damages all foes. Requires points in this ability.

#####Healing
Heals an einherjar. Requires points in this ability.

####Synergies
The player is free is free to combine the aspects on an einherjar in any possible combination. Combining different aspects causes synergies, which cause different effects. To give an example: An einherjar which has aspects of war AND healing, heals her/himself for a percentage of the caused melee damage.

####Aggression
Causing damage on your foes will enrage them, causing them to attack the einherjar which caused the most damage. But those who deal the most damage won't always be those who have the most hit points. Therefore the player has to distract the monsters away from those who damage (or heal, since it also generates aggression) to those who can take more hits. Einherjars with the aspect of the guardian will be especially suited for that job, since this aspects grants a lot of hitpoints and increases the generated aggression.

####General Battle Dynamic
The most important thing in battle is to defeat the enemies of course. But this won't be that easy: If all einherjar only deal damage, everyone will be dead soon because no one is healed. But even then it will be difficult to keep up with the foes, because you need at least one einherjar with the aspect of the guardian to distract them from your more squishy einherjar.
Battle will be a fine line between causing damage, distracting, defending, healing and so on.

##Background Story

In addition to the core of the game, the battles against monsters, I'll try to tell a story in a fantasy world, which is mostly based on nordic mythology.

This is the story so far:

After the apocalyptic events of the 'Ragnarök', the gods are dead, even the allfather and ruler of Asgard, Odin. During the events of the ragnarök he led the 'einherjar' into battle. Einherjar are once fallen heros, who are dwelling in the 'Vallhall' after their deaths, spending their days drinking mead, eating pork and kept training their fighting skills, until they are called into battle again.

When einherjar are killed, they just reappear one day later in the Valhall, because they are dead anyway. And this also happened after the Ragnarök: All einherjar were killed, but just reappared in the Valhall. Unlike the gods.

After the death of Odin, who granted the power of the five aspects to the einherjar, the aspects were then incorporated by five valkyries. The valkyries, which were formerly mere servants to Odin and his einherjar, now rule the remnants of Asgard (now: Valgard) and Valhall.

But even centuries after the war, monsters still roam the lands: giants, fenrirspawn and albs, which threaten the young human nation of Lifthrasia.

The einherjar now have to be led into battle once again!

##Inspiration

I was loosely planning a RPG-like game for years now, but could never settle on a rule system. I was always influenced by a game I was enjoying by that time (which were mostly roleplaying games...) so I was sure about my game: It needs characters which increase their levels! They have to kill the boss and loot the drop for epic equipment! In the end, I dropped most of that, for the following reasons.

Realizing that the concept of leveling up a character and slowly increasing their stats may give a rewarding feel and a sense of character development, but it was terribly tedious in terms of gameplay. It becomes especially tedious if the game actually offers fun and tactical boss fights, but you had to slay thousands of trashmobs beforehand and still don't have the needed gear or level.

In the end, I was getting rid of everything that would hinder the actual gameplay: Leveling, tedious stat increasing, killing trashmobs, all of the artificial scarcity. Instead I put in everything I wanted to see: Dynamic team building, tactical battles (and tactical losing, without being afraid of running through an endless dungeon again and losing all of the gold.), experimenting with multiclassing and their resulting synergies (There are 3125 possible combinations for a single einherjar alone and 15625 possible team combinations.)

I always liked the possibility to multiclass in games, combining two classes to create a character with more possibilities. Sadly, it rarely was implemented that well. I first encountered it in Baldur's Gate II and Neverwinter Nights, but in retrospect, the implementation of the system was rather poor. If you combined two classes, the only main consequence was that the character was receiving less XP - a rather dubious concept of balancing in my opinion. The games I liked multiclassing in were Titan Quest and the latest Etrian Oddissey game - combining two classes actually complimented the other. But unfortunatly I never saw the possibility to combine more than two classes after Neverwinter Nights again. (I didn't play the sequels.)

The battle dynamic of distracting and taunting foes stemmed from MMORPGs, where it is state of the art. The most popular example would be World of Warcraft of course, but The Elder Scrolls Online also implemented it nicely.

The tactical battle with it's flows of attacking, distracting, defending and healing is an influence from different games and even genres, be it RPGs or action games.
