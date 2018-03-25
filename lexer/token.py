class Token:
    def __init__(self, tag_id):
        self.tag = tag_id

    def __str__(self):
        return str(self.tag)
