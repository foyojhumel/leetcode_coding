//First Solution
// using linked list
// Execution time = 3ms, Memory size = 13.5ms

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    //no need to set the size since it is a linked list and not an array
    //starting point of the linked list
    //dummy is struct variable, not a pointer
    //initialize its val to 0 and next to NULL, 0 -> NULL
    struct ListNode dummy = {0, NULL};
    //a pointer variable pointing to the address of dummy
    struct ListNode* current = &dummy;

    //initialized carry to 0 this will handle 
    int carry = 0;

    //l1 and l2 are already pointers pointing to the head node, so it can
    // used directly here
    while (l1 || l2 || carry)
    {
        //ternary operator, if l1 or l2 is not NULL use that value otherwise
        // use 0
        int num1 = (l1 ? l1->val : 0);
        int num2 = (l2 ? l2->val : 0);

        int sub_total = num1 + num2 + carry;
        carry = sub_total / 10; 

        //initialize the new node
        struct ListNode* newNode = malloc(sizeof(struct ListNode));
        newNode->val = sub_total % 10;
        //this is important! if newNode->next is not set to NULL it will point
        // to a garbage value or worse, an address that is used by other variable
        newNode->next = NULL;

        //link the newNode to the result nodes or linked list results
        //points to newNode first
        current->next = newNode;
        //then move the pointer to the new node
        current = newNode;

        //if l1 is valid and not NULL, move to the next node
        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }

    //only return the resulting values of linked list
    //dummy.next is used because it points to the resulting to values
    //dummy is just the placeholder so we can know where we can get the result
    return dummy.next;
}