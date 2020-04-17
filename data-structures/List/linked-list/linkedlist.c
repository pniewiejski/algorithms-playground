#include <stdlib.h>
#include <stdio.h>

struct node
{
    int value;
    struct node * next;
};

typedef struct node node_t;

node_t * create_node(int value, node_t * next_node) {
    node_t * node = (node_t *) malloc(sizeof(node_t));
    if (node == NULL) {
        printf("Error: could not allocate memory for a new node");
        exit(EXIT_FAILURE);
    }

    node->next = next_node;
    node->value = value;

    return node;
}

node_t * prepend(node_t * head, int value) {
    node_t * new_head = create_node(value, head);
    head = new_head;
    
    return head;
}

node_t * append(node_t * head, int value) {
    node_t * cursor = head;
    while (cursor->next != NULL)
        cursor = cursor->next;

    node_t * new_node = create_node(value, NULL);
    cursor->next = new_node;

    return head;
}

node_t * reverse(node_t * head) {
    node_t * previous = NULL;
    node_t * current = head;

    while (current != NULL) {
        node_t * tmp = current->next;
        current->next = previous;
        previous = current;
        current = tmp;
    }

    head = previous;

    return head;
}

void print(node_t * head) {
    node_t * cursor = head;
    printf("--> Printing linked list. Starting from: %p\n", head);
    while (cursor != NULL)
    {
        printf("\tElement at %p; value: %d\n", cursor, cursor->value);
        cursor = cursor->next;
    }
    printf("<-- Printing linked list done\n");
}

int main() {
    node_t * head = create_node(1, NULL);
    head = append(head, 2);
    head = append(head, 3);
    head = prepend(head, 0);
    print(head);
    return 0;
}