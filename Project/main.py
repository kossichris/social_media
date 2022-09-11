
from socialPost import to_base64
from socialPost import post_platforms
import flyerCreator as fc
import contentCreator as cc


def main():
    mode = input("Enter step: ")
    if mode == 'search':
        cc.create_content()
    elif mode == 'edit':
        fc.flyer_creator()
    # post_platforms()
    # to_base64()


main()
