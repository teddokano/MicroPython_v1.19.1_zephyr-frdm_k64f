# MicroPython_v1.19.1 for FRDM-K64F
This is a firmware to operate MicroPython on FRDM-K64F. 

## What is this?
A firmware binary and some sample code for MicroPython_v1.19.1 for FRDM-K64F. 

> **note**
> MicroPython is provided in [the MIT license by dpgeorge](https://github.com/micropython/micropython/blob/master/LICENSE).  
> The firmware binary should be handled with its license in [micropython repository](https://github.com/micropython/micropython)
 
To use the MicroPython on FRDM-K64F boards, need to build the MicroPython code after installing Zephyr development envirinment.  
This repo is including the binary which was with default setting. User can try it immediately just after copy the binary by drag-and-drop. 

![FRDM-K64F](https://github.com/teddokano/additional_files/blob/main/MicroPython_v1.19.1_zephyr-frdm_k64f/board.jpg)  
_FRDM-K64F board, USB cable connected on **J26** connector_

# Getting started

1. Find a file `firmware/MicroPython_v1.19.1_zephyr-frdm_k64f.bin` and download onto your PC.  
2. When the FRDM-K64F **J26** is connected to PC, a storage icon: **DAPLINK** will appear on your desktop. 
3. Just drag the file into DAPLINK storage. 
4. The storage will be mounted on the desktop again after copy completed. 
5. In Thonny (a simple IDE application) or a termial application, connect to the serial port which is used for the FRDM-K64F. 
6. If using a terminal software, choose baudrate 115200. Press keys [Control]-'b', will show welcome message and prompt. 

![Terminal screen](https://github.com/teddokano/additional_files/blob/main/MicroPython_v1.19.1_zephyr-frdm_k64f/MicroPython_v1.19.1%20for%20FRDM-K64F_on_CoolTerm.png)  
_MicroPython prompt on CoolTerm (a terminal application)_

## If you want to try it with `screen` command
This is **just an option** if you want to access to the board without installing any other applications.  
When you use a screen command in the shell, type following command.  
```
$ screen <serial_port> 115200 
```

The `<serial_port>` should be replaced by serial port device. In my environment, the devices are appeared like
```
$ ls -al /dev/cu*
crw-rw-rw-  1 root  wheel  0x9000001 Apr 26 06:51 /dev/cu.Bluetooth-Incoming-Port
crw-rw-rw-  1 root  wheel  0x9000003 Apr 27 06:13 /dev/cu.usbmodem211102
```
So choose `/dev/cu.usbmodem211102` from the list and the command will be..  
`$ screen /dev/cu.usbmodem211102 115200`

After screen is up, press keys [Control]+'b' to display the welcome message.  

For quitting from the screen, press keys [Control]-'a' then 'k'.  

# Reference
Steps of building MictoPython Zephyr port is explained [here (Japanese version only)](https://qiita.com/teddokano/items/75a508bd32d9784efcce).  
Follow those steps if you need your own binary with customized configuration. 
