#Hello world Python example
#@author Alexei Bulazel, mod: Mateusz Wojcik
#@category INFILTRATE
#@keybinding 
#@menupath 
#@toolbar 


print "Hello world!"

danger = ["doSystemCmd"]
prgm = ghidra.program.flatapi.FlatProgramAPI(currentProgram)
listing = currentProgram.getListing()
fn = prgm.getFirstFunction()
while fn is not None:
 	if str(fn.getName()) in danger:
 		print("Dangerous function found: {}".format(fn.getName()))
 		print("Entry point: {}".format(fn.getEntryPoint()))
 		dummy = ghidra.util.task.TaskMonitor.DUMMY
 		called_by = fn.getCallingFunctions(dummy)
 		for caller in called_by:
 			print("{} is called by: {} at {}\n".format(fn.getName(), caller.getName(), caller.getEntryPoint()))
 	fn = prgm.getFunctionAfter(fn)
