from system_hotkey import SystemHotkey
hk = SystemHotkey()
hk.register(('control', 'shift', 'h'), callback=lambda:exit(0))
i=0
while 1:
    i+=1
    print(i)

