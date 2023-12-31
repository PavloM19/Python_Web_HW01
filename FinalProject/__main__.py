from Bot import *


if __name__ == "__main__":
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot = Bot()
    bot.book = Storage.load("AddressBook")

    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        action = input('Type help for list of commands or enter your command\n').strip().lower()

        if action == 'exit':
            break

        if action == 'help':
            format_str = str('{:%s%d}' % ('^',20))
            for command in commands:
                print(format_str.format(command))

            action = input().strip().lower()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                Storage.save("AddressBook", bot.book)
        else:
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                Storage.save("AddressBook", bot.book)



