import subprocess
from subprocess import call

num_of_agents = 10
num_of_iterations = 10
neighbourhood = 10
random_seed = 0

num_of_agent_increments = 2
agent_increment = 5

for i in range(num_of_agent_increments):
    print(i)
    cmd = 'python model7.py ' + str(num_of_agents) + ' ' + str(num_of_iterations) + ' ' + str(neighbourhood) + ' ' + str(random_seed)
    print(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    # wait for the process to terminate
    out, err = p.communicate()
    print(str(out.splitlines()))
    print(err)
    errcode = p.returncode
    print(errcode)
    num_of_agents += agent_increment