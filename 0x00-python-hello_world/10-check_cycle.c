#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: head linked list in traversal
 * Return: 1 if last 2 nodes before the Null corrolate in
 * several instances, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
    listint_t *sloth, *the_flash;
    sloth, the_flash = list;


    while (the_flash != NULL && the_flash->next != NULL)
    {
        sloth = sloth->next;
        the_flash = the_flash->next;
        the_flash = the_flash->next;

        if (sloth == the_flash)
            return (1);
    }

    return (0);
}
