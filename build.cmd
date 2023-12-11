nasm -f win64 main.asm -o main.obj
lnk /console /entry:main msvcrt.dll kernel32.dll main.obj