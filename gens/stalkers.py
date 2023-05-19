from random import *

def stalkerPile(list):
    return randint(0, len(list)-1)

''' def vView(view):
    if view in genPosView:
        finalAnswer = genPosAnswer[stalkerPile(genPosAnswer)]
        finalView = view
        return finalView, finalAnswer
    
    if view in genNegView:
        finalAnswer = genNegAnswer[stalkerPile(genNegAnswer)]
        finalView = view
        return finalView, finalAnswer
    
    return finalView, finalAnswer'''
    
def viewPile(view):
    yourView = genPeopleView[stalkerPile(genPeopleView)]
    return yourView

def viewGen():
    finalView = viewPile(genPeopleView)
    finalAnswer = ""
    #print(view)

    if finalView in genPosView:
        finalAnswer = genPosAnswer[stalkerPile(genPosAnswer)]
        #finalView = view
        return finalView, finalAnswer
    
    if finalView in genNegView:
        finalAnswer = genNegAnswer[stalkerPile(genNegAnswer)]
        #finalView = view
        return finalView, finalAnswer
    
def friendPile(friend):
    friendView = genFriendAttitude[stalkerPile(genFriendAttitude)]
    return friendView

def friendGen():
    friendOpinion = friendPile(genFriendAttitude)
    friendEvent = ""

    if friendOpinion in genFrAtPos:
        friendEvent = genFrPosRes[stalkerPile(genFrPosRes)]
        return friendOpinion, friendEvent

    if friendOpinion in genFrAtNeg:
        friendEvent = genFrNegRes[stalkerPile(genFrNegRes)]
        return friendOpinion, friendEvent

def stalkerGen():
    appearance = genAppearance[stalkerPile(genAppearance)]
    hairColor = genHairColor[stalkerPile(genHairColor)]
    hairType = genHairType[stalkerPile(genHairType)]
    eyeColor = genEyeColor[stalkerPile(genEyeColor)]
    eyeType = genEyeType[stalkerPile(genEyeType)]
    goal = genGoal[stalkerPile(genGoal)]
    result = genResult[stalkerPile(genResult)]
    exposure = genExposure[stalkerPile(genExposure)]
    feel = genFeel[stalkerPile(genFeel)]
    injury = genInjury[stalkerPile(genInjury)]
    attitude = genAttitude[stalkerPile(genAttitude)]
    viewGenCarrier = viewGen()
    friendGenCarrier = friendGen()
    #viewGen(genPeopleView)
    peopleView = viewGenCarrier[0]
    #peopleView = genPeopleView[stalkerPile(genPeopleView)]
    answer = viewGenCarrier[1]
    #answer = genAnswer[stalkerPile(genAnswer)]
    friendAttitude = friendGenCarrier[0]
    friendEvent = friendGenCarrier[1]
    event = genEvent[stalkerPile(genEvent)]



    stalkerDone = '''\
    You are a {pApp} stalker with {hairT} {hairC} hair and {eyeT} {eyeC} eyes.
    You got into stalking {gGoal}, and {gRes}.
    After your exposure to The Zone, {gExp} Your feeling for the radiation there {gFeel}
    {gPpl} {gAns}
    {inj}, and you tend to be pretty {ati} while stalking.
    You get along {getA} with your fellow stalkers. You {getAc}. 
    Your most notable event in The Zone was {gEve}\
'''.format(pApp=appearance, hairT=hairType, hairC=hairColor, eyeT=eyeType, eyeC=eyeColor, gGoal=goal, gRes=result, gExp=exposure, gFeel=feel, gEve=event, gPpl=peopleView, gAns=answer, inj=injury, ati=attitude, getA=friendAttitude, getAc=friendEvent)
    return stalkerDone

genAppearance = ["tired", "excitable", "calm", "pessimistic", "optimistic", "adventurous", "skittish", "irritable", "casual", "daredevil"]
genHairColor = ["brown", "black", "blonde", "red", "ginger", "gray", "white",]
genHairType = ["straight", "curly", "coarse", "fluffy", "shaggy", "wavy", "spiky", "coily"]
genEyeColor = ["brown", "black", "gray", "white", "yellow", "red", "orange", "hazel", "purple", "blue", "green", "pink"]
genEyeType = ["hazy", "bright", "dark", "pale"]
genGoal = ["because you thought it would be fun", "after your friends roped you into it", "on a whim", "to make some extra money", "to explore something for once", "to protect someone you care about"]
genResult = ["it's made you realize how dangerous life can be", "you feel like you lost a part of yourself while doing it", "it got stale after a while", "it's all you have to look forward to", "you don't think you'll ever get tired of it", "you're better off than you were before you started", "you've had way too many close calls", "you're even mentoring other people now", "you're tempted to live in The Zone one day"]
genExposure = ["you've developed a few health problems.", "you think other people might view you strangely.", "you're concerned at the thought of having mutated children.", "you think your life might be getting shorter.", "you feel kind of like a superhero.", "you're paranoid about hospital visits.", "you're worried the cops will find out and throw you in jail.", "you don't feel too different, and don't see what all the buzz is about."]
genFeel = ["is pretty intense.", "is almost nonexistent.", "is rather average.", "is better than that of your peers.", "always makes you nauseous.", "is so good that you're like a radar for irregularities.", "isn't that strong."]
genPosView = ["Some people see you as cooler, others see you as irresponsible.", "Your friends seem pretty impressed by your skills.", "People look up to you now.", "People seem to treat you with more respect now."]
genNegView = ["Your family doesn't know you're a stalker.", "Your friends regret getting you into stalking.", "People have started to give you weird looks.", "You hate the thought of anyone else knowing you're a stalker.", "Your stalking pals are the only people you can connect with anymore."]
genPeopleView = genPosView + genNegView
# genPeopleView = ["Your family doesn't know you're a stalker.", "Your friends regret getting you into stalking.", "Everyone around you keeps encouraging you to keep stalking.", "Your stalking pals are the only people you can connect with anymore.", "People have started to give you weird looks.", "Some people see you as cooler, others see you as irresponsible.", "You hate the thought of anyone else knowing you're a stalker."]
genPosAnswer = ["You don't really mind how people see you.", "Becoming a stalker might really have been worth it.", "You're determined to keep doing your best."]
genNegAnswer = ["The guilt always hangs over your head.", "You just keep pushing forward.", "You feel like your social life is crumbling around you.", "Sometimes you wonder what it'd be like to take more people along with you.", "You try not to think too much about what people think.", "You think people should lighten up a bit."]
#genAnswer = genPosAnswer + genNegAnswer
#genAnswer = ["The guilt always hangs over your head.", "You just keep pushing forward.", "You feel like your social life is crumbling around you.", "Sometimes you wonder what it'd be like to take more people along with you.", "You try not to think too much about what people think.", "You don't really mind how people see you.", "You think people should lighten up a bit."]
genInjury = ["You've almost died a few times in The Zone", "You've gotten hurt a few times in The Zone", "You've avoided injury so far in The Zone", "You've had a lot of close calls in The Zone"]
#genAti = ["reckless", "careful", "nervous", "patient", "cautious"]
#genAtii = genAti[stalkerPile(genAti)]
#genAttitude = "You tend to be pretty {atii} while stalking.".format(atii=genAti[stalkerPile(genAti)])
genAttitude = ["reckless", "careful", "nervous", "patient", "cautious"]
genFrAtPos = ["wonderfully", "well enough", "a lot", "most of the time"]
genFrAtNeg = ["poorly", "with a lot of frustration", "badly", "reluctantly"]
genFriendAttitude = genFrAtPos + genFrAtNeg
genFrPosRes = ["hang out with them all the time", "consider them your family", "have a bit of a crush on one of them", "always look forward to seeing them", "want to be around them all the time", "feel like your life is better with them in it"]
genFrNegRes = ["have to hold yourself back from snapping at them", "just keep your mouth shut and deal with them", "wish you were stalking with anyone else", "have considered ditching them more than a few times"]
genEvent = ["the time you had to run for your life from a patrol.", "a moment when you and your team found an anomaly that's always haunted you.", "a fateful day where you had to shoot your teammate to put them out of their misery.", "a time you found an item that you still keep with you to this day.", "the day you found the bodies of a less fortunate team.", "the day you found something you shouldn't have, and you can never stop thinking about it.", "the time where you, your friends, and some underpaid guard all just chilled out for a while."]