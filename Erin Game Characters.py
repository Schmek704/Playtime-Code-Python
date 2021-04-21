# This is an interactive meet & greet with characters that E7 is creating to implement in her game

char_story = {
'pearl' : "Meet Pearl! Pearl is a Fuzzball. She lives in Teeny Tinyville. \nShe has a large family, is the oldest of the children along with her brothers Freaky, Cover, and Chippy, and her sisters Squeaks and Dottie. \nHer mom, Cotton, is the sweetest snake in Teeny Tinyville, and loves all her children. \nPearl goes to Gingerbread Elementary, and is currently in 1st grade with her teacher Ms M. \nPearl loves to wear bows in her hair everywhere she goes! \nShe lives in a house with her sister Squeaks."
}
intros = True

while intros == True:
    meet = input("\n\n\nWho would you like to meet?  ")
    print(char_story[meet.lower()])

    next_meet = input("\n\n\nWanna meet anyone else right now? (y/n)")

    if next_meet.lower() != 'y':
        intros = False
