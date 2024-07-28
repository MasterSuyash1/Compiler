import os

CODES_URI = "codes"

cmd={
    'java' : f'java {CODES_URI}/main.java',
    'py' : f'python3 {CODES_URI}/main.py',
    'js' : f'node {CODES_URI}/main.js',
    'r' : f'Rscript {CODES_URI}/main.r',
    'cpp': f'g++ {CODES_URI}/main.cpp -o {CODES_URI}/main >{CODES_URI}/out.txt 2>{CODES_URI}/err.txt && ./{CODES_URI}/main',
    'c' : f'gcc {CODES_URI}/main.c -o {CODES_URI}/main >{CODES_URI}/out.txt 2>{CODES_URI}/err.txt && ./{CODES_URI}/main'
}

def run(lang,code):
    file = open(f'{CODES_URI}/main.{lang}','w')
    file.write(code)
    file.close()
    exit_code = os.system(f"{cmd[lang]} >{CODES_URI}/out.txt 2>{CODES_URI}/err.txt")
    # print(exit_code)
    if exit_code!=0:
        with open(f"{CODES_URI}/err.txt") as err :
            return {"err" : True, "msg" :err.read()}
    else:
        with open(f"{CODES_URI}/out.txt") as out:
            return out.read()
