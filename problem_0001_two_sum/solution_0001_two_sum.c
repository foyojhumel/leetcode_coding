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
    4. 













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

    *returnSize = 2;
    
    return returnArray;
}