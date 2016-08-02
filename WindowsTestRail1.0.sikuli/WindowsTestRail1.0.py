while True:
    click("1470125507873.png")
    popup("Press OK when you have finished testing")
    click("1470125519799.png")
    click("1470046377455.png")
    paste("")
    click("1470046406673.png")
    click("1470046165953.png")
    paste("1.14.0.26")
    click("1470046187921.png")
    type("Windows 7 64")
    answer = popAsk("Did the test pass?")
    if not answer:
        exit(1)
    wait(4)
    click("1470126482063.png")
    wait(2)
    click("1470126608431.png")
    doWeContinue = popAsk("Another test?")
    if not doWeContinue:
        exit(1)


