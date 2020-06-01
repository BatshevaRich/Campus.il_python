text = input("enter your text ")
text = text.replace(' ', '')
text = text.lower()
first_side = text[len(text)//2:]
if first_side[::-1] == text[:len(text)//2+1:]:
    print("ok")
else:
    print("not")