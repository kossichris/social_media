
import flyerCreator as fc
import contentCreator as cc


def main():
    mode = input("Enter step: ")
    if mode == 'search':
        cc.create_content()
    elif mode == 'edit':
        fc.flyer_creator()


main()
