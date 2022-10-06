def ui_build(sub):
    ui = ''
    for i in sub:
        if i in ui:
            pass
        else:
            ui += i
    return ui


def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        sub = ui_build(string[i:i+k]) # Understand how this is working
        print(sub)


# merge_the_tools('AABCAAADA', 3)
#print(ui_build('AAB'))

lst = [1,2,3,4]
print(sum(lst))