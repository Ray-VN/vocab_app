class Vocabulary:
    def __init__(self, word, meaning, image_path=None, review_count=0, last_review=None):
        self.word = word
        self.meaning = meaning
        self.image_path = image_path
        self.review_count = review_count
        self.last_review = last_review

    def __str__(self):
        return f"{self.word} - {self.meaning}"
