#include "lists.h"

/**
 * insert_node - includes a anumber to s sorted linked list.
 * @head: this exhibts a pointer to the head of the structure.
 * @number: The number to inserted.
 * Return: A pointer to the new node, or NULL if -1
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (temp->next != NULL && temp->next->n < number)
		temp = temp->next;

	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}
