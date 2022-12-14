#imported libraries
import os
import re
import datetime
import hashlib
import itertools
import sys
import time
#Name Banner
def name_banner():
    print('*'*50)
    print('\n╦ ╦┌─┐┌─┐┬ ┬  ╔═╗┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐\n╠═╣├─┤└─┐├─┤  ║  ├┬┘├─┤│  ├┴┐├┤ ├┬┘\n╩ ╩┴ ┴└─┘┴ ┴  ╚═╝┴└─┴ ┴└─┘┴ ┴└─┘┴└─\n')
    print('*'*50)
    return 0
#Selection Screen
def selection_screen():
    print('(This will only be asked for the first time you start the program)\n')
    print('Please Select the mode you want to run the program:\n')

    print('1.Argument mode')
    print('2.Interactive mode')
    mode_input=input('\nchoose your mode (options:1,2): ')
    if mode_input=='1' or mode_input=='2':
        if mode_input=='1':
            write_config('Opration_Mode','arg')
            sys.exit()
        elif mode_input=='2':
            write_config('Opration_Mode','int')
    else:
        print('\nChoose a Correct Option! \n')
        selection_screen()
def int_selection():
    print('\nSelect the core attack mode you want to use:\n')
    print('1.Dictionary Attack')
    print('2.Combination Attack')
    print('3.Brute Force Attack')
    print('4.Reverse Attack')
    sl_input=input("Please Enter your option: ")
    if sl_input=='1':
        dir_atc()
    elif sl_input=='2':
        comb_atc()
    elif sl_input=='3':
        brt_atc()
    elif sl_input=='4':
        hyb_atc()

#Reading Configurations
def read_config():
    script_path=os.path.dirname(__file__)
    rel_path='datafile/Settings.txt'
    config_path=os.path.join(script_path,rel_path)
    fileobj=open(config_path,'r')
    config={}
    for line in fileobj:
        temp_list=line.split('=')
        if len(temp_list)==2:
            temp_dict={temp_list[0]:temp_list[1]}
            config.update(temp_dict)
    fileobj.close()
    return config

#Writing to Configuration File
def write_config(var,val):
    script_path=os.path.dirname(__file__)
    rel_path='datafile/Settings.txt'
    config_path=os.path.join(script_path,rel_path)
    fileobj=open(config_path,'r+')
    if var=='Opration_Mode':
        OM_options=['int','arg']
        if val not in OM_options:
            print('Invalid Option')
            exit
        if check_val(str(val)) == True:
            print('Option is already set to',val)
        else:
            if val == OM_options[0]:
                z=OM_options[1]
            elif val == OM_options[1]:
                z=OM_options[0]
            with fileobj as f:
                text = f.read()
                text = re.sub(z,val,text)
                f.seek(0)
                f.write(text)
                f.truncate()
                print('Option Changed to',val)
    fileobj.close()

#checks if the option of the settings is 
def check_val(val): 
    script_path=os.path.dirname(__file__)
    rel_path='datafile/Settings.txt'
    config_path=os.path.join(script_path,rel_path)
    fileobj=open(config_path,'r+')
    for line in fileobj:
            li=line.strip()
            if not li.startswith('#') and val in li:
                return True
    fileobj.close()

#directory attack
def dir_atc():
    print('Which encryption do you want to crack:\n')
    print('1.MD5')
    print('2.blake2b')
    print('3.blake2s')
    print('4.SHA-1')
    print('5.SHA-224')
    print('6.SHA-256')
    print('7.SHA-384')
    print('8.SHA-512')
    print('9.SHA3-384')
    print('10.SHA3-512')
    print('11.SHAKE-128')
    print('12.SHAKE-256')
    print('13.EXIT')

    option=input('Select your option: ')
    if int(option) not in range(1,12):
        print('\nInvalid Option!\n')
        dct_atc()

    hash=input('\nEnter the hash: ')
    wrd_list=input('Enter the location of the wordlist: ')
    while not os.path.exists(wrd_list):
        print('The file does not exist')
        wrd_list=input('Enter the location of the wordlist: ')
    if option=='1':
        md5(hash,wrd_list)
    elif option=='2':
        blk2b(hash,wrd_list)
    elif option=='3':
        blk2s(hash,wrd_list)
    elif option=='4':
        sha1(hash,wrd_list)
    elif option=='5':
        sha224(hash,wrd_list)
    elif option=='6':
        sha256(hash,wrd_list)
    elif option=='7':
        sha384(hash,wrd_list)
    elif option=='8':
        sha512(hash,wrd_list)
    elif option=='9':
        sha3384(hash,wrd_list)
    elif option=='10':
        sha3512(hash,wrd_list)
    elif option=='11':
        shk128(hash,wrd_list)
    elif option=='12':
        shk256(hash,wrd_list)
    elif option=='13':
        sys.exit(0)
    else:
        print('\nCoudn\'t crack the password :( ')

#Combination Attack
def comb_atc():
    print('Which encryption do you want to crack:\n')
    print('1.MD5')
    print('2.blake2b')
    print('3.blake2s')
    print('4.SHA-1')
    print('5.SHA-224')
    print('6.SHA-256')
    print('7.SHA-384')
    print('8.SHA-512')
    print('9.SHA3-384')
    print('10.SHA3-512')
    print('11.SHAKE-128')
    print('12.SHAKE-256')

    option=input('Select your option: ')
    if int(option) not in (1,12):
        print('\nInvalid Option!\n')
        comb_atc()

    hash=input('\nEnter the hash: ')
    wrd_list=input('Enter the location of the wordlist: ')
    while not os.path.exists(wrd_list):
        print('The file does not exist')
        wrd_list=input('Enter the location of the wordlist: ')
    if option=='1':
        md5(hash,wrd_list)
    elif option=='2':
        blk2b(hash,wrd_list)
    elif option=='3':
        blk2s(hash,wrd_list)
    elif option=='4':
        sha1(hash,wrd_list)
    elif option=='5':
        sha224(hash,wrd_list)
    elif option=='6':
        sha256(hash,wrd_list)
    elif option=='7':
        sha384(hash,wrd_list)
    elif option=='8':
        sha512(hash,wrd_list)
    elif option=='9':
        sha3384(hash,wrd_list)
    elif option=='10':
        sha3512(hash,wrd_list)
    elif option=='11':
        shk128(hash,wrd_list)
    elif option=='12':
        shk256(hash,wrd_list)
    elif option=='13':
        sys.exit(0)
    else:
        print('\nCoudn\'t crack the password :( ')

#Brute Force Attack
def brt_atc():
    len=int(input("Enter the maximum length of a password in the list: "))
    arr_str=input("Enter the different characters to be used: ")
    arr=[]
    for i in arr_str:
        arr.append(i)
    print(brt_list_gen(arr,len))
def generate(arr,i,s,len):
    if (i==0):
        print(s)
        return
    for j in range(0, len):
        appended = s + arr[j]
        generate(arr, i - 1, appended, len)
    return
def brt_list_gen(arr, len):
    for i in range(1 , len + 1): 
        generate(arr, i, "", len)

#Genrate word list Combination
def comb_word_list(wrd_list):
    word_list=open(wrd_list,'r')
    file_path=os.path.dirname(__file__)
    folder_name='comb_word_lists\\'+str(datetime.datetime.now()).strip(':')
    with open(folder_name,'w') as comb_list:
        for i in word_list:
            for j in word_list:
                x=i.replace('\n','')+j
                comb_list.write(x)
#MD5 
def md5(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        hash2=i.replace('\n','')
        wrd_hash=hashlib.md5(hash2.encode('utf-8')).hexdigest()
        print(wrd_hash)
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            time.sleep(1)
            pass_lst.close()
            exit(0)

#SHA256
def sha256(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i.replace('\n','')
        wrd_hash=str(hashlib.sha256(i.encode('utf-8')).hexdigest())
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)

#SHA512
def sha512(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i.replace('\n','')
        wrd_hash=hashlib.sha512(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)

#SHA1
def sha1(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i.replace('\n','')
        wrd_hash=hashlib.sha1(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            exit(0)

#SHA224
def sha224(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i.replace('\n','')
        wrd_hash=hashlib.sha224(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)

#SHA384
def sha384(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i.replace('\n','')
        wrd_hash=hashlib.sha384(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)

#BLAKE2b
def blk2b(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i.replace('\n','')
        wrd_hash=hashlib.blake2b(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)

#BLAKE2s
def blk2s(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i.replace('\n','')
        wrd_hash=hashlib.blake2s(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)

#SHA3-384
def sha3384(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i.replace('\n','')
        wrd_hash=hashlib.sha3_384(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)

#SHA3-512
def sha3512(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i.replace('\n','')
        wrd_hash=hashlib.sha3_512(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)

#SHA3-256
def sha3256(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i.replace('\n','')
        wrd_hash=hashlib.sha3_256(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)

#SHAKE-128
def shk128(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i.replace('\n','')
        wrd_hash=hashlib.shake_128(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit(0)

#SHAKE-256
def shk256(hash,wrd_list):
    pass_lst=open(wrd_list)
    for i in pass_lst:
        i.replace('\n','')
        wrd_hash=hashlib.shake_256(i.encode('utf-8')).hexdigest()
        if wrd_hash==hash:
            print('The hash has been cracked: ')
            print(i)
            pass_lst.close()
            sys.exit()
def main():
    name_banner()
    selection_screen()
    int_selection()
    print("Couldn't crack it....")
    main()

main()
