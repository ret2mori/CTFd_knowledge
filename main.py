'''

'''
import json
import random

from migrations import migrations, create_database, stamp_latest_revision
from flask import Flask, render_template, request
import pandas as pd

# from bottle import request, route, run, static_file


app = Flask(__name__)

file_path = r'./k.xls'
df = pd.read_excel(file_path, sheet_name="Sheet1")
columns = df.shape[0]
topic = []  # 题列表
# ['索引', '题型', '题目', '选项A', '选项B', '选项C', '选项D', '选项E', '选项F', '答案']
topic_index_temp = []  # 题目索引(出题) 需要+1为题目索引
topic_index_answer = []  # 答案
topic_index = []
for i in range(columns):
    topic.append(df.loc[i].values)

for i in range(5):
    # 随机选择题目
    topic_index_temp = random.sample(range(columns), 5)

for i in range(len(topic_index_temp)):
    topic_index_answer.append(topic[topic_index_temp[i]][9])
    topic_index.append(topic_index_temp[i] + 1)

print(topic_index_temp)
print(topic_index)
print(topic_index_answer)


def get_topic(topic_index_temp_):
    data = []
    for i in topic_index_temp_:
        data.append(topic[i])
    return data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/knowledge/<int:num>', methods=['GET'])
def knowledge(num):
    _data = get_topic(topic_index_temp)
    _n = num
    print(_data)
    print(_n)
    return render_template('knowledge.html', data=_data[num], n=_n)


@app.route('/knowledge/test_post', methods=['POST'])
def test_post():
    if request.method == 'POST':
        op_dict = request.json
        print(type(op_dict))
        print("+++++++++" + str(op_dict))


if __name__ == '__main__':
    from models import (
        db,
        Option,
    )

    url = create_database()
    app.config["SQLALCHEMY_DATABASE_URI"] = str(url)

    db.init_app(app)
    migrations.init_app(app, db)
    if url.drivername.startswith("sqlite"):
        db.create_all()
        stamp_latest_revision()
    else:
        # This creates tables instead of db.create_all()
        # Allows migrations to happen properly
        print("upgrade()")

    from models import ma

    ma.init_app(app)

    app.db = db

    app.run(debug=True, port=8005)
