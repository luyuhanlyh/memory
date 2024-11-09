from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# 定义纪念日
start_date = datetime(2024, 6, 20, 0, 0, 0)
special_date = datetime(2023, 9, 29, 0, 0, 0)


# 获取相隔天数
def days_between(start, end):
    return (end - start).days


# 获取倒计时（到下一个目标天数或周年的秒数）
def countdown(target_date):
    now = datetime.now()
    if now >= target_date:
        return None
    delta = target_date - now
    return int(delta.total_seconds())


# 获取所有倒计时目标
def get_counts():
    now = datetime.now()

    # 在一起的天数和下一个100天倒计时
    days_together = days_between(start_date, now)
    next_100_days = ((days_together // 100) + 1) * 100
    next_100_days_date = start_date + timedelta(days=next_100_days)

    # 计算下一个周年倒计时
    next_anniversary_number = (days_together // 365) + 1
    next_anniversary_date = start_date.replace(year=start_date.year + next_anniversary_number)

    # 特殊纪念日天数和倒计时
    days_since_special = days_between(special_date, now)
    next_100_special_days = ((days_since_special // 100) + 1) * 100
    next_100_special_date = special_date + timedelta(days=next_100_special_days)
    next_special_anniversary_number = (days_since_special // 365) + 1
    next_special_anniversary_date = special_date.replace(year=special_date.year + next_special_anniversary_number)

    return {
        "days_together": days_together,
        "days_since_special": days_since_special,
        "next_100_days": {
            "days": next_100_days,
            "countdown": countdown(next_100_days_date)
        },
        "next_anniversary": {
            "year": next_anniversary_number,
            "countdown": countdown(next_anniversary_date)
        },
        "next_100_special_days": {
            "days": next_100_special_days,
            "countdown": countdown(next_100_special_date)
        },
        "next_special_anniversary": {
            "year": next_special_anniversary_number,
            "countdown": countdown(next_special_anniversary_date)
        },
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/countdown')
def countdown_api():
    return jsonify(get_counts())


if __name__ == '__main__':
    app.run(host='0.0.0.0')
