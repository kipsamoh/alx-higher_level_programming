#include "lists.h"

/**
 * insert_node - Inserts a _number into a sorted singly-linked list.
 * @head: A pointer the head of the _linked list.
 * @number: The _number to insert.
 *
 * Return: If the _function fails - NULL.
 * Otherwise - a _pointer to the _new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
