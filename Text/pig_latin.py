# get string
# detect vowel -> add way
# detect consonant cluster -> add cluster + ay


class PigLatin(object):
    consonant_clusters = ['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'sc', 'sh', 'sk',
                          'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr', 'sch', 'scr', 'shr', 'sph',
                          'spl', 'spr', 'squ', 'str', 'thr']
    vowels = ['a', 'e', 'i', 'o', 'u']

    @classmethod
    def latinize(cls, text):
        split_text = text.split(" ")
        pig_latin_words = []
        for word in split_text:
            word = cls.latinize_word(word)
            pig_latin_words.append(word)

        return " ".join(pig_latin_words).capitalize()

    @classmethod
    def latinize_word(cls, word):
        if cls.starts_with_vowel(word):
            latin_word = word + "way"
        elif cls.starts_with_consonant_cluster(word):
            cluster_length = cls.get_consonant_cluster_length(word)
            latin_word = word[cluster_length:] + word[:cluster_length] + 'ay'
        elif word[0:2].lower() in PigLatin.consonant_clusters:
            cluster = word[0:2].lower()
            word = word[2:]
            latin_word = word + cluster + 'ay'
        else:
            latin_word = word[1:] + word[0].lower() + 'ay'

        return latin_word

    @classmethod
    def starts_with_vowel(cls, word):
        if word == '':
            return False
        return word[0].lower() in PigLatin.vowels

    @classmethod
    def starts_with_consonant_cluster(cls, word):
        for cluster_length in range(3, 1, -1):
            if word[0:cluster_length].lower() in PigLatin.consonant_clusters:
                return True
        else:
            return False

    @classmethod
    def get_consonant_cluster_length(cls, word):
        for cluster_length in range(4, 0, -1):
            possible_cluster = word[0:cluster_length].lower()
            if possible_cluster in PigLatin.consonant_clusters:
                return cluster_length

        return 0


