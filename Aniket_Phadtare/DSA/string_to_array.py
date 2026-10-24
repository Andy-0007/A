text="python"
char_array=list(text)
print(char_array)
char_array[0]="j"
char_array[-1]="a"
new_text="".join(char_array)
print(new_text)