#include <stdio.h>
#define SIZE 5

int stack[SIZE];
int top = -1;
void push(int el)
{
    if (top < SIZE - 1)
    {
        top = top + 1;
        stack[top] = el;
    }
    else
    {
        printf("STACK OVERFLOW\n");
    }
}

int pop()
{
    if (top >= 0)
    {
        top = top - 1;
        int item = stack[top];
        return item;
    }
    else
    {
        printf("STACK UNDERFLOW\n");
    }
}

void display()
{
    for (int i = 0; i <= top; i++)
    {
        printf("%d\t", stack[i]);
    }
    printf("\n");
}

int main()
{
    push(5);
    push(6);
    push(7);
    push(8);
    pop();
    pop();
    push(1);
    display();
    return 0;
}