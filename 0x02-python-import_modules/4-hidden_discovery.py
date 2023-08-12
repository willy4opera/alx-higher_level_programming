#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    ids = dir(hidden_4)
    for id in ids:
        if id[:2] != "__":
            print(id)
