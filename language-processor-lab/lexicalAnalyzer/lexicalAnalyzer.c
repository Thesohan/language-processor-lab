#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
 
int isKeyword(char A[]){
	char keywords[34][10] = {"printf","scanf","auto","break","case","char","const","continue","default",
							"do","double","else","enum","extern","float","for","goto",
							"if","int","long","register","return","short","signed",
							"sizeof","static","struct","switch","typedef","union",
							"unsigned","void","volatile","while"};
	int i, flag = 0;

	
	for(i = 0; i < 32; ++i){
		if(strcmp(keywords[i], A) == 0){
			flag = 1;
			break;
		}
	}
	return flag;
}
 
int main(){
	char ch, str[1000], A[100], operators[] = "+-*/%=",delimeters[]="(){}[]";
	FILE *fp1,*fp2;
	int i,j=0;
	
	fp1 = fopen("code.cpp","r");
	fp2=fopen("output.txt","w");
	
	if(fp1 == NULL){
		printf("error while opening the file\n");
		exit(0);
	}
	
	while((ch = fgetc(fp1)) != EOF){
		if(ch=='"'){
			int k=0;
			str[k++]=ch;
			while((ch=fgetc(fp1))!='"'){
				str[k++]=ch;
			}
			str[k++]=ch;
			str[k]='\0';
			fprintf(fp2,"%s \t String \n",str);
				A[j] = '\0';
   				j = 0;
   				if(isKeyword(A) == 1)
   					fprintf(fp2,"%s \t keyword \n",A);
   				else
   					fprintf(fp2,"%s \t indentifier \n",A);
		}
		else if(isalnum(ch)){
   			A[j++] = ch;
   			// printf("hello");
   		}
   		else if((ch == ' ' || ch == '\n') && (j != 0)){
   				A[j] = '\0';
   				j = 0;
   				   				
   				if(isKeyword(A) == 1)
   					fprintf(fp2,"%s \t keyword \n",A);
   				else
   					fprintf(fp2,"%s \t indentifier \n",A);
   		}
   		else{
   	
   		 for(i = 0; i < 6; ++i){
   			
   			if(ch == operators[i]){
   				fprintf(fp2,"%c \t operator \n",ch);
   				A[j] = '\0';
   				j = 0;
   				if(isKeyword(A) == 1)
   					fprintf(fp2,"%s \t keyword \n",A);
   				else
   					fprintf(fp2,"%s \t indentifier \n",A);	
   			}
   			}
   		}
	}
	
	fclose(fp1);
	fclose(fp2);
	return 0;
}