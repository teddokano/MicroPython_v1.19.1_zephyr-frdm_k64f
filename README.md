# MicroPython_v1.19.1 for FRDM-K64F
This is a firmware to operate MicroPython on FRDM-K64F. 

## What is this?
A firmware binary and some sample code for MicroPython_v1.19.1 for FRDM-K64F.  
To use the MicroPython on FRDM-K64F boards, need to build the MicroPython code after installing Zephyr development envirinment.  
This repo is including the binary which was with default setting. User can try it immediately just after copy the binary by drag-and-drop. 

# Getting started
1. Find a file `firmware/MicroPython_v1.19.1_zephyr-frdm_k64f.bin` and download onto your PC.  
2. When the FRDM-K64F J26 is connected to PC, a storage icon: **DAPLINK** will appear on your desktop. 
3. Just drag the file into DAPLINK storage. 
4. The storage will be mounted on the desktop again after copy completed. 
5. In termial application or Thonny (a simple IDE for Python), connect to the serial port which is used for the FRDM-K64F. 
6. If using a terminal software, choose baudrate 115200. Key-input of Control-b, will show welcome message and prompt. 

![Terminal screen](https://github.com/teddokano/additional_files/blob/main/MicroPython_v1.19.1_zephyr-frdm_k64f/MicroPython_v1.19.1%20for%20FRDM-K64F_on_CoolTerm.png)  
_MicroPython prompt on CoolTerm (a terminal application)_
