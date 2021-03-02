import colorama
from colorama import Fore
from colorama.initialise import init
colorama.init(autoreset=True)

bc = Fore.BLUE
r = Fore.RESET

q1 = input("Hello there! Welcome to Mad Libs! Press P to begin or Q to quit. ")
if q1 == 'q' or 'Q':
    quit

if q1 == 'p' or 'P':
    print('Select a topic:')
    print('1. Greetings, Earthlings')
    print('2. Be Kind')
    print('3. How To Wash Your Face')
    print('4. Abducted by Aliens')
    print('5. Popular Video Game')
    print('6. Old Macdonald')
    print('7. Drgons')
    print('8. The WallMart Difference ')
    print('9. There Was An Old Woman')
    print('10. The Three Blind Mice')
    print('11. Yankee Doodle')
    print('12. The Cat And The Fiddle')
    print('13. The New Day')
    print('14. Sick Note')
    print('15. Nursery Rhyme')
    print('16. Romantic Poetry')
    print('17. Katie`s Kapers')
    print('18. Pizza Parlor')
    print('19. J.R.R Tolkien')
    print('20. Valentine`s Cards')

q2 = input('Just write the number of the topic you want to play. ')

while q2 == '1':
    q3 = [input('NOUN (PLURAL) '), input('OCCUPATION '), input(
        'ANIMAL (PLURAL) '), input('PLACE '), input('VERB '), input('NOUN ')]
    print(f'In the book War of the {Fore.BLUE}{q3[0]}{Fore.RESET}, the main character is an anonymous {Fore.BLUE}{q3[1]}{Fore.RESET} who records the arrival of {Fore.BLUE}{q3[2]}{Fore.BLUE} in {Fore.BLUE}{q3[3]}{Fore.RESET}. Needless to say, havoc reigns as the {Fore.BLUE}{q3[2]}{Fore.RESET} continue to {Fore.BLUE}{q3[4]}{Fore.RESET} everything in sight, until they are killed by the common {Fore.BLUE}{q3[5]}{Fore.RESET}.')

while q2 == '2':
    q4 = [input("NOUN "), input("NOUN (PLURAL) "), input("NOUN "), input(
        "PLACE "), input("ADJECTIVE "), input("NOUN ")]
    print(f'Be kind to your {Fore.BLUE}{q4[0]}{Fore.RESET}-footed {Fore.BLUE}{q4[1]}{Fore.RESET} For a duck may be somebody`s {Fore.BLUE}{q4[2]}{Fore.RESET}, Be kind to your {Fore.BLUE}{q4[2]}{Fore.RESET} in {Fore.BLUE}{q4[3]}{Fore.RESET} Where the weather is always {Fore.BLUE}{q4[4]}{Fore.RESET}. You may think that this is the {Fore.BLUE}{q4[5]}{Fore.RESET}, Well it is.')

while q2 == '3':
    q5 = [input('ADVERB	'), input('NOUN '), input('LIQUID '), input('VERB '), input('NUMBER	'), input('NOUN (PLURAL) '), input('VERB '), input(
        'ADJECTIVE '), input('NOUN '), input('NOUN (PLURAL) '), input('ILLNESS '), input('OCCUPATION '), input('BODY PART (PLURAL) '), input('BODY PART ')]
    print(f'In order to wash your face {Fore.BLUE}{q5[0]}{Fore.RESET}, you must wet your {Fore.BLUE}{q5[1]}{Fore.RESET} in warm {Fore.BLUE}{q5[2]}{Fore.RESET}. Then, {Fore.BLUE}{q5[3]}{Fore.RESET} it across your face {Fore.BLUE}{q5[4]}{Fore.RESET} times. This will wash off any remainig {Fore.BLUE}{q5[5]}{Fore.RESET}. When you are done you should {Fore.BLUE}{q5[6]}{Fore.RESET} the cloth in {Fore.BLUE}{q5[7]}{Fore.RESET} water to clean it. You should also wash your face with a {Fore.BLUE}{q5[8]}{Fore.RESET} to keep it smooth and shiny. This will keep also keep away {Fore.BLUE}{q5[9]}{Fore.RESET}. Don`t worry. It is normal to experience {Fore.BLUE}{q5[10]}{Fore.RESET} the first time you try this. Consult your {Fore.BLUE}{q5[11]}{Fore.RESET} if you break out in {Fore.BLUE}{q5[12]}{Fore.RESET}. This works well on your {Fore.BLUE}{q5[13]}{Fore.RESET} too!')

while q2 == '4':
    q6 = [input('VERB ENDING IN "ING" '), input('VERB ENDING IN "ED" '), input('VERB ENDING IN "ED" '), input('NOUN '), input(
        'VERB '), input('ANIMAL '), input('NOUN '), input('NOUN '), input('NOUN '), input('PLACE '), input('NUMBER ')]
    print(f'I was {Fore.BLUE}{q5[0]}{Fore.RESET} along the sidewalk when an alien {Fore.BLUE}{q5[1]}{Fore.RESET} me. I was {Fore.BLUE}{q5[2]}{Fore.RESET} into their {Fore.BLUE}{q5[3]}{Fore.RESET} and it blasted off. Then the alien asked me to {Fore.BLUE}{q5[4]}{Fore.RESET} on the TV. I was suprised they spoke english. the aliens had a pet {Fore.BLUE}{q5[5]}{Fore.RESET}. We ordered a {Fore.BLUE}{q5[6]}{Fore.RESET} and it tasted good. As we came back into the galaxy, one alien asked me if I wanted a {Fore.BLUE}{q5[7]}{Fore.RESET}. I said no but I would like a {Fore.BLUE}{q5[8]}{Fore.RESET}. He got it for me and then dropped me off at my {Fore.BLUE}{q5[9]}{Fore.RESET}. Then I realized I had been gone for {Fore.BLUE}{q5[10]}{Fore.RESET} years! ')

while q2 == '5':
    q7 = [input('VERB '), input('ADJECTIVE '), input('SILLY WORD '), input('NUMBER '), input('NOUN '), input('ADJECTIVE '), input('NOUN '), input('OCCUPATION '), input(
        'AMOUNT OF TIME '), input('VERB '), input('PLACE '), input('VERB ENDING IN "ED" '), input('NOUN (PLURAL) '), input('ADJECTIVE '), input('VERB ENDING IN "ING" '), input('VERB ')]
print(f'Good morning, Mr. Hunt. Your mission, should you choose to {Fore.BLUE}{q7[0]}{Fore.RESET} it, involves the recovery of a {Fore.BLUE}{q7[1]}{Fore.RESET} item designated "{Fore.BLUE}{q7[2]}{Fore.RESET}." You may select any {Fore.BLUE}{q7[3]}{Fore.RESET} {Fore.BLUE}{q7[4]}{Fore.RESET}, but it is {Fore.BLUE}{q7[5]}{Fore.RESET} that the third member of your {Fore.BLUE}{q7[4]}{Fore.RESET} be Nyah Nordoff-Hall. She is a {Fore.BLUE}{q7[5]}{Fore.RESET}, and a highly capable professional {Fore.BLUE}{q7[6]}{Fore.RESET}. You have {Fore.BLUE}{q7[7]}{Fore.RESET} to {Fore.BLUE}{q7[8]}{Fore.RESET} Miss Hall and meet me in {Fore.BLUE}{q7[9]}{Fore.RESET} to receive your assignment. As always, should any member of your {Fore.BLUE}{q7[4]}{Fore.RESET} be caught or {Fore.BLUE}{q7[10]}{Fore.RESET}, the {Fore.BLUE}{q7[11]}{Fore.RESET} will disavow all knowledge of your {Fore.BLUE}{q7[12]}{Fore.RESET}. And Mr. Hunt, the next time you go on holiday, please be {Fore.BLUE}{q7[13]}{Fore.RESET} enough to let us know where you`re {Fore.BLUE}{q7[14]}{Fore.RESET}. This message will self-{Fore.BLUE}{q7[15]}{Fore.RESET} in five seconds.')

# topic 6

while q2 == '6':
    q62 = input('ADJECTIVE ')
    q63 = input('NOUN ')
    q64 = input('ANIMAL ')
    q65 = input('NOISE ')
    print(f'{Fore.BLUE}{q62}{Fore.RESET} Macdonald had a {Fore.BLUE}{q63}{Fore.RESET}, E-I-E-I-O and on that {Fore.BLUE}{q63}{Fore.RESET} he had a {Fore.BLUE}{q64}{Fore.RESET}, E-I-E-I-O with a {Fore.BLUE}{q65}{Fore.RESET} {Fore.BLUE}{q65}{Fore.RESET} here and a {Fore.BLUE}{q65}{Fore.RESET} {Fore.BLUE}{q65}{Fore.RESET} there, here a {Fore.BLUE}{q65}{Fore.RESET}, there a {Fore.BLUE}{q65}{Fore.RESET}, everywhere a {Fore.BLUE}{q65}{Fore.RESET} {Fore.BLUE}{q65}{Fore.RESET}, {Fore.BLUE}{q62}{Fore.RESET} Macdonald had a {Fore.BLUE}{q63}{Fore.RESET}, E-I-E-I-O.')

# topic 7

while q2 == '7':
    q67 = input('COLOR ')
    q68 = input('SUPERLATIVE (ENDING IS "EST") ')
    q69 = input('ADJECTIVE ')
    q70 = input('BODY PART (PLURAL) ')
    q71 = input('BODY PART ')
    q72 = input('NOUN ')
    q73 = input('ANIMAL (PLURAL) ')
    q74 = input('ADJECTIVE ')
    q75 = input('ADJECTIVE ')
    q76 = input('ADJECTIVE ')
    print(f'The {Fore.BLUE}{q67}{Fore.RESET} Dragon is the {Fore.BLUE}{q68}{Fore.RESET} Dragon of all. It has {Fore.BLUE}{q69}{Fore.RESET} {Fore.BLUE}{q70}{Fore.RESET}, and a/an {Fore.BLUE}{q71}{Fore.RESET} shaped like a/an {Fore.BLUE}{q72}{Fore.RESET}. It loves to eat {Fore.BLUE}{q73}{Fore.RESET}, although it will feast on nearly anything. It is {Fore.BLUE}{q74}{Fore.RESET} and {Fore.BLUE}{q75}{Fore.RESET}. You must be {Fore.BLUE}{q76}{Fore.RESET} around it, or you may end up as it`s meal!')

# topic 8

while q2 == '8':
    q78 = input('VERB ')
    q79 = input('ADJECTIVE ')
    q80 = input('NOUN (PLURAL) ')
    q81 = input('ADJECTIVE ')
    q82 = input('VERB ENDING IN "ING" ')
    q83 = input('VERB ')
    q84 = input('NUMBER	')
    q85 = input('ADJECTIVE ')
    q86 = input('NOUN (PLURAL) ')
    q87 = input('NOUN (PLURAL) ')
    q88 = input('NOUN (PLURAL) ')
    q89 = input('RELATIVE (PLURAL) ')
    q90 = input('ADJECTIVE ')
    q91 = input('ADJECTIVE ')
    q92 = input('NOUN (PLURAL) ')
    print(f'Come {Fore.BLUE}{q78}{Fore.RESET} at WALMART, where you`ll receive {Fore.BLUE}{q79}{Fore.RESET} discounts on all of your favorite brand name {Fore.BLUE}{q80}{Fore.RESET}. Our {Fore.BLUE}{q81}{Fore.RESET} and {Fore.BLUE}{q82}{Fore.RESET} associates are there to {Fore.BLUE}{q83}{Fore.RESET} you {Fore.BLUE}{q84}{Fore.RESET} hours a day. Here you will find {Fore.BLUE}{q85}{Fore.RESET} prices on the {Fore.BLUE}{q86}{Fore.RESET} you need. {Fore.BLUE}{q87}{Fore.RESET} for the moms, {Fore.BLUE}{q88}{Fore.RESET} for the kids and all the latest electronics for the {Fore.BLUE}{q89}{Fore.RESET}. So come on down to your {Fore.BLUE}{q90}{Fore.RESET} {Fore.BLUE}{q91}{Fore.RESET} WALMART where the {Fore.BLUE}{q92}{Fore.RESET} come first.')

# topic 9

while q2 == '9':
    q94 = input('ADJECTIVE ')
    q95 = input('NOUN ')
    q96 = input('NOUN (PLURAL) ')
    q97 = input('NOUN ')
    q98 = input('VERB ENDING IN "ED" ')
    print(f'There was a/an {Fore.BLUE}{q94}{Fore.RESET} woman who lived in a/an {Fore.BLUE}{q95}{Fore.RESET}. She had so many {Fore.BLUE}{q96}{Fore.RESET} she didn`t know what to do. She gave them some broth without any {Fore.BLUE}{q97}{Fore.RESET}. She {Fore.BLUE}{q98}{Fore.RESET} them all soundly and put them to bed.')

# topic 10

while q2 == '10':
    q100 = input('NUMBER ')
    q101 = input('ADJECTIVE ')
    q102 = input('VERB ')
    q103 = input('OCCUPATION ')
    q104 = input('RELATION ')
    q105 = input('BODY PART (PLURAL) ')
    q106 = input('VERB ENDING IN "ING" ')
    q107 = input('NOUN ')
    print(f'{Fore.BLUE}{q100}{Fore.RESET} {Fore.BLUE}{q101}{Fore.RESET} mice! See how they {Fore.BLUE}{q102}{Fore.RESET}! They all ran after the {Fore.BLUE}{q103}{Fore.RESET}`s {Fore.BLUE}{q104}{Fore.RESET}, Who cut off their {Fore.BLUE}{q105}{Fore.RESET} with a {Fore.BLUE}{q106}{Fore.RESET} knife. Did you ever see such a thing in your {Fore.BLUE}{q107}{Fore.RESET} As {Fore.BLUE}{q100}{Fore.RESET} {Fore.BLUE}{q101}{Fore.RESET} mice?')


while q2 == '11':
    q109 = input('NOUN ')
    q110 = input('VERB ENDING IN "ING" ')
    q111 = input('ANIMAL ')
    q112 = input('ARTICLE OF CLOTHING ')
    q113 = input('NOUN (PLURAL) ')
    q114 = input('ADJECTIVE ')
    q115 = input('NOUN ')
    q116 = input('NOUN (PLURAL)	')
    print(f'Yankee Doodle went to {Fore.BLUE}{q109}{Fore.RESET}, a-{Fore.BLUE}{q110}{Fore.RESET} on a {Fore.BLUE}{q111}{Fore.RESET}; Stuck a feather in his {Fore.BLUE}{q112}{Fore.RESET} and called it {Fore.BLUE}{q113}{Fore.RESET}. Yankee Doodle keep it up, Yankee Doodle {Fore.BLUE}{q114}{Fore.RESET}, Mind the {Fore.BLUE}{q115}{Fore.RESET} and the step and with the {Fore.BLUE}{q116}{Fore.RESET} be handy.')

# topic 12

while q2 == '12':
    q118 = input('SILLY WORD ')
    q119 = input('ANIMAL')
    q120 = input('MUSICAL INSTRUMENT ')
    q121 = input('NOUN ')
    q122 = input('ADJECTIVE ')
    q123 = input('NOUN ')
    print(f'Hey, {Fore.BLUE}{q118}{Fore.RESET}, {Fore.BLUE}{q118}{Fore.RESET}! The {Fore.BLUE}{q119}{Fore.RESET} and the {Fore.BLUE}{q120}{Fore.RESET}, The cow jumped over the {Fore.BLUE}{q121}{Fore.RESET}; The {Fore.BLUE}{q122}{Fore.RESET} dog laughed To see such sport, And the {Fore.BLUE}{q123}{Fore.RESET} ran away with the spoon.')

# topic 13

while q2 == '13':
    q124 = input('VERB ENDING IN ING ')
    q125 = input('VERB ENDING IN ING ')
    q126 = input('VERB ENDING IN ED ')
    q127 = input('PLACE ')
    q128 = input('VERB ')
    q129 = input('VERB ')
    print(f'Tommorrow is a new day full of new suprises and new adventures. Such as {Fore.BLUE}{q124}{Fore.RESET} and {Fore.BLUE}{q125}{Fore.RESET}. Tommorrow leads you to the life you haven`t {Fore.BLUE}{q126}{Fore.RESET} yet. So why not plan to live today with the most adventurious and positive outlook because today is yesterday`s tommorrow and we all know that it`s good to do things differently. So let`s go to {Fore.BLUE}{q127}{Fore.RESET} and {Fore.BLUE}{q128}{Fore.RESET} with someone cool. Or you could just let it {Fore.BLUE}{q129}{Fore.RESET} right by.')

# topic 14

while q2 == '14':
    q130 = input('SILLY WORD ')
    q131 = input('LAST NAME ')
    q132 = input('ILLNESS ')
    q133 = input('NOUN (PLURAL) ')
    q134 = input('ADJECTIVE')
    q135 = input('ADJECTIVE ')
    q136 = input('SILLY WORD ')
    q137 = input('PLACE ')
    q138 = input('NUMBER ')
    q149 = input('ADJECTIVE')
    print(f'Dear School Nurse: {Fore.BLUE}{q130}{Fore.RESET} {Fore.BLUE}{q131}{Fore.RESET} will not be attending school today. He/she has come down with a case of {Fore.BLUE}{q132}{Fore.RESET} and has horrible {Fore.BLUE}{q133}{Fore.RESET} and a/an {Fore.BLUE}{q134}{Fore.RESET} fever. We have made an appointment with the {Fore.BLUE}{q135}{Fore.RESET} Dr. {Fore.BLUE}{q136}{Fore.RESET}, who studied for many years in {Fore.BLUE}{q137}{Fore.RESET} and has 5 degrees in pediatrics. He will send you all the information you need. Thank you! Sincerely Mrs. {Fore.BLUE}{q138}{Fore.RESET}.')

# topic 15

while q2 == '15':
    q150 = input('GIRL`S NAME ')
    q151 = input('ANIMAL ')
    q152 = input('COLOR ')
    q153 = input('PLACE ')
    q154 = input('VERB ')
    print(f'{Fore.BLUE}{q150}{Fore.RESET} had a little {Fore.BLUE}{q151}{Fore.RESET} little {Fore.BLUE}{q151}{Fore.RESET} little {Fore.BLUE}{q151}{Fore.RESET}, {Fore.BLUE}{q150}{Fore.RESET} had a little {Fore.BLUE}{q151}{Fore.RESET}, it`s fleece was {Fore.BLUE}{q152}{Fore.RESET} as snow. It followed her to {Fore.BLUE}{q153}{Fore.RESET} one day, {Fore.BLUE}{q153}{Fore.RESET} one day, {Fore.BLUE}{q153}{Fore.RESET} one day, it made the children {Fore.BLUE}{q154}{Fore.RESET} and play to see a {Fore.BLUE}{q151}{Fore.RESET} at {Fore.BLUE}{q153}{Fore.RESET}')

# topic 16

while q2 == '16':
    q154 = input('COLOR ')
    q155 = input('NOUN (PLURAL) ')
    q156 = input('NOUN ')
    q157 = input('ADJECTIVE ')
    print(
        f'Roses are {q154}, {q155} are blue, {q156} is {q157}, and so are you.')

# topic 17

while q2 == '17':
    q158 = input('VERB ENDING IN "ING" ')
    q159 = input('NOUN ')
    q160 = input('PART OF THE BODY ')
    q161 = input('VERB ')
    q162 = input('ANIMAL')
    q163 = input('VERB ENDING IN "ED" ')
    print(f'I was {Fore.BLUE}{q158}{Fore.RESET} down the hallway and some {Fore.BLUE}{q159}{Fore.RESET} grabbed my {Fore.BLUE}{q160}{Fore.RESET}, and I turned to him and said "so help me, if you {Fore.BLUE}{q161}{Fore.RESET} me again you will go the way of the {Fore.BLUE}{q162}{Fore.RESET}." And then he {Fore.BLUE}{q163}{Fore.RESET} away.')

# topic 18

while q2 == '18':
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

# topic 19

while q2 == '19':
    q171 = input('FRUIT ')
    q172 = input('NOUN (PLURAL) ')
    q173 = input('NOUN ')
    q174 = input('NOUN ')
    q175 = input('NOUN (PLURAL) ')
    q176 = input('NOUN ')
    q177 = input('SILLY WORD ')
    print(f'J.R.R. Tolkien has been thrust into the {Fore.BLUE}{q171}{Fore.RESET}-light yet again with the release of his famous trilogy Lord of the {Fore.BLUE}{q172}{Fore.RESET} as a {Fore.BLUE}{q173}{Fore.RESET} series. The three books, {Fore.BLUE}{q174}{Fore.RESET} of the Ring, The Two {Fore.BLUE}{q175}{Fore.RESET}, and Return of the {Fore.BLUE}{q176}{Fore.RESET}, are preceded by another book The {Fore.BLUE}{q177}{Fore.RESET}, which may also be filmed later on.')

while q2 == '20':
    q178 = input('NOUN ')
    q179 = input('NOUN (PLURAL)')
    q180 = input('ADJECTIVE ')
    q181 = input('VERB ')
    q182 = input('NOUN (PLURAL) ')
    q183 = input('COLOR ')
    q184 = input('BODY PART ')
    print(f'Be my {Fore.RESET}{q178}{Fore.RESET} {Fore.BLUE}{q179}{Fore.RESET} make the world go {Fore.BLUE}{q180}{Fore.RESET} Pickachu says "I {Fore.BLUE}{q181}{Fore.RESET} you" I love {Fore.BLUE}{q182}{Fore.RESET}, {Fore.BLUE}{q183}{Fore.RESET} does too You make my {Fore.RESET}{q184}{Fore.RESET} flutter')
