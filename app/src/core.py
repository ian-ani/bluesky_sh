# PYTHON VERSION: 3.12.7

import os
import getpass
from atproto import Client


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def ask_credentials():
    username = input("Enter handle (ex. username.bsky.social): ")
    password = getpass.getpass("Enter password: ")
    
    clear_screen()
    
    return username, password

def login(username, password):
    client = Client()
    retry = 1
    
    while retry <= 3:
        try:
            get_did = client.login(username, password)
            break
        except Exception as e:
            print(f"UnathorizedError: invalid username of password. Retry #{retry} (max. 3).")
            retry += 1
            if retry <= 3:
                username, password = ask_credentials()
            else:
                print("No retries left.")
                quit()

    print("This is your did " + f"\033[33m{get_did.did}\033[97m" + " you might need it for later. Save it.")
    print(f"Logged in with {username}...")

    return client

def send_post(client):
    text = input("\nNew post: ")

    if len(text) > 300:
        print("Character limit. Max 300 characters.")
    elif len(text) <= 0:
        print("You haven't written anything.")
    else:
        client.send_post(text)

def send_post_image(client):
    image = input("\nEnter image path: ")
    text = input("\nEnter text: ")
    alt = input("\nEnter image alt: ")

    if len(text) > 300 or len(alt) > 2000:
        print("Character limit is 300 characters and alt limit is 2000 characters.")
    elif len(text) <= 0:
        print("You haven't written anything.")
    else: 
        try:
            with open(os.path.join(image), "rb") as f:
                img_data = f.read()

            client.send_image(text=text, image=img_data, image_alt=alt)
        except Exception:
            print("Something went wrong with the image.")

def timeline(client):
    post_limit = input("\nEnter limit of posts (max. 100): ")

    if post_limit.isdigit() == False:
        print("Please, enter a number between 1 and 100.")
    else:
        post_limit = int(post_limit)

        if post_limit > 100:
            print("Post limit is 100.")
        elif post_limit <= 0:
            print("No post limit entered.")
        else:
            data = client.get_timeline(limit=post_limit)
            feed = data.feed

            for item in feed:
                post = item.post
                author = post.author

                print(f"AUTHOR: {author.display_name}\nDATE: {post.record.created_at}\nPOST:\n\n{post.record.text}")
                print("-----------------------------------------------------------------")

def profile_feed(client):
    post_limit = input("\nEnter limit of posts (max. 100): ") 
    get_did = input("Enter did: ")

    if post_limit.isdigit() == False:
        print("Please, enter a number between 1 and 100.")
    else:
        post_limit = int(post_limit)
        
        if int(post_limit) > 100:
            print("Post limit is 100.")
        elif int(post_limit) <= 0:
            print("No post limit entered.")
        else:
            try:
                data = client.get_author_feed(
                    actor=get_did,
                    filter="posts_and_author_threads",
                    limit=post_limit
                )
                feed = data.feed

                for item in feed:
                    post = item.post
                    author = post.author

                    print(f"AUTHOR: {author.display_name}\nDATE: {post.record.created_at}\nPOST:\n\n{post.record.text}")
                    print("-----------------------------------------------------------------")
            except Exception:
                print("Something went wrong. Enter a valid did.")

def profile_info(client):
    get_did = input("Enter did: ")

    try:
        data = client.get_profile(actor=get_did)

        print(f"""
            USERNAME: {data.display_name}
            HANDLE: {data.handle}
            CREATED AT: {data.created_at}
            FOLLOWERS: {data.followers_count}
            FOLLOWING: {data.follows_count}
            POSTS: {data.posts_count}
            BIO: {data.description}\n""")
    except Exception:
        print("Enter a valid did.")
