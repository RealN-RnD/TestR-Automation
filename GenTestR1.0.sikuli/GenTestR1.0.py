version = "AutomateG1.0"

while True:
    click("1470125507873.png")
    popup("Press OK when you have finished testing", version)
    click("1470125519799.png")
    click("1470046377455.png")
    isWindows = popAsk("Are you testing on Windows?", version)
    if not isWindows:
        paste("Mac OS X 10.10.5" + Key.ENTER + "MacBook Pro (Retina 13-inch Late 2013)" + Key.ENTER + "Model A1502")
    click("1470046406673.png")
    click("1470046165953.png")
    paste("1.14.0.26")
    click("1470046187921.png")
    if not isWindows:
        type("Mac OS X 10.10")
    else:
        type("Windows 7 64")
    answer = popAsk("Did the test pass?", version)
    if not answer:
        defect = input("Please enter defect code", version)
        if defect != "":
            click("1470210216668.png")
            paste(defect)
        popup("Select test steps that failed and change Status", version)
    wait(2)
    click("1470126482063.png")
    wait(2)
    click("1470126608431.png")
    doWeContinue = popAsk("Another test?", version)
    if not doWeContinue:
        popup("You're Winner", version)
        exit(1)


