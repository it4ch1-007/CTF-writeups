import angr
import claripy

# flag=claripy.BVS("flag",100*8)

proj=angr.Project('./x0rr3al',main_opts={'base_addr':0},auto_load_libs=False)

initial_state = proj.factory.entry_state()


sm=proj.factory.simulation_manager(initial_state)
avoid_address=[0X156A,0x16AD]
sm.explore(find=0x01b62,avoid=avoid_address)

found=sm.found[0]

print(found.posix.dumps(0))