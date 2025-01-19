# PYTHON VERSION: 3.12.7

import back as b


def main():
    username, password = b.ask_credentials()
    client = b.login(username, password)

    actions = {
        "1": lambda: b.send_post(client),
        "2": lambda: b.send_post_image(client),
        "3": lambda: b.timeline(client),
        "4": lambda: b.profile_feed(client),
        "5": lambda: b.profile_info(client),
        "6": lambda: b.clear_screen()
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