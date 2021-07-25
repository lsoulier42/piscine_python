if __name__ == "__main__":
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }
    for k in languages:
        print("{} was created by {}".format(k, languages[k]))