CHALLENGES = {
    'ascii_easy': {
        'name': 'ascii_easy',
        'track': 'Rookiss',
        'points': 33,
        'tags': ['Buffer Overflow', 'ASCII Constraints'],
        'description': 'Buffer overflow exploit with ASCII-only constraints. Exploits unsafe strcpy to achieve code execution using only printable ASCII characters.',
        'ssh_host': 'pwnable.kr',
        'ssh_port': 2222,
        'ssh_user': 'ascii_easy',
        'ssh_pass': 'guest'
    },
    'uaf': {
        'name': 'uaf',
        'track': 'Rookiss',
        'points': 30,
        'tags': ['Use-After-Free', 'Heap', 'Vtable Hijacking'],
        'description': 'Use-after-free vulnerability in C++ objects. Hijack vtable pointer to redirect virtual function calls.',
        'ssh_host': 'pwnable.kr',
        'ssh_port': 2222,
        'ssh_user': 'uaf',
        'ssh_pass': 'guest'
    },
    'tiny_easy': {
        'name': 'tiny_easy',
        'track': 'Rookiss',
        'points': 30,
        'tags': ['ASLR Bypass', 'NOP Sled', 'Shellcode'],
        'description': 'Exploit 32-bit ASLR weakness using a NOP sled and direct shellcode execution. Control argv[0] to redirect execution to stack.',
        'ssh_host': 'pwnable.kr',
        'ssh_port': 2222,
        'ssh_user': 'tiny_easy',
        'ssh_pass': 'guest'
    },
    'asm': {
        'name': 'asm',
        'track': 'Rookiss',
        'points': 9,
        'tags': ['Shellcoding', 'Seccomp', 'x86-64'],
        'description': 'Write x86-64 shellcode under seccomp sandbox. Use only open/read/write syscalls to read the flag file.',
        'ssh_host': 'pwnable.kr',
        'ssh_port': 2222,
        'ssh_user': 'asm',
        'ssh_pass': 'guest'
    },
    'unlink': {
        'name': 'unlink',
        'track': 'Rookiss',
        'points': 25,
        'tags': ['Heap Exploitation', 'Unlink Corruption', 'Stack Pivot'],
        'description': 'Exploit heap unlink corruption to achieve arbitrary write and redirect control flow. Use stack pivot technique to execute shell function.',
        'ssh_host': 'pwnable.kr',
        'ssh_port': 2222,
        'ssh_user': 'unlink',
        'ssh_pass': 'guest'
    },
}