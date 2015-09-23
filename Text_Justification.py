def fullJustify(words,maxWidth):
    if maxWidth == 0:
	    return [""]
    tail = ""
    #for i in range(maxWidth):
    #    tail += "  "
    #words.append(tail)
    lens = []
    for i in words:
        lens.append(len(i))

    anslist = []
    tmplist = []
    curlength = 0
    blanklist = []
    for index,word in enumerate(words):
        if lens[index] + curlength +len(tmplist) <= maxWidth:
            tmplist.append(word)
            curlength += lens[index]
        else:
            if len(tmplist)>1:
                blanknum = len(tmplist) -1
                blanklen = (maxWidth - curlength)/(len(tmplist)-1)
                blankmod = (maxWidth - curlength) % (len(tmplist)-1)
                if blankmod == 0:
                    for k in range(blanknum):
                        blank = ""
                        for i in range(blanklen):
                            blank += " "
                        blanklist.append(blank)
                else:
                    for i in range(blanknum):
                        blanklist.append("")
                    for i in range(maxWidth - curlength):
                        blanklist[i%blanknum] += " "

            else:
                blanklen = maxWidth - curlength
                blank = ""
                for i in range(blanklen):
                    blank += " "
                blanklist.append(blank)
            string = ""
            for tmpindex, tmpword in enumerate(tmplist):
                string += tmpword
                if tmpindex<len(blanklist):
                    string += blanklist[tmpindex]
            anslist.append(string)
            tmplist = []
            tmplist.append(word)
            curlength = len(word)
            blanklist = []
    if len(tmplist)>0:
        string = " ".join(tmplist)
    while len(string)<maxWidth:
        string += " "
    if len(string)>0:
        anslist.append(string)

    return anslist
l = ["This", "is", "an", "example", "of", "text", "justification."]
l2 = ["1234 ","1234 "]
l3 = ["What","must","be","shall","be."] #12
l4 = ["Here","is","an","example","of","text","justification."] #16
l5 = ["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."]#30
a = fullJustify(l5,30)
print a
