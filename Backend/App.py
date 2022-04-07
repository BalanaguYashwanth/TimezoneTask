import time
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Flask app is running'

@app.route('/postdetails',methods=['POST'])
def postDetails():
    try:
        task = request.json['task']
        timearr=(task).split(" ")
        current_time = request.json['current_time']
        try:
            time1=datetime.strptime(timearr[len(timearr)-2],'%H:%M:%S').time()
            time3=datetime.strptime(timearr[len(timearr)-1],'%H:%M:%S').time()
            time2=datetime.strptime(current_time,'%H:%M:%S').time()
        except Exception as e:
            return jsonify({'message':e})
        else:
            # if time2<time1:
            #     return jsonify({'message': str(time1)})
            # if time2>=time1 and time2<=time3:
            #     return jsonify({'message':"True"})
            # else:
            #     return jsonify({'message':"False"})
            result=verifytime(time1,time2,time3)
            return jsonify({'message':result})
    except Exception as e:
        return jsonify({'message':'Please enter valid input'}),400

@app.route('/postenhancedetails',methods=['POST'])
def postEnhnaceDetails():
    try:   
        task = request.json['task']
        timearr=task.split(" ")
        current_time=request.json['current_time'].split(" ")
        #print(current_time)
        try:
            taskday1 = time.strptime(timearr[len(timearr)-3], "%A").tm_wday
            taskday2 = time.strptime(timearr[len(timearr)-1], "%A").tm_wday
            currentday = time.strptime(current_time[0], "%A").tm_wday

            time1=datetime.strptime(timearr[len(timearr)-5],'%H:%M:%S').time()
            time3=datetime.strptime(timearr[len(timearr)-4],'%H:%M:%S').time()
            time2=datetime.strptime(current_time[1],'%H:%M:%S').time()

        except Exception as e:
            return jsonify({'message':'error'}),400
        else:
            if timearr[len(timearr)-2]=='and':
                print(time2,time1,time3)
                if currentday == taskday1 or currentday == taskday2:
                    if time2>time1 and time2<time3 :
                        day=current_time[0]
                    elif time2 > time3:
                        if current_time[0] == timearr[len(timearr)-3]:
                            day=timearr[len(timearr)-1]
                        if  current_time[0] == timearr[len(timearr)-1]:
                            day=timearr[len(timearr)-3]
                    elif time2<time1:
                        day=current_time[0]
                        
                if currentday> taskday1 and currentday< taskday2:
                    day=timearr[len(timearr)-1]
                  
                if currentday<taskday1 and currentday<taskday2:
                    day=timearr[len(timearr)-3]
                   
                if currentday>taskday1 and currentday > taskday2 :
                    day=timearr[len(timearr)-3]
                   
                result=verifytime(time1,time2,time3)
                if result == 'True':
                    if currentday == taskday1 or currentday == taskday2:
                        return jsonify({'message':"True"})
                    result=timearr[len(timearr)-5]
                    return jsonify({'message':day+' '+result})
                elif result == 'False':
                    result=str(time1)
                    return jsonify({'message':day+' '+result})
                else:
                    return jsonify({'message':day+' '+result})
            else:
                return jsonify({'message':"Currently programmed for and"})
    except Exception as e:
        return jsonify({'message':e}),400


def verifytime(time1,time2,time3):
    if time2<time1:
        return str(time1)
    if time2>=time1 and time2<=time3:
        return "True"
    else:
        return "False"

@app.errorhandler(400)
def bad_request(e):
    return jsonify({'message':'error'})


if __name__ == '__main__':
    app.run(debug=True)
