from twilio.rest import Client
import read_email
import time

if __name__ == "__main__":
    print("started Process")
    client = Client("AC160a215e645c53aad10dc76385cc9ddb", "f07f3fca71266e4177be37116ee34fc8")

    while True:
        try:
            open("last_msg.txt", "x")
        except:
            pass
        file = open("last_msg.txt", "r")
        last_msg = file.read()
        file.close()

        returnArray = read_email.read_email_from_gmail()

        if returnArray != 0:
            msg = "GTS-SERVER: \n"

            for item in returnArray[1]:
                if item != "[" or item != "]" or item != "0" or item != '\'':
                    msg += str(item)

            msg += "\n"

            found_s = 0
            found_p = 0
            found_a = 0
            found_n = 0
            msg_temp = ""

            item_temp = str(returnArray[2])
            item_temp = str(item_temp[6000:])

            for item in item_temp:
                item = str(item)
                if item == "s" and found_s == 0:
                    found_s = 1
                elif item == "p" and found_p == 0:
                    found_p = 1
                elif item == "a" and found_a == 0:
                    found_a = 1
                elif item == "n" and found_n == 0:
                    found_n = 1
                elif found_p == 1 and found_s == 1 and found_a == 1 and found_n == 1:
                    pass
                else:
                    found_s = 0
                    found_p = 0
                    found_a = 0
                    found_n = 0

                if found_s == 1 and found_p == 1 and found_a == 1 and found_n == 1 and item != "<":
                    msg_temp += item
                elif item == "<" and found_s == 1 and found_p == 1 and found_a == 1 and found_n == 1:
                    break
                else:
                    pass

            for i in range(15):
                msg_temp = msg_temp[1:]

            msg += "\n" + msg_temp

            if last_msg != msg:
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                print(current_time, end=" ")
                print(msg)
                client.messages.create(to="+393494492591", from_="+12566078786", body="GTS-SERVER: \n" + msg)
                print("send Message to user")
                last_msg = msg
                file = open("last_msg.txt", "w")
                file.write(last_msg)
                file.close()
                time.sleep(3600)
            else:
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                print(current_time, end=" ")
                print("Email already send")
                time.sleep(1800)
        else:
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print(current_time, end=" ")
            print("no return from Email")
            time.sleep(3600)
