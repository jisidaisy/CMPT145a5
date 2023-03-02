from Queue import Queue

def main():
    # Define the file name here
    fileName = "monsters1.txt"

    # use constants
    GODZILLA = "Godzilla"
    MOTHRA = "Mothra"

    # list to store defeated space monsters
    godzillaDefeated = []
    mothraDefeated = []

    try:
        # Create queue ADT to store space monsters
        battle = Queue()

        # Open the file in read mode
        with open(fileName, 'r') as f:
            for line in f.readlines():
                # remove any empty spaces from the line
                item = line.rstrip('\n').strip()
                #  if the current item is Godzilla
                if item == GODZILLA:
                    # Verify if any space monsters are waiting in the queue
                    if battle.is_empty() == False:
                        # Godzilla defeats the space monster that is currently first in the queue
                        godzillaDefeated.append(battle.dequeue())
                elif item == MOTHRA:
                    # Verify if any space monsters are waiting in the queue
                    if battle.is_empty() == False:
                        # Mothra defeats the space monster that is currently first in the queue
                        mothraDefeated.append(battle.dequeue())
                else:
                    # it is space monster, so enqueue the item
                    battle.enqueue(item)
        # file read is success and battle is completed

        # if there is space monster left in the queue
        if battle.is_empty() == False:
            print("Oh no! The space monsters won thanks to " + str(battle.dequeue()))
        else:
            # Earth is saved by Godzilla and Mothra
            print("The space monsters were beaten!\n")
            # Print the space monsters defeated by Godzilla and Mothra
            print("Godzilla defeated:")
            for monster in godzillaDefeated:
                print(monster)

            print("\nMothra defeated:")
            for monster in mothraDefeated:
                print(monster)
    except IOError:
        print("File ", fileName, " not accessible")


if __name__ == '__main__':
    main()