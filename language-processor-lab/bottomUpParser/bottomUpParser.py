production={}#all the productions
stack=[]#stack used for calculating leading  and trailing
l={}#it will contain the leading of each nonTerminal
t={}#it will contain the trailling of each nonTerminal
parseTable={}#it is our parseTable , there will be no values for error
def install_lead(nonTerminal,terminal):
	# print(terminal)
	if(l.get(nonTerminal)==None):
		l[nonTerminal]=[terminal]
		stack.append(nonTerminal+terminal)#pushing (A,a) into stack
		# print(alter[1])
	elif(terminal not in l.get(nonTerminal)):
		l[nonTerminal].append(terminal)
		stack.append(nonTerminal+terminal)#pushing (A,a) into stack
		
def leading():

	for pro in production: #for each production of the form A->aALPHA OR A->BaALPHA install(A,a)
		for alter in production[pro]:
			# print(alter[0]<='Z')
			if(alter[0]<='Z' and alter[0]>='A'):
				if(len(alter)>1 and (alter[1]<='Z' and alter[1]>='A')):
					continue
				elif(len(alter)>1):
					# print(alter[1])
					install_lead(pro,alter[1])
			else:
				# print(alter[0])
				install_lead(pro,alter[0])

	while(len(stack)!=0):
		string = stack.pop(len(stack)-1)#popping (Ba)
		for pro in production:
			for alter in production[pro]:
				if(alter[0]==string[0]):
					install_lead(pro,string[1])


def install_trail(nonTerminal,terminal):
	# print(terminal)
	if(t.get(nonTerminal)==None):
		t[nonTerminal]=[terminal]
		stack.append(nonTerminal+terminal)#pushing (A,a) into stack
		# print(alter[1])
	elif(terminal not in t.get(nonTerminal)):
		t[nonTerminal].append(terminal)
		stack.append(nonTerminal+terminal)#pushing (A,a) into stack
		

def trailing():

	for pro in production: #for each production of the form A->aALPHA OR A->BaALPHA install(A,a)
		for alter in production[pro]:
			# print(alter[0]<='Z')
			if(alter[len(alter)-1]<='Z' and alter[len(alter)-1]>='A'):
				if(len(alter)>1 and (alter[len(alter)-2]<='Z' and alter[len(alter)-2]>='A')):
					continue
				elif(len(alter)>1):
					# print(alter[1])
					install_trail(pro,alter[len(alter)-2])
			else:
				# print(alter[0])
				install_trail(pro,alter[len(alter)-1])

	while(len(stack)!=0):
		string = stack.pop(len(stack)-1)#popping (Ba)
		for pro in production:
			for alter in production[pro]:
				if(alter[len(alter)-1]==string[0]):
					install_trail(pro,string[1])


def rule1(alter):
	#if production of the form ALPHA a BETA b GAMMA then a=b
	i=0
	for alphabate in alter:
		if(alphabate<='Z' and alphabate>='A'):
			i+=1
			continue
		elif(len(alter)>i+2 and alter[i+1]<='Z' and alter[i+1]>='A'):
			if(len(alter)>i+3 and alter[i+2]<='Z' and alter[i+2]>='A'):
				i+=1
				continue
			else:
				parseTable[alphabate+alter[i+2]]='='
				i+=1
				continue
		elif(len(alter)>i+1 and alter[i+1]<='Z'and alter[i+1]>='A'):
			i+=1
			continue
		elif(len(alter)>i+1):
			parseTable[alphabate+alter[i+1]]='='

def rule2(alter):
	#production of form aA then a<leading(A)
	for i in range(len(alter)):
		if(alter[i]<='Z' and alter[i]>='A'):
			continue
		elif(len(alter)>i+1 and alter[i+1]<='Z' and alter[i+1]>='A'):
			for symbol in l[alter[i+1]]:
				parseTable[alter[i]+symbol]='<'


def rule3(alter):
	#production of form Aa then trailling(A)>a
	for i in range(len(alter)):
		if(alter[i]<='Z' and alter[i]>='A'):
			if(len(alter)>i+1 and alter[i+1]<='Z' and alter[i+1]>='A'):
				continue
			elif(len(alter)>i+1):
				for symbol in t[alter[i]]:
					parseTable[symbol+alter[i+1]]='>'
	

def createParseTable():
	#if A->ALPHA a Beta b Gamma then a=b
	for pro in production:
		for alter in production[pro]:
			rule1(alter)
			rule2(alter)
			rule3(alter)
			for alphabate in alter:
				if(alphabate<='Z' and alphabate>='A' and alphabate=='c' and alphabate==')'):
					continue
				else:
					#since $ has fix priority
					parseTable[alphabate+'$']='>'
					parseTable['$'+alphabate]='<'


def parseString(input):
	print("\n")
	currentInputPointer=0
	stack.append('$')
	while(True):

		ch=' '


		if(parseTable.get(stack[-1]+input[currentInputPointer])!=None):
			ch=parseTable[stack[-1]+input[currentInputPointer]]
		print(stack,ch,input[currentInputPointer:],sep='\t')
		
		if(stack[-1]=='$' and input[currentInputPointer]=='$'):
			print("This String is accepted")
			break
		else:
			#if stack top is '$'' || if symbol on stack top < input[currentInputPointer] then push input[currentInputPointer] onto stack
			if(parseTable.get(stack[-1]+input[currentInputPointer])!=None and 
				parseTable.get(stack[-1]+input[currentInputPointer])=='<'):
				stack.append(input[currentInputPointer])
				currentInputPointer+=1
			elif(parseTable.get(stack[-1]+input[currentInputPointer])!=None and
				parseTable.get(stack[-1]+input[currentInputPointer])=='>'):
				while(True):
					popped=stack.pop(-1)
					# print(popped)
					ch=''

					if(parseTable.get(stack[-1]+input[currentInputPointer])!=None):
						ch=parseTable[stack[-1]+input[currentInputPointer]]
					print(stack,ch,input[currentInputPointer:],popped,sep='\t')
					if(parseTable.get(stack[-1]+popped)!=None and parseTable[stack[-1]+popped]=='<'):
						break
			else:
				print(currentInputPointer)
				print("error")
				break

n=int(input("enter no. of productions\n"))
for i in range(n):
	a,b=list(map(str,input().split("->")));
	# print(a,b);
	if(production.get(a)==None):
		production[a]=[b]
	else:
		production[a].append(b)
# print(production)
leading()

print("leading of each Non terminal is given below")
for i in l:
	print(i,"-->",l[i],sep="  ")
#find leading of all RHS i.e keys in the produnction

trailing()

print("trailling of each Non terminal is given below\n")
for i in t:
	print(i,"-->",t[i],sep="  ")
#now create a parse table
createParseTable()
print("Parse Table \n\n")
for i in parseTable:
	print(i,"-->",parseTable[i],sep="  ")

#now algo for operator preceding parser
inputString=input("please enter the input string")
#now check whether this string can be parse by the bottom up parser
parseString(inputString)