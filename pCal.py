from main import *

def calculate():
    print("______________________________________")
    fullName = txtfn.get() + " " + txtln.get()
    lblstatus.configure(text= fullName)

    # calculate a marks and result
    s1 = txtfs.get()
    s1 = int(s1)

    s2 = txtss.get()
    s2 = int(s2)

    s3 = txtms.get()
    s3 = int(s3)

    equal = (s1 + s2 + s3)
    equaliz = equal/3
    equalD = int(equaliz)

    
    if s1 < 30:
        s1Pass=("W Faild")
    elif s1 < 50:
        s1Pass=("S Pass")
    elif s1 < 60:
        s1Pass=("C Pass")
    elif s1 < 70:
        s1Pass=("B Pass")
    elif s1 < 100:
        s1Pass=("A pass")
    elif s1 == 100:
        s1Pass=("A+ Pass")

    if s2 < 30:
        s2Pass=("W Faild")
    elif s2 < 50:
        s2Pass=("S Pass")
    elif s2 < 60:
        s2Pass=("C Pass")
    elif s2 < 70:
        s2Pass=("B Pass")
    elif s2 < 100:
        s2Pass=("A pass")
    elif s2 == 100:
        s2Pass=("A+ Pass")

    if s3 < 30:
        s3Pass=("W Faild")
    elif s3 < 50:
        s3Pass=("S Pass")
    elif s3 < 60:
        s3Pass=("C Pass")
    elif s3 < 70:
        s3Pass=("B Pass")
    elif s3 < 100:
        s3Pass=("A pass")
    elif s3 == 100:
        s3Pass=("A+ Pass")

    if equalD < 30:
        sPass=("W Faild")
    elif equalD < 50:
        sPass=("S Pass")
    elif equalD < 60:
        sPass=("C Pass")
    elif equalD < 70:
        sPass=("B Pass")
    elif equalD < 100:
        sPass=("A pass")
    elif equalD == 100:
        sPass=("A+ Pass")
    print("calculated")

    

    #printing aria
    first_subject = combofs.get()
    lbls1name.configure(text = first_subject)
    lbls1mark.configure(text = s1)
    lbls1pass.configure(text = s1Pass)

    secound_subject = comboss.get()
    lbls2name.configure(text = secound_subject)
    lbls2mark.configure(text = s2)
    lbls2pass.configure(text = s2Pass)


    third_subject = comboms.get()
    lbls3name.configure(text = third_subject)
    lbls3mark.configure(text = s3)
    lbls3pass.configure(text = s3Pass)


    lbleqal.configure(text = equal)

    lbleqalize.configure(text = equaliz)
    lblpassOrfaild.configure(text = sPass)

    print("data viewing sussessfull")

def clearDeta():
    lbls1pass.configure(text = "pass/faild")
    lbls2pass.configure(text = "pass/faild")
    lbls3pass.configure(text = "pass/faild")
    lblpassOrfaild.configure(text = "pass/faild")

    lbls1mark.configure(text = "000")
    lbls2mark.configure(text = "000")
    lbls3mark.configure(text = "000")
    lbleqal.configure(text = "000")
    lbleqalize.configure(text = "000")

    lbls1name.configure(text = "Subject")
    lbls2name.configure(text = "Subject")
    lbls3name.configure(text = "Subject")

    txtln.delete(0, 'end')
    txtfn.delete(0, 'end')
    txtfs.delete(0, 'end')
    txtss.delete(0, 'end')
    txtms.delete(0, 'end')

    print("table is cleard!")
    # lblfn.delete(0, 'end')
    # lblln.delete(0, 'end')
        #result viewer
    '''
    first subject       pass/faild
    secound subject     pass/faild
    main subject        pass/faild
    equal               
    equalize            pass/faild

    70-100 - A pass
    60-70 - B pass
    50-60 - C pass
    30-50 - S pass
    0 - 30 - W faild

    abcsw
    '''

def saveHtml():

    file = fileName_html.get()
    if file == "":
        file = "index"
    else:
        file = fileName_html.get()

    file = file + '.html'

    #full name
    fullName = txtfn.get() + " " + txtln.get()
    #subjects
    sn1 = combofs.get()
    sn1 = str(sn1)
    sn2 = comboss.get()
    sn2 = str(sn2)
    sn3 = comboms.get()
    sn3 = str(sn3)
    #marks
    sm1 = txtfs.get()
    sm1 = int(sm1)
    sm2 = txtss.get()
    sm2 = int(sm2)
    sm3 = txtms.get()
    sm3 = int(sm3)
    #equal & equalize
    eq = sm1 + sm2 + sm3
    eqz = eq / 3
    eqv = int(eqz)

    if eqv < 30:
        sPass=("W Faild")
    elif eqv < 50:
        sPass=("S Pass")
    elif eqv < 60:
        sPass=("C Pass")
    elif eqv < 70:
        sPass=("B Pass")
    elif eqv < 100:
        sPass=("A pass")
    elif eqv == 100:
        sPass=("A+ Pass")


    sm1 = str(sm1)
    sm2 = str(sm2)
    sm3 = str(sm3)
    eq = str(eq)
    eqz = str(eqz)

    print(fullName,"\t|", sn1,"\t|", sn2,"\t|", sn3,"\t|", sm1,"\t|", sm2,"\t|", sm3,"\t|", eq,"\t|", eqz)
    tableRow = ("\n<tr>\n<td>" + fullName + "</td><td>" + sn1 + "</td><td>" + sm1  + "</td><td>" + sn2 + "</td><td>" + sm2 + "</td><td>" + sn3 + "</td><td>" + sm3 + "</td><td>" + eq + "</td><td>" + eqz + "</td><td>" + sPass + "</td>\n</tr>")

    with open(file,'a') as file:
        file.write(tableRow)

    clearDeta()
    '''
    full name | subject 1 | mark | subject 2 | marks | subject 3 | marks | equal | equalize | pass or faild
    '''

def clearHtmlFile():
    file = fileName_html.get()
    if file == "":
        file = "index"
    else:
        file = fileName_html.get()

    file = file + '.html'
    tag = ("<!-- "+ file[0:-5] +" is cleard!  -->")

    with open(file,'w') as file:
        file.write(tag)

    print("Full table is cleard!")


def basicCode():
    file = fileName_html.get()
    if file == "":
        file = "index"
    else:
        file = fileName_html.get()

    file = file + '.html'
    tag = ('''<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n <title>''' + file[0:-5] + '''</title>
    <style>
    body{
        padding-left: 10%;
        padding-right: 10%;
        padding-top: 2%;
        background-color: rgba(0, 48, 77, 0.288);
        font-size: larger;
        color: black;
    }
    table {
    border-collapse: collapse;
    width: 100%;
    }
    th{
        text-align: left;
        padding: 8px;
        background-color: rgba(0, 47, 77, 0.781);
        color: cornsilk;
    }
    td {
        text-align: left;
        padding: 8px;
    }
    tr:nth-child(even){background-color: #f2f2f2}
    </style>
    \n</head>\n<body>\n<table>\n<tr><th>Name</th><th>subject 1</th><th>marks</th><th>subject 2</th><th>marks</th><th>subject 3</th><th>marks</th><th>equal</th><th>equalize</th><th>pass or faild</th></tr>''')
    # print(tag)
    print("Basic Codes are writed")

    with open(file,'w') as file:
        file.write(tag)

