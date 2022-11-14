
import random
from flask import Flask, render_template, request
import pandas as pd
import json
app = Flask(__name__)

file_path = r'./k.xls'
df = pd.read_excel(file_path, sheet_name = "Sheet1")

columns = df.shape[0]
print("col"+str(columns))
test = []
for i in range(columns):
    print(i)
    test.append(df.loc[i].values)
    print(test[i])
#     ['索引', '题型', '题目', '选项A', '选项B', '选项C', '选项D', '选项E', '选项F', '答案']
print("")
topic_index = []
topic_index_answer = []
for i in range(5):
    # 随机选择题目
    topic_index = random.sample(range(columns),5)

for i in range(len(topic_index)):

    topic_index_answer.append(test[topic_index[i]][9])

print(topic_index)
print(topic_index[0])
print(test[topic_index[0]][0])
print(topic_index_answer)


# @app.route("/k")
# def listing():
#
# def data(list):
#
'''
'''

'''
import random
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

file_path = r'./k.xls'
df = pd.read_excel(file_path, sheet_name = "Sheet1")
columns = df.shape[0]
topic = []  #题列表
# ['索引', '题型', '题目', '选项A', '选项B', '选项C', '选项D', '选项E', '选项F', '答案']
topic_index_temp = []    #题目索引(出题) 需要+1为题目索引
topic_index_answer = [] #答案
topic_index = []
for i in range(columns):
    topic.append(df.loc[i].values)

for i in range(5):
    # 随机选择题目
    topic_index_temp = random.sample(range(columns),5)

for i in range(len(topic_index_temp)):
    topic_index_answer.append(topic[topic_index_temp[i]][9])
    topic_index.append(topic_index_temp[i] + 1)

print(topic_index_temp)
print(topic_index)
print(topic_index_answer)

def get_topic(topic_index_temp):
    for i in topic_index_temp:
        data = topic[i]
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/knowledge')
def knowledge():
    data = get_topic(topic_index_temp)

    return render_template('knowledge.html', data=data)

if __name__ == '__main__':
    app.run(port=8005)
'''