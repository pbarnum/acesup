##
# AcesUp
# Written by Patrick Barnum
##

from version import __version__


class Menu:
    MAIN = 'main'
    PLAYER = 'player'
    STATS = 'stats'
    GAME = 'game'
    DELETE = 'delete'
    QUIT = 'quit'

    def __init__(self):
        self.__width = 58
        self.__padding = 10
        self.__border = '+'
        for i in range(0, self.__width):
            self.__border = self.__border + '-'
        self.__border = self.__border + '+'

        self.__currentMenu = self.MAIN

    def setCurrentMenu(self, menu):
        # TODO check if menu matches any constant value
        self.__currentMenu = menu

    def getCurrentMenu(self):
        return self.__currentMenu

    def printMenu(self, *args):
        if len(args[0]) > 0:
            return getattr(self, self.getCurrentMenu() + 'Menu')(args)
        else:
            return getattr(self, self.getCurrentMenu() + 'Menu')()

    def getInput(self, inputText):
        return str(raw_input('\n' + inputText)).lower()

    def hasMenu(self):
        return self.__currentMenu is not None

    def __titleLengthIsGood(self, title):
        return len(title) < (self.__width - self.__padding)

    def __findClosestSpace(self, title, index):
        if index is ' ':
            return index

        before = index - 1
        after = index + 1
        while before >= 0 and after < len(title):
            if title[before] is ' ':
                return before
            if title[after] is ' ':
                return after
            before = before - 1
            after = after + 1
        return index

    def __formatTitle(self, title, split=2):
        if self.__titleLengthIsGood(title) is False:
            titles = []
            titleLength = len(title)
            segmentLength = int(titleLength / split)

            index = 0
            while len(titles) != split:
                beginningIndex = index
                index = (segmentLength * split) + 1
                index = self.__findClosestSpace(title, index)
                titles.append(title[beginningIndex:index])

            for string in titles:
                if self.__titleLengthIsGood(string) is False:
                    titles = self.__formatTitle(title, split + 1)
                    break

            return titles
        else:
            return [title]

    def __addPadding(self, string):
        string = (' ' * (self.__padding / 2)) + string + (' ' * (self.__padding / 2))
        addToEnd = True
        while len(string) < (self.__width):
            if addToEnd is True:
                string = string + ' '
            else:
                string = ' ' + string
            addToEnd = not addToEnd
        return string

    def printTitle(self, title):
        if '\n' in title:
            titles = title.splitlines()
        else:
            titles = self.__formatTitle(title)

        print(self.__border)
        for string in titles:
            print('|' + self.__addPadding(string) + '|')
        print(self.__border + '\n')

    ##
    #
    ##
    def mainMenu(self, args):
        playerName = args[0]

        self.printTitle('Welcome to AcesUp\nWritten by Patrick Barnum\nBuild ' + __version__)

        print('Currently playing as "' + playerName + '"\n')

        print('Please select an option from the following menu:')
        print('[N]ew game')
        print('[C]hange Player')
        print('[P]rint statistics')
        print('[S]how top 10 scores')
        print('[D]elete all scores')
        print('[Q]uit')

        userInput = str(self.getInput('Enter your choice: ')).lower()
        if userInput == 'n':
            self.setCurrentMenu(Menu.GAME)
        elif userInput == 'q':
            self.setCurrentMenu(Menu.QUIT)

    def gameMenu(self, args):
        card1, card2, card3, card4 = args[0]
        print('Actions:')

        if card1 is not None:
            print('[mv|rm 1] ' + str(card1))
        if card2 is not None:
            print('[mv|rm 2] ' + str(card2))
        if card3 is not None:
            print('[mv|rm 3] ' + str(card3))
        if card4 is not None:
            print('[mv|rm 4] ' + str(card4))

        print('[D]eal again')
        print('[Q]uit game')
        return self.getInput('What would you like to do? ')

    def changePlayerMenu(self, args):
        currentPlayer, allPlayers = args
        print('Create or change to a new player')

        print()

    def quitMenu(self):
        answer = self.getInput('Are you sure you want to quit? [y/n] ')
        if answer == 'n' or answer == 'no':
            self.setCurrentMenu(self.MAIN)
        elif answer == 'y' or answer == 'yes':
            self.setCurrentMenu(None)
