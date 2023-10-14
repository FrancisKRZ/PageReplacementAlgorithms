# First-In, First-Out

# The simplest page replacement algorithm. 
# The operating system maintains a queue for all of the memory pages in this method, 
# with the oldest page at the front of the queue. 
# The first page in the queue is chosen for removal when a page has to be replaced.



# How to run:       python3 fifo.py <num of phys page> access sequence file
#                   python3 fifo.py 10 input.txt

import sys

class FIFO():

    # Initiazes with given data, physical memory size and the input file's name
    def __init__(self, physicalMemorySize, fileName):
        
        self.physicalMemorySize = physicalMemorySize
        self.fileName = fileName


    # method used to read the content from file and copy them to an array
    # this could be optional but it is needed with my optimal's implementation
    def read(self):

        content = []

        # Open file
        with open(self.fileName, 'r') as file:
            # Read each line
            for line in file:
                # Reading words
                for word in line.split():
                    content.append( int(word.split(':')[1]))

        # Responsibly close the file after use (+90 pts bonus)
        file.close()

        return content


    # Run's the Page Replacement Algorithm
    def run(self):

        # Page Fault counter
        pgFault = 0

        # List / physicalMemory
        physicalMemory = [] * self.physicalMemorySize
        # Calls the method to copy the content from the input file
        virtualMemory = self.read()


        # Will keep running until the virtual memory has content
        while len(virtualMemory) > 0:

            page = virtualMemory.pop(0)

            # Page fault!
            if page not in physicalMemory:
        
                pgFault += 1

                # If physical memory is full, run the FIFO algorithm
                if len(physicalMemory) >= self.physicalMemorySize:
                    physicalMemory.pop(0)
                    physicalMemory.append(page)
                
                # If it isn't simply append
                else:
                    physicalMemory.append(page)



        # Outputs the final physical memory and amount of page faults occured
        print(f"\Physical Memoryn{physicalMemory}\n")
        print(f"\nTotal Page Faults: {pgFault}\n")
        # print(f"\nSize of List: {len(physicalMemory)}")




def main():
    
    if len(sys.argv)-1 == 2:
        pageCount = int( sys.argv[1] )
        fileName  = sys.argv[2]

    else:
        print("Incorrect Arguments!...\n<page count> <file name>\n...")
        sys.exit()


    virtPage = FIFO(pageCount, fileName)
    virtPage.run()


main()