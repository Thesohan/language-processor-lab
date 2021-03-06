#include<stdio.h>
#include<string.h>
#include<ctype.h>
void main(){
	FILE *fin,*fout,*fsym;
	int sAddress=0,iAddress=0;//variable for storing starting address and current address of instructions
	char lebel[20],opcode[20],operand[30];
	fin=fopen("IN.txt","r");
	fout=fopen("output.txt","w");
	fsym=fopen("symbol.txt","w");
	fscanf(fin,"%s%s%s",lebel,opcode,operand);//scan space saperated values from fin file pointer 
	while(strcmp(opcode,"END")){
		
		if(strcmp("**",lebel)){
			fprintf(fsym,"%s %d \n",lebel,sAddress);
				
		}
		if(!strcmp(opcode,"START")){
			sscanf(operand, "%d", &sAddress);
			iAddress=sAddress;
		//printf("%d",sAddress);
		//fprintf(fout,"%d ",sAddress);
			fprintf(fout,"%s %s %s\n",lebel,opcode,operand );
		}

		else{
			if(!strcmp(opcode,"RESW")){
				fprintf(fout,"%d %s %s %s\n",sAddress,lebel,opcode,operand );
				int words;
				sscanf(operand,"%d",&words);
				sAddress+=3*words;
			}
			else if(!strcmp(opcode,"BYTE")){
				fprintf(fout,"%d %s %s %s\n",sAddress,lebel,opcode,operand );
				char byte[20];
				sscanf(operand,"%s",byte);
				sAddress+=strlen(byte)-3;
			}
			else if(!strcmp(opcode,"RESB")){
				fprintf(fout,"%d %s %s %s\n",sAddress,lebel,opcode,operand );
				int byte;
				sscanf(operand,"%d",&byte);
				sAddress+=byte;
				//printf("%d",byte);
			}
			else{
				fprintf(fout,"%d %s %s %s\n",sAddress,lebel,opcode,operand );
				// char byte;
				// sscanf(operand,"%d",&byte);
				sAddress+=3;	
			}

		}
		fscanf(fin,"%s%s%s",lebel,opcode,operand);
//	printf("%s\n",opcode );
	}
				fprintf(fout,"%d %s %s %s\n",sAddress,lebel,opcode,operand );
				fprintf(fout, "length of the program is = %d\n",sAddress-iAddress );
				fclose(fout);
				fclose(fin);
				fclose(fsym);
}