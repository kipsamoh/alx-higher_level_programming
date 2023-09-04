#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *_slow = list;
	listint_t *_fast = list;

	if (!list)
		return (0);

	while (_slow && _fast && _fast->next)
	{
		_slow = _slow->next;
		_fast = _fast->next->next;
		if (_slow == _fast)
			return (1);
	}

	return (0);
}

