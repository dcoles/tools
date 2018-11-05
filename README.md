# Tools

A collection of useful tools and short scripts that might make your day a little better.

## choot

Simple namespace-based chroot in Bash.

### Usage

```
$ choot [-R] /path/to/sysroot [cmd [args...]]
```

If the `-R` option is given then the sysroot will be mounted read-only.

If `cmd` is not given then runs `$SHELL -i` (default: `/bin/sh -i`), otherwise runs the provided command inside the sysroot.

## ghcat

Cat a file on GitHub.

### Usage

Cat a file:

```
$ ghcat owner/repo/path/in/repo.ext
```

Cat a private file:

```
$ ghcat -u username:password owner/repo/path/in/repo.ext
```

## gist

Create a GitHub gist from the command-line.

### Usage

Create a gist of one or more files:
```
$ gist -u username file [file...]
```

Provide password or [Personal Access Token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/)
on the command-line:
```
$ gist -u username:token file [file...]
```

Create a public gist:
```
$ gist -u username -P file [file...]
```

Provide a gist description:
```
$ gist -u username -d 'My files' file [file...]
```

Create a gist from STDIN:
```
$ gist -u username -
```
