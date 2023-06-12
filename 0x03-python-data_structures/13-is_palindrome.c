#include <stdio.h>

node_t *node;
int a [2];
int i = 0;
int j;
j = len (1) - 1;

for (i = 0; i < j; i++);

if (a[i] != (j- 1)




listint_t *curr, *prev = NULL, *next;

	curr = head;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	return (prev);