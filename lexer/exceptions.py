class UnknownKeyword(Exception):
    def __init__(self, keyword):
        print("ERROR: Keyword {} doesn't exist".format(keyword))
