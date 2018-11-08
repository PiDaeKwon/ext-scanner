import os
import signature_data
import binascii

def scan(directory):
    file_count = 0
    wrongfile_count = 0
    wrongfile_list = []
    notsupport_count = 0
    notsupport_ext = []
    for (path, dir, files) in os.walk(directory):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext != '':
                result = signature_data.compare(ext)
                file_count += 1
                try:
                    with open(os.path.join(path, filename), 'rb') as tmpfile:
                        signature = binascii.hexlify(tmpfile.read(result[0])).upper().decode('ascii')
                        if signature != result[1]:
                            wrongfile_count += 1
                            wrongfile_list.append(os.path.dirname(os.path.abspath(__file__)) + "/" + filename)
                            #print("Wrong file : " + os.path.dirname(os.path.abspath(__file__)) + "/" + filename)
                            """
                        else:
                            print("Correct File : " + filename)
                            """
                except TypeError:
                    notsupport_ext.append(ext)
                    notsupport_count += 1


    return file_count, wrongfile_count, wrongfile_list, notsupport_count, list(set(notsupport_ext))
