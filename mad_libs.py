import libs

while True:
    MAIN_Q = input(
        "Hello there! Welcome to Mad Libs! Press P to begin or Q to quit. ").lower()
    if MAIN_Q == 'q':
        quit()

    if MAIN_Q is 'p':
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
21. Dictionary Disasters 1''')

    topic_selection = input(
        'Just write the number of the topic you want to play. ')

    if topic_selection == '1':
        libs.madlib1
    elif topic_selection == '2':
        libs.madlib2
    elif topic_selection == '3':
        libs.madlib3
    elif topic_selection == '4':
        libs.madlib4
    elif topic_selection == '5':
        libs.madlib5
    elif topic_selection == '6':
        libs.madlib6
    elif topic_selection == '7':
        libs.madlib7
    elif topic_selection == '8':
        libs.madlib8
    elif topic_selection == '9':
        libs.madlib9
    elif topic_selection == '10':
        libs.madlib10
    elif topic_selection == '11':
        libs.madlib11
    elif topic_selection == '12':
        libs.madlib12
    elif topic_selection == '13':
        libs.madlib13
    elif topic_selection == '14':
        libs.madlib14
    elif topic_selection == '15':
        libs.madlib15
    elif topic_selection == '16':
        libs.madlib16
    elif topic_selection == '17':
        libs.madlib17
    elif topic_selection == '18':
        libs.madlib18
    elif topic_selection == '19':
        libs.madlib19
    elif topic_selection == '20':
        libs.madlib20
    elif topic_selection == '21':
        libs.madlib21