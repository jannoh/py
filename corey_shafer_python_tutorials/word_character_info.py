print("""Welcome to the Character Info Program""")
print("""=====================================\n""")
# Enter word ==> Transform ==> Print/Return

word = "tartars"

if((len(word)%2) == 1):
    char_details = f'{word} is a {len(word)} character word, has first character {word[0]}, middle character {word[len(word)//2]} and last character {word[len(word)-1]}.\n'
    print(char_details)
else: print('lenError: Enter an odd word\n')