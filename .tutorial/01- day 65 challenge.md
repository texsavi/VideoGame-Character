# 👉 Day 65 Challenge

Today is a project day! You're going to use what you've learned about OOP (on Day 64) to store characters for my video game.

1. My game needs to have a character with a name, health and magic points.
2. It needs these values setup when it is initialized.
3. It needs a method to output this data.
4. There should be a sub-class 'player' which inherits from character and also has a number of lives.
5. Player should also have an 'am I alive?' method which checks the player status and reports back yes or no.
6. There should also be an 'enemy' sub-class with additional 'type' and 'strength'.
7. 'enemy' should have **two** sub-classes:
     1. 'orc' with a 'speed' attribute.
     2. 'vampire' with a 'day/night' tracker
8. Instantiate **one** player, **two** vampires and **three** orcs. You choose their names.
9. Print out their values.


Example:

```
🌟Generic RPG🌟

Player
Name: David
Health: 100
Magic Points: 50
Lives: 3
Alive?: Yes

Name: Boris
Health: 45
Magic Points: 70
Type: Vampire
Strength: 3
Day/Night?: Night

Name: Rishi
Health: 70
Magic Points: 10
Type: Vampire
Strength: 75
Day/Night?: Day

Name: Bill
Health: 60
Magic Points: 5
Type: Orc
Strength: 75
Speed: 90

Name: Ted
Health: 75
Magic Points:40
Type: Orc
Strength: 80
Speed: 45

Name: Station
Health: 35
Magic Points: 40
Type: Orc
Strength: 49
Speed: 50
```

<details> <summary> 💡 Hints </summary>
  
- You only need to inherit from the class dierctly above. So orc only needs to inherit from enemy, for example.

</details>