__author__ = 'chris'
import shelve

# Write a function (not a class) that takes two arguments, a string player name and an integer score,
# and keeps a "high score" table in a Python shelve. If the integer argument is higher than the given
# player's current high score (or if the player has no recorded high score),
# log the value as this player's new high score. The function should return the player's current high
# score. Remember, a function is not the same thing as a class and it's a function that's needed.
# Again, write a separate test module that verifies the operation of the function.


def writehighscore(name, score):

    fn = r'/Users/chris/Documents/dev/oreilly/python/python2homework/L5_Project1/highscore.shelve'
    shelf = shelve.open(fn)
    #check if player has any record
    try:
        if shelf['name']:
        #check if new record is higher than existing
            if score > shelf['name']:
                shelf['name'] = score
                return score
        #else do no update
    except KeyError:
        print ("Player not found, adding new score")
        shelf['name'] = score
    return shelf['name']
    shelf.close()