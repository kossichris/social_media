
from socialPost import to_base64
from socialPost import post_platforms
import flyerCreator as fc
import contentCreator as cc


def main():
    mode = input("Enter step: ")
    if mode == 's':
        cc.create_content()
    elif mode == 'e':
        fc.flyer_creator()
    # post_platforms()
    # to_base64()


main()
