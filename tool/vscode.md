# VSCode

## Download

original download link:

https://az764295.vo.msecnd.net/stable/129500ee4c8ab7263461ffe327268ba56b9f210d/VSCodeUserSetup-x64-1.72.1.exe

replace `az764295.vo.msecnd.net` to `vscode.cdn.azure.cn`,

which is:

https://vscode.cdn.azure.cn/stable/129500ee4c8ab7263461ffe327268ba56b9f210d/VSCodeUserSetup-x64-1.72.1.exe

## EditorConfig

[official website](https://editorconfig.org/)

### example

```ini
# EditorConfig is awesome: https://EditorConfig.org

# top-most EditorConfig file
root = true

# Unix-style newlines with a newline ending every file
[*]
end_of_line = lf
insert_final_newline = true

# Matches multiple files with brace expansion notation
# Set default charset
[*.{js,py}]
charset = utf-8

# 4 space indentation
[*.py]
indent_style = space
indent_size = 4

# Tab indentation (no size specified)
[Makefile]
indent_style = tab

# Indentation override for all JS under lib directory
[lib/**.js]
indent_style = space
indent_size = 2

# Matches the exact files either package.json or .travis.yml
[{package.json,.travis.yml}]
indent_style = space
indent_size = 2
```
