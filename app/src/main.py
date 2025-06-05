# PYTHON VERSION: 3.12.7

import core


def main():
    username, password = core.ask_credentials()
    client = core.login(username, password)

    actions = {
        "1": lambda: core.send_post(client),
        "2": lambda: core.send_post_image(client),
        "3": lambda: core.timeline(client),
        "4": lambda: core.profile_feed(client),
        "5": lambda: core.profile_info(client),
        "6": lambda: core.clear_screen()
    }

    while True:

        input("Press Enter to continue...\n")

        action = input("""What do you want to do?\n
                        [1] - Send text post
                        [2] - Send post with image
                        [3] - See feed
                        [4] - See profile posts
                        [5] - See profile info
                        [6] - Clear screen
                        [q] - Quit\n""")
        
        if action.lower() == "q":
            break

        actions[action]()
    
if __name__ == "__main__":
    main()