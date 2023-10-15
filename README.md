--------------------------                      --------------------------


                Project 2 -  Page Replacement Algorithm(s)


-------------------------- Program Description: --------------------------


        Simulates 3 page replacement algorithms to gain
        knowledge and experience in memory management for 
        Operating Systems and other applications.

--------------------------                     --------------------------

-------------------------- How To Run --------------------------

    The format:     python3 <PRA.py> <Physical Memory Size> <Input File>
    For WSClock inlude <tau>  in the command's execution, example below...

    In terminal, execute: python3    fifo.py 10   page.txt
                          python3 optimal.py 10   page.txt
                          python3 wsclock.py 10 5 page.txt
    

--------------------------           --------------------------


                The Page Replacement Algorithm(s)


    First-In First-Out: When the physical memory is full, simply pops the first
    element in the physical's memory, then appends the Virtual's item to the end 
    of the list.


    Optimal: The algorithm searches which memory doesn't repeat anymore
    in the Virtual memory, if it doesn't then replace that page,
    else it'll parse which page repeats last (longest in the VM) 
    and replaces that one.


    WSClock: The algorithm parses through the list, in a circular matter
    the pages in a data structure with three data,
        - Element
        - Time of Last Access
        - Reference Bit

    The element is the page's content, read from the input file.
    Time of Last Access is when the Page was last accessed, in Virtual Time
    Reference Bit tells if the Page was previously refered, that is if the
    OS wanted to write a page or read a page that is already present.

    The algorithm replaces the page that hasn't been referenced 
    and has the highest time of last accessed (hasn't been accessed the longest).


--------------------------           --------------------------




--------------------------           --------------------------

Expected output:

    fifo.py 
    > Pages present in the physical memory
    > Page Fault Count

    i.e

Physical Memory: [-3, 2, 41, 15, 81, 3, 4, 7, 8, 9]

Total Page Faults: 22

Similar results for the other two PRA(s).






References & Resources used:

    [Official Resources]:
        Modern Operating System 4th Ed by Tanenbaum
        
    [Unofficial Resources]:
    
        Page Replacement Algorithms in Operating Systems
        https://www.geeksforgeeks.org/page-replacement-algorithms-in-operating-systems/
    
        WSCLOCK—a simple and effective algorithm for virtual memory management
        https://dl.acm.org/doi/pdf/10.1145/800216.806596

        WSClock algorithm as approximation
        https://stackoverflow.com/questions/34091165/wsclock-algorithm-as-approximation



                        __
                     -=(o '.
                        '.-.\
                        /|  \\
                        '|  ||
                         _\_):,_
_____________________________________________________
