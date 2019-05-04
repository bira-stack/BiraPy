from subprocess import Popen, PIPE

# p1 = Popen(["python", "testprocesss.py"], stdout=PIPE)

# print p1.communicate()

process = Popen(
        ["python", "testprocesss.py"],
        cwd=None,
        shell=False,
        close_fds=True,
        stdout=PIPE,
        stderr=PIPE,
        bufsize=1
    )

print process.stdout.readline()
print process.stderr.readline().encode('UTF-8')