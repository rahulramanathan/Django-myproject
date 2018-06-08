import netmiko
def fn(command):
    try:
        net_connect = netmiko.ConnectHandler(
            device_type='cisco_ios',
            ip='192.168.1.10',
            username='cisco',
            password='cisco',
            # port=22,
            # global_delay_factor=2
        )
        net_connect.enable()
        # print('Connection successful')
        # print(net_connect)
        result = net_connect.send_command(command)
        #print(result)
        net_connect.disconnect()
        return result
    except netmiko.NetMikoTimeoutException as e:  # router getting timed out
        print(e)
    except netmiko.NetMikoAuthenticationException as e:
        print('AuthException')