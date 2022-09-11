from ayrshare import SocialPost
import base64


# get an API Key at ayrshare.com
social = SocialPost('AKQBV4E-2GF4155-PPZB7VB-2H797PF')

# Post to Platforms Twitter, Facebook, and LinkedIn


def post_platforms():
    base64_img = to_base64()
    upload_response = social.upload({
        # Required: The image as a Base64 encoded string. Example encoding: https://www.base64-image.de/
        'file': base64_img,

        # Optional
        'fileName': 'tips.png',

        'platforms': ['twitter', 'linkedin'],

        'scheduleDate': '2022-09-10T17:25:00Z',

        # Optional
        'description': 'Test: An automated post with image',

        'shorten_links': True

    })
    print(upload_response)


# Convert image to base64
def to_base64():
    with open("new_flyer.png", "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
        return 'data:image/jpeg;base64,/9j/' + str(b64_string.decode('utf-8'))


# Delete a post


def delete_post(post_result):
    delete_result = social.delete({'id': post_result['id']})
    print(delete_result)


# History
# print(social.history())
