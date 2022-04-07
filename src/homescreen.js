import { useState, useEffect } from "react"
import axios from 'axios'

export default function Homescreen(){

    const [task, setTask] = useState('')
    const [currenttime, setCurrenttime] = useState('')
    const [result, setResult] = useState('')
    const [enhancetask, setEnhanceTask] = useState('')
    const [enhancecurrenttime, setEnhanceCurrenttime] = useState('')
    const [enhanceresult, setEnhanceResult] = useState('')

    function submit()
    {
        setResult('loading...')
        axios.post('http://127.0.0.1:5000/postdetails',{
            task:task,
            current_time:currenttime
        })
        .then(res=>setResult(res.data.message))
        .catch(err=>setResult(err.message))
    }

    function enhancesubmit()
    {
        setEnhanceResult('loading...')
        axios.post('http://127.0.0.1:5000/postenhancedetails',{
            task:enhancetask,
            current_time:enhancecurrenttime
        })
        .then(res=>setEnhanceResult(res.data.message))
        .catch(err=>{setEnhanceResult(err.message)})
    }


    return(
        <div className="center">
            <div style={{margin:10}}>
                <p> Normal Version </p>
                <input placeholder="Enter the task" onChange={(e)=>setTask(e.target.value)} />
                <input placeholder="Enter the current time" onChange={(e)=>setCurrenttime(e.target.value)}/>
                <p> output - {result ? result : 'None'} </p>
                <div>
                    <p> Task should be in <strong>CALL U2 India 13:00:00 14:30:00  </strong> format </p> 
                    <p> Current time should be in <strong> HH:MM:SS </strong> format  </p>
                </div>
            </div>
            <button onClick={submit}> submit </button>
            <div>
                <p> Enhanced Version </p>
                <input placeholder="Enter the task" onChange={(e)=>setEnhanceTask(e.target.value)}/>
                <input placeholder="Enter the current time" onChange={(e)=>setEnhanceCurrenttime(e.target.value)}/>
                <p> output - {enhanceresult ? enhanceresult : 'None' } </p>
                <p> Task should be in <strong>Email - U1 - India - 13:30:00 14:30:00 Tuesday and Thursday  </strong> format </p> 
                <p> Current time should be in <strong> Weekday HH:MM:SS </strong> format  </p>
            </div>
            <button onClick={enhancesubmit} > submit </button>
        </div>
    )
}