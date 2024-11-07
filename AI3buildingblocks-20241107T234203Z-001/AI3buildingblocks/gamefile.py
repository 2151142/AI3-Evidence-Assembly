win=0
import time
while win==0:
    blade = 0
    gold = 49
    torch = 0
    stage = 0
    x = 0
    while x == 0:



        print('You come to a junction, with the path diverging to the left and right.')
        print('The path to the left leads downhill, and you can hear the faint sound of running water.')
        print('The path to the right leads uphill, and continues to the mouth of an ominous cave.')
        print('Which way will you go?')

        choice = input()
        if choice == 'left': 
            print('As you start marching down the slope and around a bend, the sound of running')
            time.sleep(1)
            print('water becomes louder and louder, until a racing river comes into view.')
            time.sleep(1)
            print('A stone bridge carries the path across the bridge and back up the hill.')
            time.sleep(1)
            print('Will you cross the bridge or go back?')
            choice = input()
            if choice == 'bridge':
                print('As soon as your foot touches the flagstones of the bridge a massive rumbling')
                time.sleep(1)
                print('shakes the bridge, followed quickly by a grotesque figure pulling itself up from')
                time.sleep(1)
                print('under the bridge.')
                time.sleep(1)
                print('"WHO DARES TO TRY TO CROSS MY BRIDGE?"')
                time.sleep(1)
                print("The troll's eyes quickly turn to you, before narrowing into a predatory glare.")
                time.sleep(1)
                print('"DIE FILTHY HUMAN!"')
                time.sleep(1)
                print('As the beast charges, a choice must be made. Will you fight, or flee?')
                choice = input()
                if choice == 'flee':
                   print("As you run, the rumblings of the beast's pursuit draw quieter and quieter.")
                   time.sleep(1)
                   print('However, as you make your escape, you realise that you have lost the creature')
                   time.sleep(1)
                   print('but are back where you started, and your quest remains unfinished.')
                   continue
                elif choice == 'fight':
                    if blade == 0:
                        print('You draw your sword and strike out at the beast, but the blade shatters upon its thick skin.')
                        time.sleep(1)
                        print('The beast swings its mighty club down upon your head, and the world disappears into')
                        time.sleep(1)
                        print('the darkness. Perhaps in the next life you will be more careful.')
                        time.sleep(2)
                        print(' ')
                        print(' ')
                        print(' ')
                        print(' ')
                        print(' ')
                        break
                    elif blade == 1:
                        print("Reldy's blade slides cleanly out of your scabbard with a shrill tone, the blade")
                        time.sleep(1)
                        print('glistening in the sunlight. You steady yourself as the monster approaches,')
                        time.sleep(1)
                        print('blade held out in front of you. The troll lunges towards you, its eyes widening')
                        time.sleep(1)
                        print('as it impales itself on your extended sword. The beast lets out one final breath')
                        time.sleep(1)
                        print('before collapsing to the ground, eyes glazed over and body still.')
                        time.sleep(1)
                        print('You step over its corpse and across the bridge, continuing farther into the forest.')
                        time.sleep(2)
                        stage = 1
                else:
                    print('Invalid input. Valid inputs are fight and flee.')
            elif choice == 'back':
                continue
            else:
                print('Invalid input. Valid inputs are bridge and back.')
        elif choice == 'right':
            print('You set your mind and begin marching up to the dark cavern at the top of the hill.')
            time.sleep(1)
            print('Its wide maw looms before you, its darkness thick and heavy. Do you continue into the shadows or turn back?')
            choice = input()
            if choice == 'continue':
                if torch == 0:
                    print('You tentatively step into the deep darkness, and, unguided by light, you')
                    time.sleep(1)
                    print('slowly feel the way forward. Suddenly, your hand touches something... Warm.')
                    time.sleep(1)
                    print('A loud cacophany of screeches echoes through the cavern as the shadows come alive, eager to devour you.')
                    time.sleep(1)
                    print('The overwhelming darkness prevents both escape and attack,')
                    time.sleep(1)
                    print('and while you flail, desperate to survive, the shadows eat you alive.')
                    time.sleep(1)
                    print('Perhaps in the next life you will be more prepared.')
                    time.sleep(2)
                    print(' ')
                    print(' ')
                    print(' ')
                    print(' ')
                    print(' ')
                    break
                elif torch == 1:
                    print('You pull out your torch and light it before stepping confidently into the darkness.')
                    time.sleep(1)
                    print('Your feet find stable footing as you descend, and the shadows themselves seem to almost move around you,')
                    time.sleep(1)
                    print('with the sound of fluttering wings, footfalls, and the crackling of the torch the only refuges from the silence.')
                    time.sleep(1)
                    print('test')
            elif choice == 'back':
                continue
        elif choice == 'back':
            print('You turn away from the path and march back the way you came, eventually coming to an enclosed wooden cart')
            time.sleep(0.7)
            print('on the side of the path. A small hatch covers a window on the side of the cart. ')
            time.sleep(0.7)
            print('Will you knock on the hatch, or go back to the crossroads?')
            choice = input()
            if choice == 'hatch':
                print('Your hand rises up to the small window, but before you can knock, it swings open, and you are greeted')
                time.sleep(1)
                print("by a round face with a wispy beard clinging to its chin. A large, lumpy nose juts out from the creature's")
                time.sleep(1)
                print('face, which, you note, is far smaller than you expected it to be. The gnome cracks a thin smile at you.')
                time.sleep(1)
                print('"Well, good morning traveller. Have you a need for supplies? I, Reldy, provide only the highest quality')
                time.sleep(1)
                print('"goods at the most reasonable prices. would you care to take a look?"')
                time.sleep(1.5)
                print('Reldy shuffles away from the window, and, after a moment, returns with a finely crafted sword.')
                time.sleep(1)
                print('"This masterforged blade comes straight from the dwarvern mountains, born of the magma at their hearts.')
                time.sleep(1)
                print('It will serve you far better than that rusted blade at your hip, and for only 40 gold!" Reldy gestures')
                time.sleep(1)
                print('to your current sword, which is admittedly of poor quality.')
                time.sleep(1)
                print('"And if the blade is not to your liking," the gnome continues, perhaps instead you would desire a handcrafted')
                time.sleep(1)
                print('orcish torch? Captured from their beastly camps and enchanted to burn for 100 years once lit!"')
                time.sleep(1)
                print('You check your coinpurse, which currently holds 49 gold pieces. Will you purchase the sword for 40 gold or the torch for 10?')
                choice = input()
                while x == 0:
                    print(f'GOLD = {gold}')
                    choice == input()
                    if choice == 'sword':
                        if gold >=40:
                            gold = gold-40
                            print("The gnome's mouth smiles as it watches your gold piles up on the table before quickly sweeping it into a bag.")
                            print('"Will there be anything else sir?" he asks, clasping his tiny hands together in anticipation.')
                            continue
                        else:
                            print('The gnome frowns as he looks at you as you count your gold. "I am sorry sir, it appears you are short!')
                            print('Is there anything else you might desire?"')
                            continue
                    elif choice == 'torch':
                        if gold >= 10:
                            if torch < 1:
                                gold = gold-10
                                print("The gnome's mouth smiles as it watches your gold piles up on the table before quickly sweeping it into a bag.")
                                print('"Will there be anything else sir?" he asks, clasping his tiny hands together in anticipation.')
                                continue
                            else:
                                print('"I am truly sorry, but I am all out of torches. That one should suit you just fine though."')
                        else:
                            print('The gnome frowns as he looks at you as you count your gold. "I am sorry sir, it appears you are short!')
                            print('Is there anything else you might desire?"')
                    elif choice == 'back':
                        print("You leave the gnome's cart behind as you return to the crossroads.")
                        break


