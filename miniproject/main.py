from checkmate import checkmate

# Example 1
def main():
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)
if __name__ == "__main__":
    main()


# Example 2
def main():
    board = """\
..
.K\
"""
    checkmate(board)
if __name__ == "__main__":
    main()



