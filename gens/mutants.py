from random import *

def mutantPile(list):
    return randint(0, len(list)-1)

#Code is XT00#-###
def codeGen():
    codeLetter = alphabet[mutantPile(alphabet)]
    codeT = "T"
    codeDash = "-"
    codeRank = "0"
    codeNumbers = str(randrange(100, 999))

    urMutation = typeGen(genMutationType)

    if urMutation in genMutation001:
        codeRank = "001"
    elif urMutation in genMutation002:
        codeRank = "002"
    elif urMutation in genMutation003:
        codeRank = "003"
    elif urMutation in genMutation004:
        codeRank = "004"
    

    completedCode = codeLetter + codeT + codeRank + codeDash + codeNumbers
    return [completedCode, urMutation]

def backstoryGen(origin):
    backstoriesBaby = genOriginStory[0], genOriginStory[1]
    backstoriesChild = genOriginStory[2], genOriginStory[3], genOriginStory[4], genOriginStory[5], genOriginStory[6]
    backstoriesAdult = genOriginStory[7], genOriginStory[8], genOriginStory[9]
    urBackstory = origin

    if urBackstory in backstoriesBaby:
        urBackstory = genBabystories[mutantPile(genBabystories)]
        return urBackstory
    elif urBackstory in backstoriesChild:
        urBackstory = genChildstories[mutantPile(genChildstories)]
        return urBackstory
    elif urBackstory in backstoriesAdult:
        urBackstory = genAdultstories[mutantPile(genAdultstories)]
        return urBackstory

def typeGen(yourMutation):
    yourMutation = genMutationType[mutantPile(genMutationType)]
    return yourMutation

def appearanceGen():
    oddLook = randint(1, 10)
    oddAppearance = ""
    oddHair = randint(1, 10)
    oddHairColor = ""
    allHairs = genHairColor + genBonusHairColors

    if oddLook == 2 or oddLook == 5 or oddLook == 9:
        oddAppearance = genBonusAppearance[mutantPile(genBonusAppearance)]
    else:
        oddAppearance = ""
    if oddHair == 2 or oddHair == 9:
        oddHairColor = allHairs[mutantPile(allHairs)]
    else:
        oddHairColor = genHairColor[mutantPile(genHairColor)]
    return oddAppearance, oddHairColor

def mutantGen():
    physicalAppearance = genPhysicalAppearance[mutantPile(genPhysicalAppearance)]
    appearanceGenCarrier = appearanceGen()
    hairColor = appearanceGenCarrier[1]
    oddAppearance = appearanceGenCarrier[0]
    hairType = genHairType[mutantPile(genHairType)]
    eyeColor = genEyeColor[mutantPile(genEyeColor)]
    eyeType = genEyeType[mutantPile(genEyeType)]
    extras = genExtras[mutantPile(genExtras)]
    mishaps = genMishaps[mutantPile(genMishaps)]
    codeGenCarrier = codeGen()
    mutationType = codeGenCarrier[1]
    medicalProblems = genMedicalProblems[mutantPile(genMedicalProblems)]
    originStory = genOriginStory[mutantPile(genOriginStory)]
    backstoryGenCarrier = backstoryGen(originStory)
    finalCode = codeGenCarrier[0]
    caretakerDescriptor = genCaretakerDescriptor[mutantPile(genCaretakerDescriptor)]
    caretakerAppearance = genCaretakerAppearance[mutantPile(genCaretakerAppearance)]
    caretakerPersonality = genCaretakerPersonality[mutantPile(genCaretakerPersonality)]
    caretakerView = genCaretakerView[mutantPile(genCaretakerView)]


    mutantDone = '''\
    Your Facility code is {fCode}.
    You are a {pApp} mutant with {hairT} {hairC} hair and {eyeT} {eyeC} eyes.
    Your mutation is {mutT}, and you suffer from {medP}. {oddA}
    You came to the Facility {orS}. {backG}
    {extr}
    {mish}
    One of your usual caretakers is a {careD} {careA} scientist, who {careP} You {careV}\
'''.format(fCode=str(finalCode), pApp=physicalAppearance, hairT=hairType, hairC=hairColor, eyeT=eyeType, eyeC=eyeColor, mutT=mutationType, medP=medicalProblems, oddA=oddAppearance, orS=originStory, backG=backstoryGenCarrier, extr=extras, mish=mishaps, careD=caretakerDescriptor, careA=caretakerAppearance, careP=caretakerPersonality, careV=caretakerView)
    return mutantDone

genPhysicalAppearance = ["sickly", "nervous", "confident", "relatively normal", "very unstable", "aloof", "uncaring", "overly friendly", "kindhearted", "typical", "unusual", "peppy", "dour", "positive", "tough", "determined"]
genHairColor = ["brown", "black", "blonde", "red", "ginger", "gray", "white",]
genHairType = ["straight", "curly", "coarse", "fluffy", "shaggy", "wavy", "spiky", "coily"]
genEyeColor = ["brown", "black", "gray", "white", "yellow", "red", "orange", "hazel", "purple", "blue", "green", "pink"]
genEyeType = ["hazy", "bright", "dark", "pale"]
genMutation001 = ['teleportation', 'transformation', 'extreme strength', 'telekinesis', 'portals', 'influence', 'mind reading', 'memory stealing', 'healing others', 'causing good luck', 'a form of elemental kinesis']
genMutation002 = ['telepathy', 'prophecy', 'regeneration', 'heightened senses', 'rapid aging', 'zombification', 'body separation', 'xenoglossy', 'invisibility', 'insomnia', 'astral projection', 'invincibility', 'perfect immunity', 'levitation', 'hypermobility', 'dream manipulation', 'stretchy biology', 'bioluminesence', 'multicolored blood', 'going chameleon', 'incredible hearing', 'alchemizing items in your stomach', 'emitting light', 'controlling shadows', 'being amphibious', 'having aquatic traits']
genMutation003 = ['growing crystals', 'generating heat', 'emitting cold', 'having animalistic features', 'magnetism', 'liquid control', 'producing venom', 'super speed', 'emotion draining', 'melting yourself', 'liquefying objects', 'temperature control', 'having a crushing bite force']
genMutation004 = ['spitting acid', 'combustion', 'uncontrollable rage', 'mental lockdown', 'breathing fire', 'emitting dangerous levels of radiation', 'causing bad luck', 'causing necrosis', 'having an ultrasonic voice', 'having a deadly stinger', 'having a dangerous maw', 'amoeboid skin', 'shedding plague']
genMutationType = genMutation001 + genMutation002 + genMutation003 + genMutation004
genMedicalProblems = ["crippling migraines", "stomach pain", "heart irregularity", "breathing troubles", "fragile skin", "vertigo", "chronic pain", "forgetfulness", "difficulty getting around", "sensory overload", "crippling anxiety", "obsessive compulsions", "restlessness", "joint pain", "toothaches", "nerve pain", "spinal issues", "temperature sensitivity", "a poor immune system", "chronic fatigue", "endless paranoia", "hemophilia", "intrusive thoughts", "spinal issues", "mouth problems", "ear issues", "an inability to focus", "exhaustion", "shortness of breath", "compulsive itching", "spontaneous pain", "constant coughing", "having a scratchy throat", "mouth pain", "difficulty sleeping", "trouble staying awake", "overt clumsiness", "delusions", "varying hallucinations", "spasms", "compulsive rocking"]
genOriginStory = ["as a baby, taken at birth", "as a baby, given willingly by your parents", "as a child, for utilizing your mutation publicly", "as a child, handed over by tired parents", "as a child, caught as a runaway", "as a child, because you thought it would be fun", "as a child, as the result of a thorough investigation", "as an adult, caught out by accident", "as an adult after turning yourself in", "as an adult, betrayed by those you loved"]
genExtras = ["You have a lot of hobbies, and some of the other subjects find it annoying.", "You wish you could be outside.", "You've grown very attached to one of the scientists that tends to you.", "You're always trying to earn the scientists' approval.", "Your main goal is to escape one day.", "You want to become a scientist.", "You're surprisingly popular amongst the other subjects.", "The other subjects are nervous around you.", "You value your life over that of others.", "You wish you could save everyone.", "You kind of enjoy the fight testing.", "You're just doing your best to survive.", "You feel like you might not be around for much longer.", "You think some of the other subjects deserve to be terminated.", "You feel envious of the subjects that receive special treatment.", "Sometimes it's hard not to feel inferior to everyone else.", "You feel like the scientists are always watching you.", "You're always watching and gauging the danger levels of the other subjects."]
genMishaps = ["One time, you tried to eat soap, and the scientists had to wrestle it away from you.", "At some point, you snapped and tried to fight a scientist, and they look upon you more strictly as a result.", "You've gone out of your way to try befriending the scientists, to varying levels of success.", "You crawled in a drawer and pretended to be clothes once.", "You stayed in the bathroom hiding from the cameras for so long the scientists thought you were dead.", "You attempted to create a revolution one time, but you just got scolded.", "The time you made a campfire out of your study room is commonly recounted as the time the Facility found out their fire alarms were broken.", "After oversleeping for basically every event in your life, the scientists eventually shoved an alarm clock directly into your pillow.", "Trying to escape through a wall was not your best idea, because you had to get yanked out in a very unflattering fashion.", "Your refusal to eat your vegetables is so notorious that short of physical restraints, the scientists always have to bribe you.", "You fixate very intensely on a single one of your studies, and it distracts you from everything else.", "Sometimes you try to hide from the scientists, but they always know where you are. You keep doing it anyways.", "You've memorized your daily routine to the point that any deviation throws you off.", "You leave your sink running because you like the noise, and the scientists keep telling you to shut it off.", "You demanded enrichment, and when the scientists gave you multicolored books, you turned them into origami and bounced them off your cell walls."]
genBabystories = ["You wonder what it would be like to have a real family.", "You wonder if you family hated you.", "You're convinced your real family will come and get you one day.", "You think one of your parents might be a scientist.", "A life growing up in the Facility has left you used to the monotony.", "You think some of the scientists might view you as your own.", "You grew up alongside another subject and are very protective of them."]
genChildstories = ["You miss playing outside like you used to.", "You hope your friends are okay.", "You wonder if your family is still thinking about you.", "You hold a lot of regrets.", "You wish you were better to the people around you.", "You try to cling to your good memories.", "You miss your parents.", "Sometimes you try to think of some of the scientists as your family, but it's not the same.", "The world is so dull now.", "You grew up alongside another subject and are very protective of them."]
genAdultstories = ["You wonder if everything was worth it.", "Your life has been a mess, and you wonder if this place will make it worse.", "You've been through enough to try and stay optimistic, but it's hard.", "Holding a job was better than being in this place.", "If your family is still out there, you hope they're okay.", "You wonder if the choices you made in life were the right ones.", "You wonder if you got what was coming to you."]
genBonusAppearance = ["You have small horns.", "Your eyes are slitted.", "Your skin is discolored in some places.", "You have scaly formations in some spots on your skin.", "You have a tail.", "Your hair is bi-colored.", "Your eyes have additional colors in them.", "Your pupils are strangely shaped.", "There are tattoo-like markings on your skin.", "Your skin sometimes takes on an unusual tint.", "Your anatomy has always been a bit unusual.", "Your hair is strangely colored at the ends.", "Your teeth are sharper than usual."]
genBonusHairColors = ["blue", "pink", "purple", "green"]

genCaretakerDescriptor = ["frumpy", "absentminded", "skittish", "serious", "excitable", "gentle", "curious", "irritable", "calm", "eerie", "neurotic"]
genCaretakerAppearance = ["older", "younger", "new", "experienced", "mainstay", "grunt", "high-ranking"]
genCaretakerPersonality = ["is usually kind with you.", "is always checking up on you.", "is typically focused on getting results out of you.", "is protective over you.", "views you exactly as what you are - a test subject.", "views you as someone worthy of pity.", "always looks at you like you're stupid.", "would probably terminate you if they got the chance.", "visibly enjoys their time with you.", "seems uninterested in you."]
genCaretakerView = ["feel like an object in their presence.", "get depressed around them.", "feel like you could do better.", "are anxious around them.", "are happy to see them, despite everything.", "want to win them over more.", "want to hide away when they show up.", "feel like you need to earn their approval or you'll die.", "are curious about your own experiments.", "have learned to be curious about the experiments of others from them.", "feel some kinship to them, because they are also a mutant."]

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]