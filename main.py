# This is a sample Python script.

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Refs: https://github.com/pythonnet/pythonnet/wiki/How-to-call-a-dynamic-library
# https://stackoverflow.com/questions/49942487/python-for-net-how-to-explicitly-create-instances-of-c-sharp-classes-using-dif


if __name__ == '__main__':
    import clr
    import sys
    from clr import System #don't use dots after import; use from-import

    from enum import Enum

    path = "C:\\DLL\\"

    sys.path.append(path)
    ans0 = clr.AddReference('ClientApp1')
    ans = clr.System.Reflection.Assembly.LoadFile(path + "ClientApp1.dll")
    print( "\n", ans0.FullName, "\n", ans0.Location, "\n", ans.FullName, "\n", ans.Location, "\n")
    import ClientApp1 as AssemblyLib

    port = 0;    address = "";    id = ""

    #ca_obj = ClientApp1Lib.ClientApp1Lib.ClientApp1() # alas, it calls "new" which triggers file search popup window
    ca_obj = AssemblyLib.ClientApp1Lib.ClientApp1
    # get type
    ca_Type = clr.GetClrType(AssemblyLib.ClientApp1Lib.ClientApp1)
    print(ca_Type.FullName, "\t", ca_Type)
    # GetUninitializedObject to avoid constructor and 'new' issue
    ca_obj = System.Runtime.Serialization.FormatterServices.GetUninitializedObject(ca_Type)
    print(ca_obj.IsValid(), "\t", ca_obj) # False
    ca_obj = AssemblyLib.ClientApp1Lib.ClientApp1.Create(ca_obj, ca_obj)
    print(ca_obj.IsValid(), "\t", ca_obj) # True

    ca_obj, ca_obj, port, address, id = AssemblyLib.ClientApp1Lib.ClientApp1.GetConfig(ca_obj, ca_obj, port, address, id)
    print(id, "\t", address, ":", port, "\t", ca_obj)

    ca_obj = AssemblyLib.ClientApp1Lib.ClientApp1.SetConfig(1234, "localhost", ca_obj, "id_ca", ca_obj)

    ca_obj, ca_obj, port, address, id = AssemblyLib.ClientApp1Lib.ClientApp1.GetConfig(ca_obj, ca_obj, port, address, id)
    print(id, "\t", address, ":", port, "\t", ca_obj)
    AssemblyLib.ClientApp1Lib.ClientApp1.Destroy(ca_obj)

# See
