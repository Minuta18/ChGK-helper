import { useState, useEffect } from 'react';

// https://stackoverflow.com/questions/40885923/countdown-timer-in-react
const Timer = (props) => {
    const initialMinute = Math.floor(props.initialTime / 60);
    const initialSeconds = props.initialTime % 60;
    const [ minutes, setMinutes ] = useState(initialMinute);
    const [seconds, setSeconds] =  useState(initialSeconds);
    useEffect(()=>{
    let myInterval = setInterval(() => {
            if (seconds > 0) {
                setSeconds(seconds - 1);
            }
            if (seconds === 0) {
                if (minutes === 0) {
                    clearInterval(myInterval)
                } else {
                    setMinutes(minutes - 1);
                    setSeconds(59);
                }
            } 
            if (minutes === 0 && seconds === 0) {
                props.onExpired();
            }
        }, 1000)
        return ()=> {
            clearInterval(myInterval);
          };
    });

    return (
        <div className={ 
                (minutes === 0 && seconds < 10) ? 
                'timer-font-red' : 'timer-font' 
        }>
            { minutes === 0 && seconds === 0
                ? '00:00'
                : <> { Math.floor(minutes / 10) }{ minutes % 10 }:
                    { Math.floor(seconds / 10) }{ seconds % 10 }</> 
            }
        </div>
    )
}

export default Timer;
