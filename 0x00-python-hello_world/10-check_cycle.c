#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list is a cycle
 * Return: 0 if no cycle, 1 is yes
 */
int check_cycle(listint_t *list)
{
	listint_t *shift_2 = list;
	listint_t *shift_1 = list;

	if (!list)
		return (0);

	while (1)
	{
		/*traverse through nodes as long as linked list node exists*/
		if (shift_2->next != NULL && shift_2->next->next != NULL)
		{
			shift_2 = shift_2->next->next;
			shift_1 = shift_1->next;

			if (shift_2 == shift_1)
				return (1);
		}
		else
			return (0);
	}

}
