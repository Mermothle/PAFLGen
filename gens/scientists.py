from random import *

def scientistPile(list):
    return randint(0, len(list)-1)

def personalityPile(personality):
    yourPersonality = genPersonality[scientistPile(genPersonality)]
    return yourPersonality

def opinionGen():
    finalPersonality = personalityPile(genPersonality)
    finalOpinion = ""
    finalMutOpinion = ""

    if finalPersonality in genPersonalityPos:
        finalOpinion = genPosOpinion[scientistPile(genPosOpinion)]
        finalMutOpinion = genMutPosEvent[scientistPile(genMutPosEvent)]
        return finalPersonality, finalOpinion, finalMutOpinion
    
    if finalPersonality in genPersonalityNeg:
        finalOpinion = genNegOpinion[scientistPile(genNegOpinion)]
        finalMutOpinion = genMutNegEvent[scientistPile(genMutNegEvent)]
        return finalPersonality, finalOpinion, finalMutOpinion


def scientistGen():
    appearance = genAppearance[scientistPile(genAppearance)]
    hairColor = genHairColor[scientistPile(genHairColor)]
    hairType = genHairType[scientistPile(genHairType)]
    eyeColor = genEyeColor[scientistPile(genEyeColor)]
    eyeType = genEyeType[scientistPile(genEyeType)]
    opinionGenCarrier = opinionGen()
    personality = opinionGenCarrier[0]
    experience = genExperience[scientistPile(genExperience)]
    num = genNum[scientistPile(genNum)]
    goal = genGoal[scientistPile(genGoal)]
    result = genResult[scientistPile(genResult)]
    backstory = genBackstory[scientistPile(genBackstory)]
    thought = genBackthought[scientistPile(genBackthought)]
    view = genView[scientistPile(genView)]
    opinion = opinionGenCarrier[1]
    event = genEvent[scientistPile(genEvent)]
    mutEvent = opinionGenCarrier[2]


    scientistDone = '''\
    You are a{pApp} scientist with {hairT} {hairC} hair and {eyeT} {eyeC} eyes.
    You're {exp} your field of work, and you work primarily with {num} level mutants.
    You look upon your subjects with {gPer}, and the mutants {gOpi}
    You joined the facility because {gGoal}, and {gRes}
    {bSty} It {bTht}
    You view your latest days at the facility {gView} 
    Your most notable day at the facility was {gEve}
    {mutE}\
'''.format(pApp=appearance, hairT=hairType, hairC=hairColor, eyeT=eyeType, eyeC=eyeColor, gPer=personality, gGoal=goal, gRes=result, bSty=backstory, bTht=thought, gView=view, gOpi=opinion, gEve=event, exp=experience, num=num, mutE=mutEvent)
    return scientistDone

genAppearance = [" confident", " nervous", " skittish", " cold", "n excitable", "n over-eager", " no-nonsense", " calm", " kind", " stern", "n exasperated", " ditzy"]
genHairColor = ["brown", "black", "blonde", "red", "ginger", "gray", "white",]
genHairType = ["straight", "curly", "coarse", "fluffy", "shaggy", "wavy", "spiky", "coily"]
genEyeColor = ["brown", "black", "gray", "white", "yellow", "red", "orange", "hazel", "purple", "blue", "green", "pink"]
genEyeType = ["hazy", "bright", "dark", "pale"]
genPersonalityPos = ["kindness", "pity", "worry", "sadness", "anxiety", "sympathy", "confusion", "interest", "curiosity"]
genPersonalityNeg = ["contempt", "disgust", "annoyance", "frustration", "hatred"]
genPersonality = genPersonalityPos + genPersonalityNeg
genExperience = ["fairly experienced in", "very experienced in", "in training in", "rather new to", "very confident in", "familiar enough with", "still learning the ropes of", "getting used to"]
genNum = ["001", "002", "003", "004"]
genGoal = ["you wanted to progress science", "you were always curious about the mutants", "you really needed the money", "your family pressured you into it", "you had friends working there", "someone you knew got brought there a long time ago", "you were a released mutant, always wondering what it was like to be a scientist", "you want to show up the other scientists"]
genResult = ["it's been a mess from the start.", "you regret coming here every day.", "you actually really enjoy your position.", "you've made good friends with some of the more tolerable scientists.", "you've grown to find the mutants pitiable.", "you feel like your research has come a long way.", "you like the feeling of power this place gives you."]
genBackstory = ["You've always heard about how mutants were perceived since you were little.", "You saw a mutant get into a massive fight, and they ended up dying.", "You've always found science fascinating in general, especially this new science.", "You want to be the best you can be, and saw becoming a scientist as an opportunity."]
genBackthought = ["made you wonder if you made the right choices.", "made you think more about how you perceive life.", "leaves something to be desired.", "has left a dark shadow over your life.", "has made you even more curious than you were before."]
genView = ["in a more positive light.", "as a slog sometimes.", "as new and interesting.", "as a never-ending whirl of chaos.", "with great anxiety.", "as an opportunity to keep learning.", "as a babysitting routine.", "poorly, since your fellows have started annoying you to death."]
genPosOpinion = ["elicit a lot of sympathy from you.", "make you feel like a monster for experimenting on them.", "are people you get attached to too quicky."]
genNegOpinion = ["get on your nerves more and more.", "are just subjects in your eyes.", "make you feel like a monster.", "are a sore point for you.", "make you feel sick on sight."]
genOpinion = genPosOpinion + genNegOpinion
genEvent = ["the time a riot broke out, and you almost got killed by one of the subjects. You're still scarred from it.", "the day your favorite subject was terminated. You still miss them.", "when one of the subjects reacted poorly to an experiment and had to be violently terminated.", "when a shouting match started amongst your superiors, and you just wanted to go home."]
genMutPosEvent = ["You're currently planning on helping a mutant escape.", "You've helped a mutant escape in the past.", "No mutants have ever broken out under your care.", "You have connected a lot with your subjects.", "You like seeing how happy you can make the mutants.", "You try to offer comfort to any mutants in pain, even if you get scolded for it."]
genMutNegEvent = ["No mutants have ever broken out under your care.", "You keep the mutants as obedient as you can.", "Whenever a mutant is causing problems, you're the one to handle it.", "The mutants have a fearful view of you, and you think they're just spineless.", "You've participated in some of the harshest experiments."]
genMutEvent = genMutPosEvent + genMutNegEvent