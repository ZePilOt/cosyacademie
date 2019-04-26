# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image intro = "BienvenueAlaCosyAcademie_intro.png"

#esprism
image Esprism = "Esprism_Naked.png"

#joueur
image side player = ConditionSwitch("sex==\"m\"", "boy.png", "True", "girl.png")

#fonds
image classePhysique = "classePhysique.jpg"

# Déclarez les personnages utilisés dans le jeu.

define pov = Character("[povname]", color="#fff", image="player")
define innerpov = Character("[povname]", color="#a1e7df", text_color="#a1e7df", image="player", who_suffix=" {i}{size=-20}à lui même{/size}{/i}", what_prefix="{i}", what_suffix="{/i}", window_background="dialoguebox_thoughts.png")
define med = Character('Medoc', color="#fff", image="Medoc")
define mog = Character('Moguri', color="#fff", image="Moguri")
define met = Character('Metalice', color="#fff", image="Metalice")
define mic = Character('Mickey', color="#fff" , image="Mickey")
define dieuv = Character('Dieuvomi', color="#fff", image="Dieuvomi")
define esprism = Character('Esprism', color="#fff", image="Esprism")

define von = Character('Von Yaourt', color="#fff", who_prefix="{font=Deutsch-webfont.ttf}{size=+8}", who_suffix="{/size}{/font}",what_prefix="{font=Squealer.ttf}{size=+10}", what_suffix = "{/size}{/font}", image="Von", window_left_padding=1000, what_xalign=0.5) 
define mat = Character('Mathilde', color="#fff", image="Mathilde")
define chuen = Character('Chuenpodo', color="#fff", image="Chuenpodo")
define caro = Character('Caro', color="#fff", image="Caro")
define din = Character('din', color="#fff", image="din")
define foulk = Character('Foulk', color="#fff", image="Foulk")

define inc = Character('???', color="#fff")
define tlm = Character('Tout le monde', color="#fff")

#Effets nouveaux
define longfade = Fade(0.8, 0.2, 0.8, color="#000")
define shortflash = Fade(.1, 0, .1, color="#fff")
define flash = Fade(.25, 0, .75, color="#fff")
define animintro = Fade(0.8, 0.2, 0.8, color="#fff")

#Musique
define audio.memento = "music/Memento.mp3"
define audio.haunted = "music/Haunted House.mp3"
define audio.journeys = "music/sb_journeys.mp3"
define audio.tomorrow = "music/sb_tomorrow.mp3"
define audio.wonderful = "music/sb_wonderful.mp3"

#FX
define audio.woosh = "sounds/creepy-hifreq-woosh.mp3"

# Le jeu commence ici
label start:

    

    python:
        #Points routes
        pointsmedoc=0
        pointsmoguri=0
        pointsincel=0

        povname = renpy.input("Avant de commencer, veuillez renseigner votre prénom ? Par défaut vous serez appelé Hector")
        povname = povname.strip()

        while povname=="moguri" or povname=="Moguri" or povname=="medoc" or povname=="Medoc" :
            povname = renpy.input("Pas Medoc ou Moguri svp")
            povname = povname.strip()
        if not povname:
            povname="Hector"


    menu:

        "Et du coup, masculin ou féminin ?"

        "Homme.":
            python:
                sex = "m"

        "Femme.":
            python:
                sex = "f"

    play music journeys
    scene school entrance

    with fade
    innerpov "OK."
    innerpov "C'est une journée comme les autres."
    innerpov "Aucun enjeu particulier."
    pov "Souffle."
    innerpov "Certes, c'est une académie d'élite, et je ne croiserai que les plus grands de ce pays."
    innerpov "Mais si je suis là, c'est que je l'ai mérité, non ?"
    innerpov "Personne ne me jugera, ils sont tous passés par là."
    innerpov "C'est une journée comme les autres."
    innerpov "..."
    innerpov "Je sais que c'est un mensonge."
    innerpov "C'est ma première journée à la Cosy Académie, un tournant dans ma vie."
    innerpov "Si je me plante je peux tout foutre en l'air..."
    innerpov "..."
    pov "Aaaaargh mais qu'est ce que je fais ic- !!"


    show Moguri Standard Badboy
    with flash

    "BOOONG!!!!!"

    pov "Hey !! Mais ça va pas de foncer dans les gens comme ç- !?"

    pov "Oh non...."
    pov "C'est Moguri..."
    pov "Mais s'il est ici, ça veut dire que..."

    hide Moguri
    show Medoc Standard Badboy
    with flash

    "BOOONG!!!!!"


    show Moguri Standard Badboy at right
    show Medoc Standard Badboy at left

    pov "C'est pas vrai..."
    pov "Medoc et Moguri. Dès mon premier jour, je tombe sur eux."
    pov "Littéralement en plus."
    pov "Moi qui voulais faire une rentrée à peu près discrète, c'est rapé."

    show Medoc Standard Degoute at left

    med "Dis donc, tu comptes nous fixer longtemps, comme ça ?"
    pov "Je... Non, bien sûr, excusez-moi, c'est juste que..."

    show Moguri BrasCroises Sourire at right

    if sex=="m":
        mog "Ahahah mais enfin Medoc, laisse-le ! Regarde comme il a l'air stressé !"
    else:
        mog "Ahahah mais enfin Medoc, laisse-la ! Regarde comme elle a l'air stressée !"

    show Moguri Standard Sourire at right



    if sex=="f":
        mog "Bienvenue à la Cosy Académie, gamine. Ne t'inquiète pas, on n'est pas tous aussi bourru que lui !"
        "Je suis presque sûre qu'on a le même âge, mais le fait qu'il m'appelle gamine ne me déplait pas particulièrement."
        pov "Aaaah, merci... Je tâcherai de me faire plus discrete, désolée !"
        mog "Mais non enfin ! Si tu es ici, c'est que tu as ta place. Aucune raison de se faire discrète !"
    else:
        mog "Bienvenue à la Cosy Académie, gamin. Ne t'inquiète pas, on n'est pas tous aussi bourru que lui !"
        "Je suis presque sûr qu'on a le même âge, mais le fait qu'il m'appelle gamin ne me déplait pas particulièrement."
        pov "Aaaah, merci... Je tâcherai de me faire plus discret, désolé !"
        mog "Mais non enfin ! Si tu es ici, c'est que tu as ta place. Aucune raison de se faire discret !"



    show Moguri BrasCroises Sourire at right

    mog "Sur ce... On va y aller, il s'agirait pas d'arriver en retard ! A plus tard p'tite tête !"

    hide Moguri
    pause 0.5
    hide Medoc 
    show Medoc Standard Degoute with fade

    med "Tch."
    med "Moguri a raison. Tout le monde n'est pas aussi bourru que moi..."
    med "Mais attention."
    show Medoc Standard Degoute at centerzoomed

    med "Tout le monde n'est pas aussi indulgent que lui..."

    pov "Gloups."

    pov "Ouch... Près... Très près. Trop près ?"
    pov "Pas vraiment."

    show Medoc Standard Degoute: 
        zoom 1.0 yoffset 0

    med "Allez. Fais attention à toi."

    hide Medoc with fade

    pov "Ouf."
    pov "Ca commence fort."
    pov "Même de dos ils sont impressionants..."
    pov "Aller, ça va le faire ! On y va !"

    window hide

    show intro at truecenter
    with animintro

    pause 3

    jump Meeting_Metalice

    return

