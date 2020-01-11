#first function for feeling input 

def choose_feeling ():
    userfeeling = input("Choose a feeling: ")
    return userfeeling
    
feeling = choose_feeling()

# lists of lists for songs

happy = ['Walking on Sunshine by Katrina and the Waves', 'Feeling Good by Nina Simone', 'Happy by Pharrell']
sad = ['Sad Songs by Elton John', 'Someone like You by Adele', 'Sad, Sad Day by Muddy Waters']
excited = ["I'm So Excited by The Pointer Sisters", "Bad by Michael Jackson", "Dancing on My Own by Robyn"]
angry = ['Drop the World by Lil Wayne', "Cleanin' Out My Closet by Eminem"]
songs = [happy, sad, excited, angry]

#second function that randomly selects song based on mood input
import random
def choose_song (feeling):
    if (feeling == "happy"):
        print(random.choice(happy))
    elif (feeling == "sad"):
        print(random.choice(sad))
    elif (feeling == "excited"):
        print(random.choice(excited))
    elif (feeling == "angry"):
        print(random.choice(angry))
    else:
        print('Try again!')

choose_song(feeling)
