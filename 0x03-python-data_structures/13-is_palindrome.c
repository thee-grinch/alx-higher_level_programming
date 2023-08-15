#include "lists.h"
/**
 * is_palindrome - checks whether a string is a palindrome
 * @head: pointer to the head of the linked list
 * Return: returns 1 if true or otherwise 0
 */
int is_palindrome(listint_t **head)
{
	int len, i, j, *datas;
	listint_t *buffer;

	if (!(*head))
		return (1);
	len = 0;
	buffer = *head;
	while (buffer->next)
	{
		len++;
		buffer = buffer->next;
	}
	datas = malloc(len * sizeof(int));
	if (datas == NULL)
		return (0);
	buffer = *head;
	for (i = 0; buffer != NULL; i++)
	{
		datas[i] = buffer->n;
		buffer = buffer->next;
	}
	i--;
	for (j = 0; j <= (len / 2); j++)
	{
		if (datas[j] == datas[i])
			i--;
		else
		{
			free(datas);
			return (0);
		}
	}
	free(datas);
	return (1);
}
