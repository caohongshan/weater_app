# app.py
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# 假设的 Weather API 端点
WEATHER_API_URL = 'http://apis.juhe.cn/simpleWeather/query'

@app.route('/')
def index():
    # 初始时没有城市和天气数据
    city = None
    weather_data = None
    error = None
    return render_template('index.html', city=city, weather_data=weather_data, error=error)

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    if not city:
        error = '请输入城市名称'
        return render_template('index.html', city=city, weather_data=None, error=error)

    try:
        response = requests.get(f"{WEATHER_API_URL}?city={city}&key=***")
        response.raise_for_status()  # 如果请求失败，抛出异常
        weather_data = response.json()
        return render_template('index.html', city=city, weather_data=weather_data.get('result'), error=None)
    except requests.exceptions.RequestException as e:
        error = str(e)
        return render_template('index.html', city=city, weather_data=None, error=error)

if __name__ == '__main__':
    app.run(debug=True)