#include "lists.h"
/**
* insert_node - Inserting a num to a sorted singly-linked list.
* @head: A pointer the head of the linked list.
* @number: The number to insert.
* 
* Return: If the function fails - NULL.
* Otherwise - a pointer to the new node.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *curr;
	curr = malloc(sizeof(listint_t));
	if (curr == NULL)
		return (NULL);
	curr->n = number;
	if (node == NULL || node->n >= number)
	{
		curr->next = node;
		*head = curr;
		return (curr);
	}
	
	while (node && node->next && node->next->n < number)
		node = node->next;
	curr->next = node->next;
	node->next = curr;
	return (curr);
}
