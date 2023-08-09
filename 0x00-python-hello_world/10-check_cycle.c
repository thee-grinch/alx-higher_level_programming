#include "lists.h"
/**
 * check_cycle - used to check a cycle in a linked list
 * @list: the linked list to be checked
 * Return: cycle present: 1 else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;
	if (!list)
		return (0);
	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (second == first)
			return (1);
	}
	return (0);
}
