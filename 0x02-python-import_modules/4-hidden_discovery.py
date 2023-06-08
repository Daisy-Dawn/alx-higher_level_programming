#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    a = dir(hidden_4)

    for x in a:
        if x[:2] != "__":
            print(x)
