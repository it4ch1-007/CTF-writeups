import gdb

def is_program_ended():
    try:
        # Run the "info inferiors" command to get information about all inferiors (processes)
        info_output = gdb.execute("info inferiors", to_string=True)
        
        # Check if the output contains "No registers."
        # This typically indicates that the program has ended
        return "No registers." in info_output
    except gdb.error:
        # Handle any exceptions that may occur
        return False
gdb.execute("b *xoring+154")
gdb.execute("b *xoring+171")
gdb.execute("b *xoring+207")
i=100
s="csawctf{"
gdb.execute("r")
while(i>=0):
    gdb.execute("c")
    if(is_program_ended()):
        s+="}"
        break
    pc = gdb.selected_frame().pc()
    disassembly = gdb.execute(f'disassemble {pc}', to_string=True)
    # instruction_name = disassembly.strip().split(':')[i]
    # print(instruction_name)
    value = gdb.execute("x/x $rip",to_string=True).split(':')[0].split(' ')[1]
    if(value=='<xoring+171>'):
        s+='0'
    elif(value == '<xoring+207>'):
        s+='1'
    print(value)
    print(s)
    i-=1

    
   

    