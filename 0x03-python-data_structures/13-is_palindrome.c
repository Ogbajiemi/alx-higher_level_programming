#include "lists.h"
/**
 * palindrome - verify wether or not its palindrome with recursion
 * @l: l
 * @r: r
 *
 * Return: 1 palindrome, 0 not palindrome
 */

int palindrome(listint_t **l, listint_t *r)
{
	int ans;

	if (r != NULL)
	{
		ans = palindrome(l, r->next);
		if (ans != 0)
		{
			ans = (r->n == (*l)->n);
			*l = (*l)->next;
			return (ans);
		}
		return (0);

	}
	return (1);
}

/**
 * is_palindrome - confirm if a singly linked list is a palindrome.
 * @head: head of linked list
 *
 * Return: 1 palindrome, 0 not palindrome
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}
