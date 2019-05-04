from subprocess import Popen, PIPE

def execute():
    process = Popen(
            ["python", "testprocesss.py"],
            cwd=None,
            shell=False,
            close_fds=True,
            stdout=PIPE,
            stderr=PIPE,
            bufsize=1
        )
    
    errors = []
    # read error lines from the PIPE
    for line in process.stderr.readline():
        errors.append(line)
    
    out = ' '.join(errors)

    print out

    # print process.stdout.readline()
    # print process.stderr.readline().encode('UTF-8')

execute()