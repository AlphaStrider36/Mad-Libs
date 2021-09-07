from colorama import Fore
from colorama.initialise import init
init(autoreset=True)

while True:
    MAIN_Q = input(
        "Hello there! Welcome to Mad Libs! Press P to begin or Q to quit. ").lower()
    if MAIN_Q == 'q':
        quit()

    if MAIN_Q == 'p':
        print('''Select a topic:
1. Greetings, Earthlings
2. Be Kind
3. How To Wash Your Face
4. Abducted by Aliens
5. Popular Video Game
6. Old Macdonald
7. Drgons
8. The WallMart Difference
9. There Was An Old Woman
10. The Three Blind Mice
11. Yankee Doodle
12. The Cat And The Fiddle
13. The New Day
14. Sick Note
15. Nursery Rhyme
16. Romantic Poetry
17. Katie`s Kapers
18. Pizza Parlor
19. J.R.R Tolkien
20. Valentine`s Cards
21. Dictionary Disasters 1
22. Movie Quotes 1''')
    topic_selection = input(
        'Just write the number of the topic you want to play. ')

    if topic_selection == '1':
        lib1 = [
            input('NOUN (PLURAL) '),
            input('OCCUPATION '),
            input('ANIMAL (PLURAL) '),
            input('PLACE '),
            input('VERB '),
            input('NOUN ')
        ]
        print(f'In the book War of the {Fore.BLUE}{lib1[0]}{Fore.RESET}, the main character is an anonymous {Fore.BLUE}{lib1[1]}{Fore.RESET} who records the arrival of {Fore.BLUE}{lib1[2]}{Fore.BLUE} in {Fore.BLUE}{lib1[3]}{Fore.RESET}. Needless to say, havoc reigns as the {Fore.BLUE}{lib1[2]}{Fore.RESET} continue to {Fore.BLUE}{lib1[4]}{Fore.RESET} everything in sight, until they are killed by the common {Fore.BLUE}{lib1[5]}{Fore.RESET}.')

    elif topic_selection == '2':

        lib2 = [
            input("NOUN "),
            input("NOUN (PLURAL) "),
            input("NOUN "),
            input("PLACE "),
            input("ADJECTIVE "),
            input("NOUN ")
        ]
        print(f'Be kind to your {Fore.BLUE}{lib2[0]}{Fore.RESET}-footed {Fore.BLUE}{lib2[1]}{Fore.RESET} For a duck may be somebody`s {Fore.BLUE}{lib2[2]}{Fore.RESET}, Be kind to your {Fore.BLUE}{lib2[2]}{Fore.RESET} in {Fore.BLUE}{lib2[3]}{Fore.RESET} Where the weather is always {Fore.BLUE}{lib2[4]}{Fore.RESET}. You may think that this is the {Fore.BLUE}{lib2[5]}{Fore.RESET}, Well it is.')

    elif topic_selection == '3':
        lib3 = [
            input('ADVERB	'),
            input('NOUN '),
            input('LIQUID '),
            input('VERB '),
            input('NUMBER '),
            input('NOUN (PLURAL) '),
            input('VERB '),
            input('ADJECTIVE '),
            input('NOUN '),
            input('NOUN (PLURAL) '),
            input('ILLNESS '),
            input('OCCUPATION '),
            input('BODY PART (PLURAL) '),
            input('BODY PART ')
        ]
        print(f'In order to wash your face {Fore.BLUE}{lib3[0]}{Fore.RESET}, you must wet your {Fore.BLUE}{lib3[1]}{Fore.RESET} in warm {Fore.BLUE}{lib3[2]}{Fore.RESET}. Then, {Fore.BLUE}{lib3[3]}{Fore.RESET} it across your face {Fore.BLUE}{lib3[4]}{Fore.RESET} times. This will wash off any remainig {Fore.BLUE}{lib3[5]}{Fore.RESET}. When you are done you should {Fore.BLUE}{lib3[6]}{Fore.RESET} the cloth in {Fore.BLUE}{lib3[7]}{Fore.RESET} water to clean it. You should also wash your face with a {Fore.BLUE}{lib3[8]}{Fore.RESET} to keep it smooth and shiny. This will keep also keep away {Fore.BLUE}{lib3[9]}{Fore.RESET}. Don`t worry. It is normal to experience {Fore.BLUE}{lib3[10]}{Fore.RESET} the first time you try this. Consult your {Fore.BLUE}{lib3[11]}{Fore.RESET} if you break out in {Fore.BLUE}{lib3[12]}{Fore.RESET}. This works well on your {Fore.BLUE}{lib3[13]}{Fore.RESET} too!')

    elif topic_selection == '4':
        lib4 = [
            input('VERB ENDING IN "ING" '),
            input('VERB ENDING IN "ED" '),
            input('VERB ENDING IN "ED" '),
            input('NOUN '), input('VERB '),
            input('ANIMAL '),
            input('NOUN '),
            input('NOUN '),
            input('NOUN '),
            input('PLACE '),
            input('NUMBER ')
        ]
        print(f'I was {Fore.BLUE}{lib4[0]}{Fore.RESET} along the sidewalk when an alien {Fore.BLUE}{lib4[1]}{Fore.RESET} me. I was {Fore.BLUE}{lib4[2]}{Fore.RESET} into their {Fore.BLUE}{lib4[3]}{Fore.RESET} and it blasted off. Then the alien asked me to {Fore.BLUE}{lib4[4]}{Fore.RESET} on the TV. I was suprised they spoke english. the aliens had a pet {Fore.BLUE}{lib4[5]}{Fore.RESET}. We ordered a {Fore.BLUE}{lib4[6]}{Fore.RESET} and it tasted good. As we came back into the galaxy, one alien asked me if I wanted a {Fore.BLUE}{lib4[7]}{Fore.RESET}. I said no but I would like a {Fore.BLUE}{lib4[8]}{Fore.RESET}. He got it for me and then dropped me off at my {Fore.BLUE}{lib4[9]}{Fore.RESET}. Then I realized I had been gone for {Fore.BLUE}{lib4[10]}{Fore.RESET} years! ')

    elif topic_selection == '5':
        lib5 = [
            input('VERB '),
            input('ADJECTIVE '),
            input('SILLY WORD '),
            input('NUMBER '),
            input('NOUN '),
            input('ADJECTIVE '),
            input('NOUN '),
            input('OCCUPATION '),
            input('AMOUNT OF TIME '),
            input('VERB '),
            input('PLACE '),
            input('VERB ENDING IN "ED" '),
            input('NOUN (PLURAL) '),
            input('ADJECTIVE '),
            input('VERB ENDING IN "ING" '),
            input('VERB ')
        ]
        print(f'Good morning, Mr. Hunt. Your mission, should you choose to {Fore.BLUE}{lib5[0]}{Fore.RESET} it, involves the recovery of a {Fore.BLUE}{lib5[1]}{Fore.RESET} item designated "{Fore.BLUE}{lib5[2]}{Fore.RESET}." You may select any {Fore.BLUE}{lib5[3]}{Fore.RESET} {Fore.BLUE}{lib5[4]}{Fore.RESET}, but it is {Fore.BLUE}{lib5[5]}{Fore.RESET} that the third member of your {Fore.BLUE}{lib5[4]}{Fore.RESET} be Nyah Nordoff-Hall. She is a {Fore.BLUE}{lib5[5]}{Fore.RESET}, and a highly capable professional {Fore.BLUE}{lib5[6]}{Fore.RESET}. You have {Fore.BLUE}{lib5[7]}{Fore.RESET} to {Fore.BLUE}{lib5[8]}{Fore.RESET} Miss Hall and meet me in {Fore.BLUE}{lib5[9]}{Fore.RESET} to receive your assignment. As always, should any member of your {Fore.BLUE}{lib5[4]}{Fore.RESET} be caught or {Fore.BLUE}{lib5[10]}{Fore.RESET}, the {Fore.BLUE}{lib5[11]}{Fore.RESET} will disavow all knowledge of your {Fore.BLUE}{lib5[12]}{Fore.RESET}. And Mr. Hunt, the next time you go on holiday, please be {Fore.BLUE}{lib5[13]}{Fore.RESET} enough to let us know where you`re {Fore.BLUE}{lib5[14]}{Fore.RESET}. This message will self-{Fore.BLUE}{lib5[15]}{Fore.RESET} in five seconds.')

    elif topic_selection == '6':
        lib6 = [
            input('ADJECTIVE '),
            input('NOUN '),
            input('ANIMAL '),
            input('NOISE ')
        ]
        print(f'{Fore.BLUE}{lib6[0]}{Fore.RESET} Macdonald had a {Fore.BLUE}{lib6[1]}{Fore.RESET}, E-I-E-I-O and on that {Fore.BLUE}{lib6[1]}{Fore.RESET} he had a {Fore.BLUE}{lib6[2]}{Fore.RESET}, E-I-E-I-O with a {Fore.BLUE}{lib6[3]}{Fore.RESET} {Fore.BLUE}{lib6[3]}{Fore.RESET} here and a {Fore.BLUE}{lib6[3]}{Fore.RESET} {Fore.BLUE}{lib6[3]}{Fore.RESET} there, here a {Fore.BLUE}{lib6[3]}{Fore.RESET}, there a {Fore.BLUE}{lib6[3]}{Fore.RESET}, everywhere a {Fore.BLUE}{lib6[3]}{Fore.RESET} {Fore.BLUE}{lib6[3]}{Fore.RESET}, {Fore.BLUE}{lib6[0]}{Fore.RESET} Macdonald had a {Fore.BLUE}{lib6[1]}{Fore.RESET}, E-I-E-I-O.')

    elif topic_selection == '7':
        lib7 = [
            input('COLOR '),
            input('SUPERLATIVE (ENDING IS "EST") '),
            input('ADJECTIVE '),
            input('BODY PART (PLURAL) '),
            input('BODY PART '),
            input('NOUN '),
            input('ANIMAL (PLURAL) '),
            input('ADJECTIVE '),
            input('ADJECTIVE '),
            input('ADJECTIVE ')
        ]
        print(f'The {Fore.BLUE}{lib7[0]}{Fore.RESET} Dragon is the {Fore.BLUE}{lib7[1]}{Fore.RESET} Dragon of all. It has {Fore.BLUE}{lib7[2]}{Fore.RESET} {Fore.BLUE}{lib7[3]}{Fore.RESET}, and a/an {Fore.BLUE}{lib7[4]}{Fore.RESET} shaped like a/an {Fore.BLUE}{lib7[5]}{Fore.RESET}. It loves to eat {Fore.BLUE}{lib7[6]}{Fore.RESET}, although it will feast on nearly anything. It is {Fore.BLUE}{lib7[7]}{Fore.RESET} and {Fore.BLUE}{lib7[8]}{Fore.RESET}. You must be {Fore.BLUE}{lib7[9]}{Fore.RESET} around it, or you may end up as it`s meal!')

    elif topic_selection == '8':
        lib8 = [
            input('VERB '),
            input('ADJECTIVE '),
            input('NOUN (PLURAL) '),
            input('ADJECTIVE '),
            input('VERB ENDING IN "ING" '),
            input('VERB '),
            input('NUMBER '),
            input('ADJECTIVE '),
            input('NOUN (PLURAL) '),
            input('NOUN (PLURAL) '),
            input('NOUN (PLURAL) '),
            input('RELATIVE (PLURAL) '),
            input('ADJECTIVE '),
            input('ADJECTIVE '),
            input('NOUN (PLURAL) ')
        ]
        print(f'Come {Fore.BLUE}{lib8[0]}{Fore.RESET} at WALMART, where you`ll receive {Fore.BLUE}{lib8[1]}{Fore.RESET} discounts on all of your favorite brand name {Fore.BLUE}{lib8[2]}{Fore.RESET}. Our {Fore.BLUE}{lib8[3]}{Fore.RESET} and {Fore.BLUE}{lib8[4]}{Fore.RESET} associates are there to {Fore.BLUE}{lib8[5]}{Fore.RESET} you {Fore.BLUE}{lib8[6]}{Fore.RESET} hours a day. Here you will find {Fore.BLUE}{lib8[7]}{Fore.RESET} prices on the {Fore.BLUE}{lib8[8]}{Fore.RESET} you need. {Fore.BLUE}{lib8[9]}{Fore.RESET} for the moms, {Fore.BLUE}{lib8[10]}{Fore.RESET} for the kids and all the latest electronics for the {Fore.BLUE}{lib8[11]}{Fore.RESET}. So come on down to your {Fore.BLUE}{lib8[12]}{Fore.RESET} {Fore.BLUE}{lib8[13]}{Fore.RESET} WALMART where the {Fore.BLUE}{lib8[14]}{Fore.RESET} come first.')

    elif topic_selection == '9':
        lib9 = [
            input('ADJECTIVE '),
            input('NOUN '),
            input('NOUN (PLURAL) '),
            input('NOUN '),
            input('VERB ENDING IN "ED" ')
        ]
        print(f'There was a/an {Fore.BLUE}{lib9[0]}{Fore.RESET} woman who lived in a/an {Fore.BLUE}{lib9[1]}{Fore.RESET}. She had so many {Fore.BLUE}{lib9[2]}{Fore.RESET} she didn`t know what to do. She gave them some broth without any {Fore.BLUE}{lib9[3]}{Fore.RESET}. She {Fore.BLUE}{lib9[4]}{Fore.RESET} them all soundly and put them to bed.')

    elif topic_selection == '10':
        lib10 = [
            input('NUMBER '),
            input('ADJECTIVE '),
            input('VERB '),
            input('OCCUPATION '),
            input('RELATION '),
            input('BODY PART (PLURAL) '),
            input('VERB ENDING IN "ING" '),
            input('NOUN ')
        ]
        print(f'{Fore.BLUE}{lib10[0]}{Fore.RESET} {Fore.BLUE}{lib10[1]}{Fore.RESET} mice! See how they {Fore.BLUE}{lib10[2]}{Fore.RESET}! They all ran after the {Fore.BLUE}{lib10[3]}{Fore.RESET}`s {Fore.BLUE}{lib10[4]}{Fore.RESET}, Who cut off their {Fore.BLUE}{lib10[5]}{Fore.RESET} with a {Fore.BLUE}{lib10[6]}{Fore.RESET} knife. Did you ever see such a thing in your {Fore.BLUE}{lib10[7]}{Fore.RESET} As {Fore.BLUE}{lib10[0]}{Fore.RESET} {Fore.BLUE}{lib10[1]}{Fore.RESET} mice?')

    elif topic_selection == '11':
        lib11 = [
            input('NOUN '),
            input('VERB ENDING IN "ING" '),
            input('ANIMAL '),
            input('ARTICLE OF CLOTHING '),
            input('NOUN (PLURAL) '),
            input('ADJECTIVE '),
            input('NOUN '),
            input('NOUN (PLURAL) ')
        ]
        print(f'Yankee Doodle went to {Fore.BLUE}{lib11[0]}{Fore.RESET}, a-{Fore.BLUE}{lib11[1]}{Fore.RESET} on a {Fore.BLUE}{lib11[2]}{Fore.RESET}; Stuck a feather in his {Fore.BLUE}{lib11[3]}{Fore.RESET} and called it {Fore.BLUE}{lib11[4]}{Fore.RESET}. Yankee Doodle keep it up, Yankee Doodle {Fore.BLUE}{lib11[5]}{Fore.RESET}, Mind the {Fore.BLUE}{lib11[6]}{Fore.RESET} and the step and with the {Fore.BLUE}{lib11[7]}{Fore.RESET} be handy.')

    elif topic_selection == '12':
        lib12 = [
            input('SILLY WORD '),
            input('ANIMAL'),
            input('MUSICAL INSTRUMENT '),
            input('NOUN '),
            input('ADJECTIVE '),
            input('NOUN ')
        ]
        print(f'Hey, {Fore.BLUE}{lib12[0]}{Fore.RESET}, {Fore.BLUE}{lib12[0]}{Fore.RESET}! The {Fore.BLUE}{lib12[1]}{Fore.RESET} and the {Fore.BLUE}{lib12[2]}{Fore.RESET}, The cow jumped over the {Fore.BLUE}{lib12[3]}{Fore.RESET}; The {Fore.BLUE}{lib12[4]}{Fore.RESET} dog laughed To see such sport, And the {Fore.BLUE}{lib12[5]}{Fore.RESET} ran away with the spoon.')

    elif topic_selection == '13':
        q124 = input('VERB ENDING IN ING ')
        q125 = input('VERB ENDING IN ING ')
        q126 = input('VERB ENDING IN ED ')
        q127 = input('PLACE ')
        q128 = input('VERB ')
        q129 = input('VERB ')
        print(f'Tommorrow is a new day full of new suprises and new adventures. Such as {Fore.BLUE}{q124}{Fore.RESET} and {Fore.BLUE}{q125}{Fore.RESET}. Tommorrow leads you to the life you haven`t {Fore.BLUE}{q126}{Fore.RESET} yet. So why not plan to live today with the most adventurious and positive outlook because today is yesterday`s tommorrow and we all know that it`s good to do things differently. So let`s go to {Fore.BLUE}{q127}{Fore.RESET} and {Fore.BLUE}{q128}{Fore.RESET} with someone cool. Or you could just let it {Fore.BLUE}{q129}{Fore.RESET} right by.')

    elif topic_selection == '14':
        q130 = input('SILLY WORD ')
        q131 = input('LAST NAME ')
        q132 = input('ILLNESS ')
        q133 = input('NOUN (PLURAL) ')
        q134 = input('ADJECTIVE ')
        q135 = input('ADJECTIVE ')
        q136 = input('SILLY WORD ')
        q137 = input('PLACE ')
        q138 = input('NUMBER ')
        q149 = input('ADJECTIVE ')
        print(f'Dear School Nurse: {Fore.BLUE}{q130}{Fore.RESET} {Fore.BLUE}{q131}{Fore.RESET} will not be attending school today. He/she has come down with a case of {Fore.BLUE}{q132}{Fore.RESET} and has horrible {Fore.BLUE}{q133}{Fore.RESET} and a/an {Fore.BLUE}{q134}{Fore.RESET} fever. We have made an appointment with the {Fore.BLUE}{q135}{Fore.RESET} Dr. {Fore.BLUE}{q136}{Fore.RESET}, who studied for many years in {Fore.BLUE}{q137}{Fore.RESET} and has 5 degrees in pediatrics. He will send you all the information you need. Thank you! Sincerely Mrs. {Fore.BLUE}{q138}{Fore.RESET}.')

    elif topic_selection == '15':
        q150 = input('GIRL`S NAME ')
        q151 = input('ANIMAL ')
        q152 = input('COLOR ')
        q153 = input('PLACE ')
        q154 = input('VERB ')
        print(f'{Fore.BLUE}{q150}{Fore.RESET} had a little {Fore.BLUE}{q151}{Fore.RESET} little {Fore.BLUE}{q151}{Fore.RESET} little {Fore.BLUE}{q151}{Fore.RESET}, {Fore.BLUE}{q150}{Fore.RESET} had a little {Fore.BLUE}{q151}{Fore.RESET}, it`s fleece was {Fore.BLUE}{q152}{Fore.RESET} as snow. It followed her to {Fore.BLUE}{q153}{Fore.RESET} one day, {Fore.BLUE}{q153}{Fore.RESET} one day, {Fore.BLUE}{q153}{Fore.RESET} one day, it made the children {Fore.BLUE}{q154}{Fore.RESET} and play to see a {Fore.BLUE}{q151}{Fore.RESET} at {Fore.BLUE}{q153}{Fore.RESET}')

    elif topic_selection == '16':
        q154 = input('COLOR ')
        q155 = input('NOUN (PLURAL) ')
        q156 = input('NOUN ')
        q157 = input('ADJECTIVE ')
        print(f'Roses are {Fore.BLUE}{q154}{Fore.RESET}, {Fore.BLUE}{q155}{Fore.RESET} are blue, {Fore.BLUE}{q156}{Fore.RESET} is {Fore.BLUE}{q157}{Fore.RESET}, and so are you.')

    elif topic_selection == '17':
        q158 = input('VERB ENDING IN "ING" ')
        q159 = input('NOUN ')
        q160 = input('PART OF THE BODY ')
        q161 = input('VERB ')
        q162 = input('ANIMAL')
        q163 = input('VERB ENDING IN "ED" ')
        print(f'I was {Fore.BLUE}{q158}{Fore.RESET} down the hallway and some {Fore.BLUE}{q159}{Fore.RESET} grabbed my {Fore.BLUE}{q160}{Fore.RESET}, and I turned to him and said "so help me, if you {Fore.BLUE}{q161}{Fore.RESET} me again you will go the way of the {Fore.BLUE}{q162}{Fore.RESET}." And then he {Fore.BLUE}{q163}{Fore.RESET} away.')

    elif topic_selection == '18':
        q162 = input('MALE NAME ')
        q163 = input('ADJECTIVE ')
        q164 = input('NOUN ')
        q165 = input('ADJECTIVE ')
        q166 = input('FOOD (PLURAL) ')
        q167 = input('NOUN (PLURAL) ')
        q168 = input('VERB ENDING IN "ED" ')
        q169 = input('LIQUID ')
        q170 = input('NOUN ')
        print(f'Come on over to {Fore.BLUE}{q162}{Fore.RESET}`s Pizza Parlor where you can enjoy you favorite {Fore.BLUE}{q163}{Fore.RESET}-dish pizza`s. You can try our famous {Fore.BLUE}{q164}{Fore.RESET}-lovers pizza, or select from our list of {Fore.BLUE}{q165}{Fore.RESET} toppings, including sauteed {Fore.BLUE}{q166}{Fore.RESET}, {Fore.BLUE}{q167}{Fore.RESET}, and many more. Our crusts are hand-{Fore.BLUE}{q168}{Fore.RESET} and basted in {Fore.BLUE}{q169}{Fore.RESET} to make them seem more {Fore.BLUE}{q170}{Fore.RESET}-made.')

    elif topic_selection == '19':
        q171 = input('FRUIT ')
        q172 = input('NOUN (PLURAL) ')
        q173 = input('NOUN ')
        q174 = input('NOUN ')
        q175 = input('NOUN (PLURAL) ')
        q176 = input('NOUN ')
        q177 = input('SILLY WORD ')
        print(f'J.R.R. Tolkien has been thrust into the {Fore.BLUE}{q171}{Fore.RESET}-light yet again with the release of his famous trilogy Lord of the {Fore.BLUE}{q172}{Fore.RESET} as a {Fore.BLUE}{q173}{Fore.RESET} series. The three books, {Fore.BLUE}{q174}{Fore.RESET} of the Ring, The Two {Fore.BLUE}{q175}{Fore.RESET}, and Return of the {Fore.BLUE}{q176}{Fore.RESET}, are preceded by another book The {Fore.BLUE}{q177}{Fore.RESET}, which may also be filmed later on.')

    elif topic_selection == '20':
        q178 = input('NOUN ')
        q179 = input('NOUN (PLURAL)')
        q180 = input('ADJECTIVE ')
        q181 = input('VERB ')
        q182 = input('NOUN (PLURAL) ')
        q183 = input('COLOR ')
        q184 = input('BODY PART ')
        print(f'Be my {Fore.RESET}{q178}{Fore.RESET} {Fore.BLUE}{q179}{Fore.RESET} make the world go {Fore.BLUE}{q180}{Fore.RESET} Pickachu says "I {Fore.BLUE}{q181}{Fore.RESET} you" I love {Fore.BLUE}{q182}{Fore.RESET}, {Fore.BLUE}{q183}{Fore.RESET} does too You make my {Fore.BLUE}{q184}{Fore.RESET} flutter')

    elif topic_selection == '21':
        q185 = input('ADJECTIVE ')
        q186 = input('NOUN ')
        q187 = input('BODY PART (PLURAL) ')
        q188 = input('NOUN ')
        q189 = input('VERB ENDING IN "ED" ')
        q190 = input('VERB ENDING IN "ING" ')
        q191 = input('NOUN (PLURAL) ')
        q192 = input('NOUN (PLURAL) ')
        q193 = input('NOUN (PLURAL) ')
        q194 = input('NOUN ')
        q195 = input('NOUN ')
        print(f'''Xanthochroid: 
Adj. Having a/an {Fore.BLUE}{q185}{Fore.RESET} {Fore.BLUE}{q186}{Fore.RESET} and light {Fore.BLUE}{q187}{Fore.RESET}.
N. A/An {Fore.BLUE}{q188}{Fore.RESET} having a/an {Fore.BLUE}{q185}{Fore.RESET} {Fore.BLUE}{q186}{Fore.RESET} and light {Fore.BLUE}{q187}{Fore.RESET}. Obdurate
Adj. {Fore.BLUE}{q189}{Fore.RESET} against feeling; {Fore.BLUE}{q189}{Fore.RESET} in {Fore.BLUE}{q190}{Fore.RESET} or wickedness; not giving in to {Fore.BLUE}{q191}{Fore.RESET}; showing unfeeling {Fore.BLUE}{q192}{Fore.RESET} to tender {Fore.BLUE}{q193}{Fore.RESET}. Affuage
N. The right to cut {Fore.BLUE}{q194}{Fore.RESET} in a {Fore.BLUE}{q195}{Fore.RESET} for a family fire.''')
    elif topic_selection == '22':
        q196 = input