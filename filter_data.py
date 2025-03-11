import json
from tqdm import tqdm#进度条显示

# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_ollama import ChatOllama

# model = ChatOllama(model='llama3.1')
# message = ChatPromptTemplate.from_messages([
#     ("system", "You are an excellent translator. Translate the following text from English to Chinese"),
#     ("human", "{context}:"),
# ])
# translate_chain = message | model | StrOutputParser()

input_file = r'C:\Users\lenovo\Desktop\Safety_Assessment_Path_Planning_modified.json'
output_file = r'C:\Users\lenovo\Desktop\Safety_Assessment_Path_Planning_modified_filter.json'


def should_keep_question(question, answer):
    print('\n')

    # question_translated = translate_chain.invoke({"context":question})
    # answer_translated = translate_chain.invoke({"context":answer})

    print(f"问题: {question}")
    print(f"回答: {answer}")
    # print(f"问题 (中文): {question_translated}")
    # print(f"回答 (中文): {answer_translated}")
    user_input = input("是否保留该问题对？(y/n, enter默认保留): ").strip().lower()
    print('\n')
    
    if user_input == 'n' or user_input == 'N':
        return False
    return True

def process_questions(data):

    with open(output_file, 'a', encoding='utf-8') as outfile:
        for img_data in tqdm(data, desc="image"):
            filtered_data = []
            img_id = img_data.get("img_id")
            qa_list = img_data.get("qa", [])
            
            new_qa_list = []
            print(f"\n处理图片ID: {img_id}")
            
            for qa in qa_list:
                question = qa.get("question")
                if question == "Is this picture taken on Mars?":
                    new_qa_list.append(qa)
                    continue
                answer = qa.get("answer")
                
                if should_keep_question(question, answer):
                    new_qa_list.append(qa)

            filtered_data.append({"img_id": img_id, "qa": new_qa_list})

            outfile.write(json.dumps(filtered_data, ensure_ascii=False) + '\n')
            outfile.flush()
    
    print("处理完成，已保留的数据写入到输出文件中。")

with open(input_file, 'r', encoding='utf-8') as f:
    data = [json.loads(line) for line in f]

process_questions(data[5220:5698])
