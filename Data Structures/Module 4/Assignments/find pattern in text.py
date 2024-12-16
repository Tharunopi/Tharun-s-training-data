def find_pattern(text, pattern):
    for i in range(len(text)):
        if pattern == text[i:(i+len(pattern))]:
            print(i, end=" ")

find_pattern("testTesttesT", "Test")