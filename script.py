import os, time, sys
from multiprocessing import process
from llamaapi import LlamaAPI

# Initializes the SDK
llama = LlamaAPI("LL-jlvx438CK5iJG638zQ2PzB5wqpAqhoMg5p4g6lrHknwL69TP8eRMgst9Ki4YY1dR")

# Builds the API request
def build_api(message) :
    api_request_json = {
        "model": "mixtral-8x22b-instruct", "messages": [
        {"role": "user", "content": message},
        ],
        "stream": False,
        "max_tokens": 3000,
    }
    return api_request_json

# Gets the initial attack
def get_spectre_v1():
    file_path = "spectre.c"
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Gets the new attack
def get_modified_spectre_v1():
    file_path = "modified_attack.c"
    with open(file_path, 'r') as file:
        content = file.read()
    return content

#Get rid of infinite loops
def modified_code_llama():
    print("modified code llama")
    message = "Without explanation, change the following code by replacing while(1) with while(number of successes < number of characters in the secret) but keep the comments to a minimum: \n:"
    message += get_modified_spectre_v1()
    json_api = build_api(message)
    return llama.run(json_api)

# Executes the request
def code_llama():
    print("Code LLama")
    message = "Without explanation, change the following code to reduce the L1 cache miss rate but keep the comments to a minimum: \n:"
    message += get_spectre_v1()
    json_api = build_api(message)
    return llama.run(json_api)

# Parses through JSON object and extracts only the modified code
def get_attack(response):
    print("Get Attack")
    key = "```"
    with open('temp.txt', 'w') as file:
        file.write(response.json()['choices'][0]['message']['content'])
    with open('temp.txt', 'r') as file:
        all_lines = file.readlines()
    flag = False
    stop = False
    with open('modified_attack.c', 'w') as file2:
        for line in all_lines:
            if key in line and flag: #end of code
                flag = False
                stop = True
            elif key in line and not flag: #beginning of code
                flag = True
            elif flag and not stop:
                file2.write(line)
    #os.remove('temp.txt')
    check = os.system("clang modified_attack.c")
    if check != 0:
        print("Compilation error.")
        code_llama()
    #Check for infinite loops
    filename = 'modified_attack.c'
    check_loop = os.system(f"grep 'while (1)' {filename}")
    if check_loop == 0:
         print("Found infinite loop")
         get_attack(modified_code_llama())
                       
       

# Moves generated attack to CloudShield location
def relocate_attack():
    print("relocating the attack")
    os.system("rmdir CloudShield/attack/ai_modified_Kat/modified_attack.c")
    os.system("mkdir CloudShield/attack/ai_modified_Kat")     
    os.system("mv modified_attack.c CloudShield/attack/ai_modified_Kat")
    mf_contents = '''CC = gcc
CC44 = gcc-4.4
FLAGS = -static -std=c99 -g
FLAGS44 = -static -std=c99 -msse2
    
modified: modified_attack.c
\t$(CC) $(FLAGS) modified_attack.c -o ai_modified_attack

clean:
\trm -f ai_modified_attack'''
    with open('CloudShield/attack/ai_modified_Kat/Makefile', 'w') as file:
        file.write(mf_contents)

# def analysis():
#     os.system("cd CloudShield/attack/ai_modified")
#     t_end = time.time() + 60
#     os.system("./ai_modified_attack")
#     time.sleep(60)
    
#     for i in range(3):
#         os.system("cd ..")
#     os.system("python3 CloudShield/bg_program/run_spec.py")
#     time.sleep(30)
#     os.system("^C")
#     os.system("python3 CloudShield/perf/data_collection.py --core 3 --us 10000 --n_readings 12000")
#     os.system("python3 CloudShield/detector/LSTMAD.py --training --data_dir ../perf/data/webserver/10000us/ --save_model_name AnomalyDetectorMLtrain.ckpt --gpu --Nhidden 256 --LearningRate 1e-2 --Nbatches 100 --RED_points 100")
#     os.system("python3 CloudShield/detector/LSTMAD.py --testing --allanomalyscores --data_dir ../perf/data/webserver/10000us/ --load_model_name AnomalyDetectorMLtrain.ckpt  --gpu --Pvalue_th 1e-5")



def main():
    json_output = code_llama()
    get_attack(json_output)
    relocate_attack()
    # analysis()

if __name__ == "__main__":
    main()
