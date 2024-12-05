from fi_fsa import fi_fsa_v2
import time

# server_ip_list = ["192.168.137.101"]


def main():
    server_ip_list = fi_fsa_v2.broadcast_func_with_filter(filter_type="Actuator")

    if server_ip_list:

        for i in range(len(server_ip_list)):
            print("now is setting: " + server_ip_list[i])
            ret = fi_fsa_v2.set_fsa_abs_zero(server_ip_list[i])
            print(ret)
            time.sleep(1)

        time.sleep(3)

        for i in range(len(server_ip_list)):
            fi_fsa_v2.reboot(server_ip_list[i])


if __name__ == "__main__":
    main()