#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <assert.h>
#include "bucketstack.h"

//struct NodeBucket {
//	char** val;
//	struct NodeBucket* next;
//};

//typedef struct {
//	struct NodeBucket* firstBucket;
//	int topElt;
//	int bucketSize;
//} Stack;

void initStack (int bucketSize, Stack **stack){
	(*stack)=malloc(sizeof(Stack));
	(*stack)->firstBucket=NULL;
	(*stack)->topElt=-1;
	(*stack)->bucketSize=bucketSize;
}
bool isEmpty (const Stack *stack){
	if(stack->firstBucket==NULL)
		return true;
	return false;
}
void push (char* val, Stack *stack){
	if(stack->firstBucket==NULL){
		struct NodeBucket *newbucket;
		newbucket=malloc(sizeof(struct NodeBucket));
		newbucket->next=NULL;
		newbucket->val=malloc(sizeof(char*)*stack->bucketSize);
		newbucket->val[0]=malloc(strlen(val)+1);
		strcpy(newbucket->val[0],val);
		//printf("%s",newbucket->val[0]);
		//newbucket->next=NULL;
		stack->topElt=0;
		stack->firstBucket=newbucket;

	}
	else if(stack->topElt==(stack->bucketSize)-1){
		struct NodeBucket *newbucket;
		newbucket=malloc(sizeof(struct NodeBucket));
		newbucket->val=malloc(sizeof(char*)*stack->bucketSize);
		newbucket->val[0]=malloc(strlen(val)+1);
		strcpy(newbucket->val[0],val);
		newbucket->next=stack->firstBucket;
		stack->firstBucket=newbucket;
		stack->topElt=0;
	}
	else{
		stack->topElt=stack->topElt+1;
		stack->firstBucket->val[stack->topElt]=malloc(strlen(val)+1);
		strcpy(stack->firstBucket->val[stack->topElt],val);
	}
}
void pop(Stack *stack){
	assert(stack->firstBucket!=NULL);
	if(stack->topElt==0){
		struct NodeBucket *temp;
		free(stack->firstBucket->val[0]);
		free(stack->firstBucket->val);
		temp=stack->firstBucket;
		//free(stack->firstBucket);
		stack->firstBucket=temp->next;
		free(temp);
		stack->topElt=stack->bucketSize-1;
	}
	else{
		free(stack->firstBucket->val[stack->topElt]);
		stack->topElt=stack->topElt-1;
	}
}
int size (const Stack *stack){
	int s_size=0;
	int b_size;
	b_size=stack->bucketSize;
	struct NodeBucket *cursor;
	if(stack->firstBucket==NULL)
		return 0;
	else
		cursor=stack->firstBucket->next;
	for(;cursor!=NULL;cursor=cursor->next){
		s_size=s_size+b_size;
	}
	return (s_size+(stack->topElt+1));
}
char* top (const Stack *stack){
	assert(stack->firstBucket!=NULL);
	struct NodeBucket *cursor;
	cursor=stack->firstBucket;
	return(cursor->val[stack->topElt]);
}
void swap (Stack *stack){
	assert(size(stack)>=2 && (stack->firstBucket!=NULL));
	if(stack->topElt==0){
		char *temp1;
		char *temp2;
		char *temp_alloc;
		temp1=stack->firstBucket->val[0];
		temp2=stack->firstBucket->next->val[stack->bucketSize-1];
//		stack->firstBucket->val[0]=realloc(stack->firstBucket->val[0],strlen(temp2)+1);
		temp_alloc=malloc(strlen(temp1)+1);
		strcpy(temp_alloc,temp1);
//		strcpy(stack->firstBucket->val[0],temp2);
//		stack->firstBucket->val[0]=cursor->val[stack->bucketSize-1];
//		stack->firstBucket->next->val[stack->bucketSize-1]=realloc(stack->firstBucket->next->val[stack->bucketSize-1],strlen(temp_alloc)+1);

//		strcpy(stack->firstBucket->next->val[stack->bucketSize-1],temp_alloc);
		free(stack->firstBucket->val[0]);
		stack->firstBucket->val[0] = temp2;
		stack->firstBucket->next->val[stack->bucketSize-1]=temp_alloc;
//		free(temp_alloc);
	}
	else{
		char *temp1;
		char *temp2;
		temp1=stack->firstBucket->val[stack->topElt];
		char *temp_alloc=malloc(strlen(temp1)+1);
		temp2=stack->firstBucket->val[(stack->topElt)-1];
//		stack->firstBucket->val[stack->topElt]=realloc(stack->firstBucket->val[stack->topElt],strlen(temp2)+1);
		strcpy(temp_alloc,temp1);
//		strcpy(stack->firstBucket->val[stack->topElt],temp2);
//		stack->firstBucket->val[(stack->topElt)-1]=realloc(stack->firstBucket->val[(stack->topElt)-1],strlen(temp_alloc)+1);
//		strcpy(stack->firstBucket->val[(stack->topElt)-1],temp_alloc);
		free(stack->firstBucket->val[stack->topElt]);
		stack->firstBucket->val[stack->topElt]=temp2;
		stack->firstBucket->val[stack->topElt-1]=temp_alloc;
//		free(temp_alloc);
	}
}
void print (const Stack *stack){
	struct NodeBucket *cursor;
	cursor=stack->firstBucket;
	int top=stack->topElt;
	int i=0;
	printf("stack is:\n");
	for(;cursor!=NULL;cursor=cursor->next,i++){
		if(i>0)
			top=stack->bucketSize-1;
		for(;top>=0;top=top-1){
			printf("	%s\n",cursor->val[top]);
		}
	}
}
void clear(Stack *stack){
	struct NodeBucket *cursor;
	cursor=stack->firstBucket;
	int top=stack->topElt;
	struct NodeBucket *temp;
	int i=0;
	for(;cursor!=NULL;cursor=temp,i++){
		temp=cursor->next;
		if(i>0)
			top=stack->bucketSize-1;
		for(;top>=0;top=top-1){
			free(cursor->val[top]);
		}
		free(cursor->val);	
		free(cursor);

	}
	stack->firstBucket=NULL;
	stack->topElt=-1;

}
void destroyStack(Stack **stack){
	clear(*stack);
	free(*stack);
	(*stack)=NULL;
}
