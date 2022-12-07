Role Name
=========

This role configures default RPi Kali installation as a device inplant.
It uses OpenVPN to automatically connect to a VPN server on boot.
Additionally, it is configured with a 4G that can send updates and receive commands.

Requirements
------------

The RPi needs to be configured with a default Kali image.
Put the Operator pubkeys and the .ovpn connection file under `files/`.


Role Variables
--------------

| Variable          | Default value | Required | Description                                                  |
| ---               | ---           | ---      | ---                                                          |
| rt_hostname       | rpi-vpn-0     | False    | The RPi's hostname                                           |
| rt_user           | kali          | False    | The default user as which everything will run                |
| rt_user_pw        | temp          | False    | The default user's password                                  |
| rt_ovpn_file_name | `null`        | True     | The filename of the .ovpn file. Put this file under `files/` |
| rt_operator_keys  | []            | True     | List of operator names. Put their SSH pubkey under `files/`  |
| rt_numbers        | []            | True     | List of numbers where the 4G dongle sends updates to.        |


Dependencies
------------

None

Example Playbook
----------------

```Yaml
    - hosts: localhost
      roles:
         - fpkmatthi.redteam_device
      vars:
        rt_hostname: 'rpi-vpn-69'
        rt_user: 'rtoperator'
        rt_user_pw: 'K4l1H4ck3r'
        rt_ovpn_file_name: 'connection.ovpn'
        rt_operator_keys:
          - matthias
          - arne
        rt_numbers:
          - "+32472909199"
```

You can add the following snippet to your ~/.ssh/config to make connecting to the implant easier.

```
Host rpi-vpn-69
    Port 22
    Hostname 192.2.0.6
    ProxyJump <project>-vpn-0 #VPN server
    User kali #rt_user
```


License
-------

MIT

