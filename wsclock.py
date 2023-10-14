# Working-Set Clock Algorithm

# This algorithm uses a circular frame, containing a data structure for the pages.
# For choosing an appropiate page to remove, it scans the array
# for a page who's age is greater than tau, a specified time parameter
# if the page is an unreferenced page.

# How to run:       python3 wsclock.py <num of phys page> <tau> access sequence file
#                   python3 wsclock.py 10  5 page.txt




import sys

# A Struct-Like data to simulate our page(s)
# Contains:
# element
# time-of-last-access
# reference-bit
class Page:

    element = 0
    tola = 0
    ref_bit = 1

    def printData(self):
        print(f"{self.element} : {self.tola} : {self.ref_bit}")


class WSCLOCK():

    def __init__(self, physicalMemorySize, tau, fileName):
        
        self.physicalMemorySize = physicalMemorySize
        self.fileName = fileName
        self.tau = tau


    ClockHand   = 0
    VirtualTime = 0


    @staticmethod
    def findPage(physicalMemory, page):

        for pg in physicalMemory:

            if page == pg.element:
                return True, physicalMemory.index(pg)
        
        return False, 0


    def removePage(self, physicalMemory):

        # Must loop indefinetely until an appropiate TOLA is found
        while True:
            
            # Dereference the Bit
            if physicalMemory[self.ClockHand].ref_bit == 1:
                physicalMemory[self.ClockHand].ref_bit = 0
            
            elif (self.VirtualTime - physicalMemory[self.ClockHand].tola) > self.tau:
                return self.ClockHand

            # Move the hand // Circular List
            self.ClockHand = (self.ClockHand + 1) % self.physicalMemorySize
            # print(f"removePage ClockHand: {self.ClockHand}")


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

    def run(self):

        # Page Fault counter
        pgFault = 0

        # List / Queue
        physicalMemory = [] * self.physicalMemorySize
        virtualMemory = self.read()

        # Keep looping until we've read all the content from the Virtual Memory
        while len(virtualMemory) > 0:

            # Element from the Virtual Memory / page.txt
            elem = virtualMemory.pop(0)

            # Make a page with the class & asign element
            page = Page()
            page.element = elem

            # If element is in physicalMemory, update the Time of Last Access
            existsInPhysMem , indexOfPage = self.findPage(physicalMemory, page.element)

            # Page Hit
            # Update: Clock , Virtual Time , Reference Bit
            if existsInPhysMem:
                physicalMemory[indexOfPage].tola = self.VirtualTime
                physicalMemory[indexOfPage].ref_bit = 1


            # Page Fault!
            else:
            
                pgFault += 1

                # If our memory capacity is reached,
                # run our page replacement algorithm
                if len(physicalMemory) >= self.physicalMemorySize:
                    page.tola = self.VirtualTime
                    pgToRem = self.removePage(physicalMemory)
                    physicalMemory[pgToRem] = page


                # If there's still memory,
                # simply append
                else:
                    page.tola = self.VirtualTime
                    physicalMemory.append(page)


                # Points to the next page in a circular manner
                self.ClockHand = (self.ClockHand + 1) % self.physicalMemorySize


            # This adds one integer to our virtual time 🤓
            self.VirtualTime += 1



        print("Physical Memory\n")
        for page in physicalMemory:
            page.printData()
      
        print(f"\nTotal Page Faults: {pgFault}\n")


def main():
    
    if len(sys.argv)-1 == 3:
        pageCount = int( sys.argv[1] )
        tau = int(sys.argv[2])
        fileName  = sys.argv[3]

    else:
        print("Incorrect Arguments!...\n<page count> <file name>\n...")
        sys.exit()


    virtPage = WSCLOCK(pageCount, tau, fileName)
    virtPage.run()



main()