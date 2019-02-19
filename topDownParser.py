production={}#all the productions
stack=[]#stack used for calculating first  and trailing
fst={}#it will contain the first of each nonTerminal
flw={}#it will contain the trailling of each nonTerminal
parseTable={}#it is our parseTable , there will be no values for error
startingSymbol=""
def install_first(nonTerminal,terminal):
	# print(terminal)
	if(fst.get(nonTerminal)==None):
		fst[nonTerminal]=[terminal]
		stack.append(nonTerminal+terminal)#pushing (A,a) into stack
		# print(alter[1])
	elif(terminal not in fst.get(nonTerminal)):
		fst[nonTerminal].append(terminal)
		stack.append(nonTerminal+terminal)#pushing (A,a) into stack
		
def first():

	for pro in production: #for each production of the form X->aALPHA OR X->e  
		for alter in production[pro]:
			# print(alter[0]<='Z')
			if((alter[0]<='Z' and alter[0]>='A')):
				continue
			else:
				install_first(pro,alter[0])

	while(len(stack)!=0):
		string = stack.pop(-1)#popping (Ba) and find production in the form of A->Balpha now each first(B) will be in first(A)
		for pro in production:
			for alter in production[pro]:
				if(alter[0]==string[0] and string[1]!='e'):
					# print(string[1])
					install_first(pro,string[1])

#for production in the form of A->y1y2y3y3....
#if y1,y2,y3 all contain the e then only first(A) will have e
	for pro in production:
		for alter in production[pro]:
			flag=0
			for alphabate in alter:
				if(alphabate<='Z' and alphabate >='A'):
					if(fst.get(alphabate)!=None):
						for symbol in fst[alphabate]:
							if(symbol=='e'):
								flag=1
								continue
							install_first(pro,symbol)
				else:
					#if you find any nonterminal then stop
					install_first(pro,alphabate)
					break		
				if(flag==1):

				# print("awefwe")
				# print("sdfasd",alter)
					continue
				else:
					break
				#if e is present then we have to go for the first(next alphabate)
				# install_first(pro,'e')
				
	#since we are not poping the elements of the stack we need to clear our stack
	stack.clear()





# def install_trail(nonTerminal,terminal):
# 	# print(terminal)
# 	if(t.get(nonTerminal)==None):
# 		t[nonTerminal]=[terminal]
# 		stack.append(nonTerminal+terminal)#pushing (A,a) into stack
# 		# print(alter[1])
# 	elif(terminal not in t.get(nonTerminal)):
# 		t[nonTerminal].append(terminal)
# 		stack.append(nonTerminal+terminal)#pushing (A,a) into stack
		
def install_follow(nonTerminal,alphabate):
	if(alphabate<='Z' and alphabate>='A'):
		# print("fist of ",alphabate,fst[alphabate])
		for symbol in fst[alphabate]:
			if(symbol=='e'):
				continue
			if(flw.get(nonTerminal)==None):
				flw[nonTerminal]=[symbol]
			else:
				flw[nonTerminal].append(symbol)
			# flw[nonTerminal]=fst[alphabate]
		# else:
			# for symbol in fst[alphabate]:
			# flw[nonTerminal].append(fst[alphabate])
		if('e' in fst[alphabate]):
			return True
	else:
		if(flw.get(nonTerminal)==None):
			# print("sdfasd")
			flw[nonTerminal]=[alphabate]
		else:
			flw[nonTerminal].append(alphabate)
	return False

def install_follow_follow(nonTerminal,calcuateFollow):
	
	if(flw.get(calcuateFollow)!=None):
		a=[]# to avoid the recursive call
		for symbol in flw[calcuateFollow]:
			a.append(symbol)
		for symbol in a:
			if(flw.get(nonTerminal)==None):
				flw[nonTerminal]=[symbol]
			elif(symbol not in flw[nonTerminal]):
			# print(flw)
				flw[nonTerminal].append(symbol)

def follow():

	#if it starting symbol insert $ in the follow(starting symbol)
	flw[startingSymbol]=['$']

	for pro in production: #for each production of the form A->aALPHA OR A->BaALPHA install(A,a)
		for findPro in production:
			for alter in production[findPro]:
				print(pro,alter)
				# print("alter", alter,"and",production[findPro])
				if(pro in alter):
					# print(True,pro,alter)
					flag=0#this flag indicate whether we have found pro or not
					for alphabate in alter:
						# print("fasdfa")
						if(flag==1):
							containEpsilon=install_follow(pro,alphabate)
							# print(containEpsilon,pro,alphabate<"asdfasdfasdfasdfasdfasd")
							if(not containEpsilon):
								flag=0
								break

						if(alphabate==pro):
							flag=1

					if(flag==1):
						install_follow_follow(findPro,findPro)
				
					# print(False)

						# print(flw)


	# 			for 
	# 	for alter in production[pro]:
	# 		# print(alter[0]<='Z')
	# 		if(alter[len(alter)-1]<='Z' and alter[len(alter)-1]>='A'):
	# 			if(len(alter)>1 and (alter[len(alter)-2]<='Z' and alter[len(alter)-2]>='A')):
	# 				continue
	# 			elif(len(alter)>1):
	# 				# print(alter[1])
	# 				install_trail(pro,alter[len(alter)-2])
	# 		else:
	# 			# print(alter[0])
	# 			install_trail(pro,alter[len(alter)-1])

	# while(len(stack)!=0):
	# 	string = stack.pop(len(stack)-1)#popping (Ba)
	# 	for pro in production:
	# 		for alter in production[pro]:
	# 			if(alter[len(alter)-1]==string[0]):
	# 				install_trail(pro,string[1])


# def rule1(alter):
# 	#if production of the form ALPHA a BETA b GAMMA then a=b
# 	i=0
# 	for alphabate in alter:
# 		if(alphabate<='Z' and alphabate>='A'):
# 			i+=1
# 			continue
# 		elif(len(alter)>i+2 and alter[i+1]<='Z' and alter[i+1]>='A'):
# 			if(len(alter)>i+3 and alter[i+2]<='Z' and alter[i+2]>='A'):
# 				i+=1
# 				continue
# 			else:
# 				parseTable[alphabate+alter[i+2]]='='
# 				i+=1
# 				continue
# 		elif(len(alter)>i+1 and alter[i+1]<='Z'and alter[i+1]>='A'):
# 			i+=1
# 			continue
# 		elif(len(alter)>i+1):
# 			parseTable[alphabate+alter[i+1]]='='

def rule2(pro,alter):
	#production of form aA then a<first(A)
	moveToNextAlpha=False
	i=0
	while(len(alter)>i):
		if(alter[i]<='Z' and alter[i]>='A'):
			for symbol in fst[alter[i]]:
				if symbol=='e':
					if(i+1==len(alter)):
						for each_symbol in flw[alter[i]]:
							parseTable[pro+each_symbol]=pro+" -> "+'e'
						break
					moveToNextAlpha=True
					continue
				parseTable[pro+symbol]=pro+" -> "+alter
			if(not moveToNextAlpha):
				break
		else:
			if(alter[i]=='e'):
				for each_symbol in flw[pro]:
					parseTable[pro+each_symbol]=pro+" -> "+'e'
				break
			parseTable[pro+alter[i]]=pro+" -> "+alter
			break
		i+=1


# def rule3(alter):
# 	#production of form Aa then trailling(A)>a
# 	for i in range(len(alter)):
# 		if(alter[i]<='Z' and alter[i]>='A'):
# 			if(len(alter)>i+1 and alter[i+1]<='Z' and alter[i+1]>='A'):
# 				continue
# 			elif(len(alter)>i+1):
# 				for symbol in t[alter[i]]:
# 					parseTable[symbol+alter[i+1]]='>'
	

def createParseTable():
	#if A->ALPHA repeat rule 2
	for pro in production:
		for alter in production[pro]:
			rule2(pro,alter)
	

# def parseString(input):
# 	print("\n")
# 	currentInputPointer=0
# 	stack.append('$')
# 	while(True):

# 		ch=' '


# 		if(parseTable.get(stack[-1]+input[currentInputPointer])!=None):
# 			ch=parseTable[stack[-1]+input[currentInputPointer]]
# 		print(stack,ch,input[currentInputPointer:],sep='\t')
		
# 		if(stack[-1]=='$' and input[currentInputPointer]=='$'):
# 			print("This String is accepted")
# 			break
# 		else:
# 			#if stack top is '$'' || if symbol on stack top < input[currentInputPointer] then push input[currentInputPointer] onto stack
# 			if(parseTable.get(stack[-1]+input[currentInputPointer])!=None and 
# 				parseTable.get(stack[-1]+input[currentInputPointer])=='<'):
# 				stack.append(input[currentInputPointer])
# 				currentInputPointer+=1
# 			elif(parseTable.get(stack[-1]+input[currentInputPointer])!=None and
# 				parseTable.get(stack[-1]+input[currentInputPointer])=='>'):
# 				while(True):
# 					popped=stack.pop(-1)
# 					# print(popped)
# 					ch=''

# 					if(parseTable.get(stack[-1]+input[currentInputPointer])!=None):
# 						ch=parseTable[stack[-1]+input[currentInputPointer]]
# 					print(stack,ch,input[currentInputPointer:],popped,sep='\t')
# 					if(parseTable.get(stack[-1]+popped)!=None and parseTable[stack[-1]+popped]=='<'):
# 						break
# 			else:
# 				print(currentInputPointer)
# 				print("error")
# 				break

n=int(input("enter no. of productions\n"))
for i in range(n):
	a,b=list(map(str,input().split("->")));
	if(i==0):
		startingSymbol=a
	# print(a,b);
	if(production.get(a)==None):
		production[a]=[b]
	else:
		production[a].append(b)
for pro in production:
	print(pro," -> ",production[pro])
first()
# find first of all RHS i.e keys in the produnction

print("first of each Non terminal is given below")
for i in fst:
	print(i,"-->",fst[i],sep="  ")

#find follow of each non-terminal
follow()

print("follow of each Non terminal is given below\n")
for i in flw:
	print(i,"-->",flw[i],sep="  ")
#now create a parse table
createParseTable()
print("Parse Table \n\n")
for i in parseTable:
	print(i,"-->",parseTable[i],sep="  ")

#now algo for top down parsing
inputString=input("please enter the input string")
#now check whether this string can be parse by the top down parser
# parseString(inputString)