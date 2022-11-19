'''
获取用户id
提交答案
user = get_current_user()
print(user.name)
print("-----")
print(user.id)
'''
# noinspection PyUnresolvedReferences
from CTFd.utils.user import get_current_user
from CTFd.models import db
'''
@app.route('/knowledge/test_post', methods=['POST'])
def test_post():
    if request.method == 'POST':
        op_dict = request.json
        print(type(op_dict))
        print("+++++++++" + str(op_dict))

'''
def push():
    db.