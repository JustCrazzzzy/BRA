#7^3 + 20 * (10/3 + 6)
def func1 ( x, y, z, f, h):
    #x+y*(z**f+h)
    result = x+y*(z/f+h)
    print(result)
    return result

var1 = func1(7**3,20,10,3,6)
print('Result: ', var1)


#(63/2 + 45 - 8) / 2^5
def func2 (q,w,e,r,t,y):
    #q/w+e-r/t**y
    result = (q/w+e-r)/t**y
    print(result)
    return result

var2 = func2(63,2,45,8,2,5)
print('Result:', var2)

#83/8*(43/20+5**7)
def func3 (a, b, c):
    #a*(b+c)
    result = a*(b+c)
    print(result)
    return (result)

var3 = func3(83/8, 43/20, 5**7)
print ('Result:', var3)

#Написать функцию, которая будет принимать номер телефона и выводить его в формате +38 (099) 123 - 12 - 12

def func4(j, m):
    result = " +380 (%s) %s" % (j, m)
    print(result)

var3 = func4( '99', '123 12 12')


def func5(j, m):
    result = "+380 ({}) {}".format(j, m)
    print(result)

var3 = func5( '99', '123 12 12')

def func6(j, m):
    result = f"+380 {j} {m}"
    print(result)

var3 = func6('(99)', '123 12 12')


#"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam posuere ex at leo interdum, eget aliquet ex ornare."
def func22(text):
    result = text[0:10]
    print(result)

S='''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam posuere ex at leo interdum, eget aliquet ex ornare.'''
var22 = func22(S)

def func23(text):
    result = text[0:25]
    print(result)

S='''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam posuere ex at leo interdum, eget aliquet ex ornare.'''
var22 = func23(S)



def func24(text):
    result = text.upper()
    print(result)

text='''hello world'''
var24 = func24(text)

#"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus non dictum lacus. Etiam placerat, sapien tincidunt pellentesque ullamcorper, tortor tortor condimentum tellus, eget tempor mi turpis nec sapien. Nunc lectus ex, suscipit in justo quis, maximus consequat elit. Fusce mollis massa id ornare semper. Morbi cursus sollicitudin porttitor. Mauris at lobortis metus. Donec a nisl felis. Mauris eu enim mollis, dictum velit a, venenatis odio. Integer non pellentesque urna. Nam tortor lacus, elementum a diam sed, porttitor ullamcorper justo. Morbi laoreet tempor sapien non auctor. Proin imperdiet finibus pellentesque. Nulla gravida leo et libero egestas vulputate quis quis orci. Morbi felis est, dignissim sit amet malesuada sit amet, maximus id lacus."""


def func25(fruit, vegetables):
    result = f"I like {fruit} and {vegetables}"
    print(result)


var25 = func25('fruit', 'vegetables')


def func26(fff):
    result = f"Do you like summer? {fff}"
    print(result)


var26 = func26('NO')

def func27(t1, t2):
    result = f"This is a {t1}. It's {t2}."
    print(result)

var27 = func27('subj', 'prop')


def func28(l, w, h):
    result = f"lenght {l}.width {w}. height {h}."
    print(result)

var28 = func28('88', '93', '44')


def func29(text):
    result = text.strip([8])
    print(result)

text='''    Hello world!    '''
var29 = func29(text)



def func30(text):
    result = text.isdigit()
    print(result)

text='''    Hello world!    '''
var30 = func30(text)






