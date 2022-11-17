def generate_hashtag(s):
    if not s or len(s) > 140:
        return False
    else:
        return '#' + s.title().replace(' ', '')


print(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice')
