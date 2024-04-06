#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int testCharManipulation(char *stringInput);
int printVowels(char *stringInput);
int protoMemory();

int main(int argc, char *argv[])
{
    printf("Hellow World!\n");

   char *stringData = "String data...";
    testCharManipulation(stringData);
 //   testCharManipulation("This is data.\n");
  
    printVowels(stringData);

    protoMemory();

    return 1;
}


int testCharManipulation(char *myData)
{
    printf("Original data string:\t\t%s\n", myData);
    printf("Reverse character string:\t");
    for (int i = strlen(myData); i >= 0; --i) 
    {
      printf("%c", myData[i]);
      //
    }  
    printf("\n");
    return 0;
}

int printVowels(char *myData)
{
    printf("Original data string:\t\t%s\n", myData);
    printf("Reverse character string:\t");
    for (int i = strlen(myData); i >= 0; --i) 
    {
        char c = tolower(myData[i]);   // doing this as I dont need to check separately for uppercase and lowercase 
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') 
        {
            printf("%c",myData[i]); // using str[i] instead of c because c is always lowercase where as str[i] stores the actaul case 
        }
      //  printf("%c", myData[i]);
      //
    }  
    printf("\n");
    return 0;


}


int protoMemory()
{
  int i,n;
  char * buffer;

  printf ("How long do you want the string? ");
  scanf ("%d", &i);

  buffer = (char*) malloc (i+1);
  if (buffer==NULL) exit (1);

  for (n=0; n<i; n++)
  buffer[n]=rand()%26+'a';
  buffer[i]='\0';

  printf ("Random string: %s\n",buffer);
  free (buffer);

  return 0;
}
