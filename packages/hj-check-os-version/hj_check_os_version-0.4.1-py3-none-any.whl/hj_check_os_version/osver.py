def get_os_pretty_name() -> str:
    with open('/etc/os-release', 'r') as file:
        for line in file:
            if line.startswith('PRETTY_NAME'):
                # Ubuntu 24.04.1 LTS
                r = line.split('=')[1].replace('\n','').strip("\"")
                print(r)
                return r
    return None
