/*          Memory Layout of C Programs
        --------------------------------  <--- High address
        |                               | Command-line arguments and env. variables
        --------------------------------
        |            Stack              | expands downward, towards Heap
        --------------------------------
        |                               | when Stack and Heap meets, the program's free memory is exhausted
        --------------------------------
        |            Heap               | expands upward, towards Stack
        --------------------------------
        |   Uninitialized Data (BSS)    | Initialized to zero at runtime
        --------------------------------
        |       Initialized Data        |
        --------------------------------
        |            Text               | Read from program file
        --------------------------------  <--- Low address
        
    1. Text Segment - executable code of the program's functions and instructions,
            usually read-only to prevent accidental modification during execution.
            Size depends on the number of instructions and the program's complexity.
    2. Data Segment - stores global and static variables of the program, variables
            in this segment retain their values throughout program execution.
            Size depends on the number and type of global/static variables.
        A. Initialized Data Segment - contains static variables initialized by the
                programmer.
        B. Uninitialized Data Segment - stores global and static variables that are
                not initialized by the programmer, initialized to zero at runtime.
    3. Heap Segment - used for dynamic memory allocation, memory is managed using
            functions like malloc(), realloc(), and free. It grows towards higher
            memory address and stack segment. Heap is shared by all shared libraries
            and dynamically loaded modules in a process.
    4. Stack Segment - stores local variables, function parameters, and return
            addresses for each function call. Usually at higher memory addresses and
            grows opposite to the heap. When the stack and heap meet, the program's
            free memory is exhausted.
*/


// First solution
//  Brute force using nested for loop
//  Execution time = 114ms, Memory size = 9.4mb
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {   
    //Set size of returnArray to 2 using memory allocation
    // in malloc, or memory allocation, array will be populated by garbage values
    int* returnArray = (int *) malloc(sizeof(int) * 2);
    
    for (int i = 0; i < numsSize; i++)
    {
        for (int j = i + 1; j < numsSize; j++)
        {
            if ((nums[i] + nums[j]) == target)
            {
                returnArray[0] = i;
                returnArray[1] = j;
            }
        }
    }

    //Set returnSize to 2, this is to inform leetcode test automation that the
    // answer size is 8bytes (2 * int size which is 4bytes)
    *returnSize = 2;
    
    return returnArray;
}

// Second solution
//  Using heap data structure
//  Execution time = 0ms, Memory size = 10.5mb
//create a struct that will become a linked list
struct hashNode {
    int keyValue;   // the value from given array nums
    int index;  // index position of keyValue
    struct hashNode* next;  // creates a linked list to next struct
};

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    //sets hashTable size to twice the size of given numsSize, this will ensure
    // no collision will happen when mapping additional element to the hash table
    int tableSize = numsSize * 2;
    //calloc is used here to take advantage of initializing all elements to 0
    // which is equivalent to a NULL
    //if malloc is used here, a for loop will be needed to set each element to a
    // NULL because malloc initialize elements to garbage values
    struct hashNode** hashTable = calloc(tableSize, sizeof(struct hashNode*));
    //struct hashNode* means a pointer to a single struct hashNode
    //struct hashNode** means a pointer to a pointer to a struct hashNode hence
    // it makes hashTable an array of pointers.
    //Here, hashTable is an array where each slot hashTable[j] is a
    // struct hashNode* (the head of chain)
    
    //returns key to map the given value to hash table
    // a hash function that takes any integer and consistently maps it to valid
    // bucket index.
    int hash(int key)
    {
        return (key % tableSize + tableSize) % tableSize;
    }

    //function that inserts a hash node to a linked list.
    //the first node points to NULL
    //for example, initialized to hashTable[h] -> NULL
    // after first insert it will be hashTable[h] -> node1 -> NULL
    void insert(int key, int index)
    {
        int h = hash(key);
        struct hashNode* node = malloc(sizeof(struct hashNode));
        node->keyValue = key;
        node->index = index;
        node->next = hashTable[h];
        hashTable[h] = node;
    }

    //function to find if the complement is in the hash table
    struct hashNode* find(int key)
    {
        int h = hash(key);
        struct hashNode* node = hashTable[h];
        while (node)
        {
            if (node->keyValue == key) return node;
            node = node->next;
        }
        return NULL;
    }

    int* result = malloc(2 * sizeof(int));

    for (int i = 0; i < numsSize; i++)
    {
        int complement = target - nums[i];

        struct hashNode* node = find(complement);

        if (node)
        {
            //-> means a pointer to struct, it can be use to access field inside
            // that struct.
            //-> is an operator in which is the as (*pointer).field so below
            // node->index is equal to (*node).index
            result[0] = node->index;
            result[1] = i;

            *returnSize = 2;
            return result;
        }

        insert(nums[i], i);
    }

    *returnSize = 0;
    return NULL;
}