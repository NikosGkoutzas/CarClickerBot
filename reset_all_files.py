# Nick Gkoutzas - Feb 2022 ---------------
# --------------- Last update: Sep 28 2024
# ----------------------------------------


def writeNumOfErrors(file_name , number):
    write_err = open(file_name , 'w')
    write_err.write( str(number) )
    write_err.flush()
    write_err.close()

def write_delay(file_name , writeDelay):    # in the beginning 'writeDelay' must be '5'... -. 'delay.txt'
    delay = open(file_name , 'w')
    delay.write( str(writeDelay) )
    delay.flush()
    delay.close()

def read_NumberOfMachines(file_name):
    numOfMach = open(file_name , 'r')
    numberOfMachines__ = numOfMach.read()
    numOfMach.close()
    return int(numberOfMachines__)


'''file = open("updateNumber.txt", "w")    # open the file
file.write(str(0))   # write the number in the file
file.flush() 
file.close()'''

fileTotal = open("totalUpdates.txt", "w")    # open the file
fileTotal.write(str(0))   # write the number in the file
fileTotal.flush()
fileTotal.close()

fileEach = open("MachinesEachUpdate.txt" , "w")
for i in range(0 , read_NumberOfMachines("NumberOfMachines.txt")):
    fileEach.write(str(0) + "\n")
fileEach.close()

#changeDelayOnceWrite("change_delay_once.txt" , 1)
writeNumOfErrors("reached_20_errors.txt" , 0)
write_delay("delay.txt" , 5)

errors__ = open("totalErrors.txt" , 'w')
errors__.write( str(0) )
errors__.flush()
errors__.close()

GitHub_updates_number = open("GitHubUpdatesNumber.txt" , 'w')
GitHub_updates_number.write( str(0) )
GitHub_updates_number.flush()
GitHub_updates_number.close()

internet_err_DATE_file = open("internet_error_DATE.txt" , 'w')
internet_err_DATE_file.write( str(0) )
internet_err_DATE_file.flush()
internet_err_DATE_file.close()

feedback_number = open("read_feedbackNumber.txt" , 'w')
feedback_number.write( str(0) )
feedback_number.flush()
feedback_number.close()

reset_number = open("read_resetNumber.txt" , 'w')
reset_number.write( str(0) )
reset_number.flush()
reset_number.close()

file_removed_machines = open("removed_machines.txt" , 'w')
file_removed_machines.write( str(0) )
file_removed_machines.flush()
file_removed_machines.close()

file_imported_machines = open("imported_machines.txt" , 'w')
file_imported_machines.write( str(0) )
file_imported_machines.flush()
file_imported_machines.close()
