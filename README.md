# Tools

## gist

Create a GitHub gist from the command-line.

## Usage

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

