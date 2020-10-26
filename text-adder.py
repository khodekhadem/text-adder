#*** code ha va file ha hame bayad to yek pooshe bashand ***
file = open("text.txt", "r")   #text.txt --> file matn avaliye
file2 = open("text2.txt","w")  #text2.txt --> file matni ke gharare khorooji ro save kone
for i in file.readlines():
    text = i
    text2 = "------"               #matni ke mikhay be tahesh ezafe beshe
    text = text[:len(text)-1]+text2+text[int(len(text))-1:]
    file2.write(text)



