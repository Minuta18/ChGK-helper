import * as React from "react";

import "./timer.css";

interface TimerProps {
    length: number;
    length1: number;
    length2: number;
    on_end_func: any;
    on_end1_func: any;
    on_end2_func: any; 
    reset_timer: boolean;
    set_reset_timer: any;
}

export function Timer(props: TimerProps) {
    const [timer, setTimer] = React.useState<number>(props.length);
    const [part, setPart] = React.useState<number>(0);

    React.useEffect(() => {
        setTimeout(() => {
            if (timer > 0) {
                setTimer(timer - 1);
            }
        }, 1000);

        if (part === 0 && timer <= 0) {
            setPart(1);
            setTimer(props.length1);
            props.on_end_func();
        }
        if (part === 1 && timer <= 0) {
            setPart(2);
            setTimer(props.length2);
            props.on_end1_func();
        }
        if (part === 2 && timer <= 0) {
            props.on_end2_func();
            setPart(3);
        }
        if (props.reset_timer) {
            setPart(0);
            setTimer(props.length);
            props.set_reset_timer(false);
        }
    }, [setTimer, timer, setPart, part, props]);

    return <span className={
        timer <= 10 ? "timer timer-red" : "timer timer-default"
    }>
        { Math.floor(Math.floor(timer / 60) / 10) }
        { Math.floor(timer / 60) % 10 }:
        { Math.floor((timer % 60) / 10) }{ (timer % 60) % 10 }
    </span>
}
