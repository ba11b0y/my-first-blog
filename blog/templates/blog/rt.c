#include<stdio.h>
#include<malloc.h>
#include<string.h>
struct node
{
    char data[20];
    struct node* left;
    struct node* right;
};
struct node* root;
struct node* create_newptr(char d[])
{
    int i,l;
    l=strlen(d);
    struct node* newptr=(struct node*)malloc(sizeof(struct node));
    for(i=0; i<l; i++)
    {
        newptr->data[i]=d[i];
    }
    newptr->data[i+1]='\0';
    newptr->left=NULL;
    newptr->right=NULL;
    return newptr;
}
struct node* insert_data(struct node* rootptr,char d[])
{
    if(rootptr==NULL)
    {
        rootptr=create_newptr(d);
        return rootptr;
    }
    else if((strlen(d))>=(strlen(rootptr->data)))
    {
        rootptr->right=insert_data(rootptr->right,d);
    }
    else
    {
        rootptr->left=insert_data(rootptr->left,d);
    }
    return rootptr;
}
struct node* findmin(struct node* root)
{
	while(root->left != NULL) root = root->left;
	return root;
}
struct node* Delete(struct node *root, char deldata[]) {
	if(root == NULL) return root;
	else if(strlen(deldata) < strlen(root->data)) root->left = Delete(root->left,deldata);
	else if (strlen(deldata) > strlen(root->data)) root->right = Delete(root->right,deldata);
	else {
		// Case 1:  No child
		if(root->left == NULL && root->right == NULL) {
			free(root);
			root = NULL;
		}
		//Case 2: One child
		else if(root->left == NULL) {
			struct node *temp = root;
			root = root->right;
			free(temp);
		}
		else if(root->right == NULL) {
			struct node *temp = root;
			root = root->left;
			free(temp);
		}
		// case 3: 2 children
		else {
			struct node* temp;
			temp = findmin(root->right);
			strcpy(root->data,temp->data);
			root->right = Delete(root->right,temp->data);
		}
	}
	return root;
}
int main()
{
    int choice,ndata,i;
    char rdata[20],cdata[20];
    root=NULL;
    do
    {
        printf("\n\nChoose among the following\n1.Create tree\n2.Delete node\n3.Exit\n");
        scanf("%d",&choice);
        switch(choice)
        {
        case 1:
            printf("\nEnter data as a string to insert in root node:\n");
            scanf("%s",&rdata);
            root=insert_data(root,rdata);
            printf("\nTree created with %s as the root node:",rdata);
            printf("\nEnter how many data you want to insert:");
            scanf("%d",&ndata);
            for(i=0; i<ndata; i++)
            {
                printf("\nEnter child data as string:");
                scanf("%s",&cdata);
                root=insert_data(root,cdata);
            }
            printf("\n\n\nTree Created!!\n");
            break;
        case 2:
            printf("\nEnter data to be deleted\n");
            scanf("%s",&rdata);
            Delete(root,rdata);
            break;

        }
    }
    while(choice!=3);
}
