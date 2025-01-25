import subprocess


def bash(cmd_string, suppress_exception=False):
    process = subprocess.Popen(
        cmd_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL
    )
    
    output = ""
    for line in process.stdout:
        line = line.decode('utf-8')
        print(line, end='')
        output += line

    for line in process.stderr:
        line = line.decode('utf-8')
        print(line, end='')
        output += line

    process.stdout.close()
    process.stderr.close()
    process.wait()

    if process.returncode != 0 and not suppress_exception:
        raise subprocess.CalledProcessError(process.returncode, cmd_string, output=output)

    return output