
 20 #include <stdio.h>
 21 #include <stdlib.h>
 22 #include <string.h>
 23 #include <stdbool.h>
 24 void encrypt(FILE *fp2,int input_file,int input_num,char plain[26],char cipher[26]);
 25 void decrypt(FILE *fp2,int input_file,int input_num,char plain[26],char cipher[26]);
 26 int main(int argc, char *argv[]) {
 27     int i;
 28     int j;
 29     int mapping;   //will be index for mapping csv file
 30     int input_file; //will be the index for the input_file argument
 31     int mode;//index for mode
 32     int line_count=0;
 33     int el;
 34 //  int a;
 35     int let_count_1=0;
 36     int let_count_2=0;
 37     FILE *fp1;
 38     FILE *fp2;
 39 //  char alphabet[26]={'a'};
 40     char plain[26]={'2'};
 41     char cipher[26]={'2'};
 42     // start of command line argument analysis
 43     if(argc>7 || argc<7){
 44         fprintf(stderr,"Usage: ./encrypt -t <mappingfile> -m <encryption mode> -i <inputfile>");
 45         exit(7);
 46     }
 47     for (i=1;i<6;i=i+2)
 48     {
 49         if(strcmp(argv[i],"-t")==0){
 50             mapping=i+1;
 51             //gives length of total argument
 52             int size= strlen(argv[mapping]);
 53             /*const char is a mutable pointer, it allows us to point to the last 3
 54             characters of the arg, then compare */
 55             const char *ext= &argv[mapping][size-3];
 56             //checking if last 3 chars after . are csv
 57             if(strcmp(ext,"csv")!=0){
 58                 fprintf(stderr,"Usage: ./encrypt -t <mappingfile> -m <encryption mode> -i <inputfile>");
 59                 exit(7);
 60             }
 61
 62         }
 63         else if(strcmp(argv[i],"-i")==0){
 64             input_file=i+1;
 65             int len= strlen(argv[input_file]);
