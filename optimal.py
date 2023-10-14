# Optimal Page Replacement

# With this technique, 
# pages that would be inactive 
# for the longest amount of time are replaced.

# How to run:       python3 optimal.py <num of phys page> access sequence file
#                   python3 optimal.py 10 input.txt


import sys



# Class for our Page Replacement Algorithm
class Optimal():

    def __init__(self, physicalMemorySize, fileName):
        
        self.physicalMemorySize = physicalMemorySize
        self.fileName = fileName



    #Function to find the optimal page to replace
    @staticmethod
    def removePage(physicalMemory, virtualMemory):
  
        maxIndex = 0

        # Searches the physical memory 
        # until an appropiate page is found
        # Determined by finding either a page who's
        # no longer present in the virtual memory
        # or a page who's accessed farthest in the virtual memory
        for i in range(len(physicalMemory)):

            # Commenting Python code sometimes is redundant
            if physicalMemory[i] not in virtualMemory:
                return i

            else:
                # Get the current index of where the physical memory's element
                # lies in the virtual memory
                index = virtualMemory.index( physicalMemory[i] )

                # if its greater than our maximum index, then update it
                if index > maxIndex:
                    maxIndex = i


        # This shall be our max index that will be replaced
        return maxIndex
            
 

    # Copies the content from the input file
    # and return it as an array, useful for Optimal PRA
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


    # Executes the Page Replacement Algorithm
    def run(self):

        # Page Fault counter
        pgFault = 0
        # physical memory & virtual memory contents
        physicalMemory = [] * self.physicalMemorySize

        # Reads the input file
        virtualMemory  = self.read()

        # Keep looping until we've read all the content from the Virtual Memory
        while len(virtualMemory) > 0:

            page = virtualMemory.pop(0)

            # If page not in physical memory
            if page not in physicalMemory:

                pgFault += 1

                # If we've reached max size for the physical memory
                if len(physicalMemory) >= self.physicalMemorySize:

                    # Finds the page to remove
                    pgToRem = self.removePage(physicalMemory, virtualMemory)
                    physicalMemory[pgToRem] = page
                
                # Or simply appends if there's still memory available
                else:
                    physicalMemory.append(page)


        print(f"Physical Memory\n{physicalMemory}\n")
        print(f"\nTotal Page Faults: {pgFault}\n")
        


def main():
    
    if len(sys.argv)-1 == 2:
        pageCount = int( sys.argv[1] )
        fileName  = sys.argv[2]

    else:
        print("Incorrect Arguments!...\n<page count> <file name>\n...")
        sys.exit()


    virtPage = Optimal(pageCount, fileName)
    virtPage.run()



main()
