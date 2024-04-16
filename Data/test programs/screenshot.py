if pgb.button_left():
    with open("out.bin","ab") as out:
        for line in range(240):
            data=bytes(pgb.sbuffer[line*480:line*480+480])
            out.write(data)
