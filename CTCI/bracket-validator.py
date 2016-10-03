def Evaluate(str):
  stack = []
  set1, set2 = "<({[", ">)}]"
  for c in str :
    if c in set1:
        #print "c in pushChars, APPENDING: ", c
        stack.append(c)
    elif c in set2:
        #print "c in popChars: ", c
        if len(stack)==0:
            return False
        else:
            stackTop = stack.pop()
            #print "POPPING" , stackTop
            balancingBracket = set1[set2.index(c)]
            if stackTop != balancingBracket:
                #print "THIS NOW"
                return False
  #finally everything should be popped
  if len(stack)==0:
      return True
  else:
      return False

result = Evaluate("<html><head><body><h1>Still working on it</h1></body></head></html>")
print "Bracket Validator: ", result
result = Evaluate("<html><head><body><h1>Still working on it</h1</body></head></html>")
print "Bracket Validator: ", result
