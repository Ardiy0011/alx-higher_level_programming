#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Head pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev, *next, *mid, *curr;

    if (!(*head) || !((*head)->next))
        return (1);

    slow = *head;
    fast = *head;

    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }
    prev = NULL;
    curr = slow;
    while (curr)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    mid = prev;
    while (*head && mid)
    {
        if ((*head)->n != mid->n)
            return (0);
        *head = (*head)->next;
        mid = mid->next;
    }

    return (1);
}
