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