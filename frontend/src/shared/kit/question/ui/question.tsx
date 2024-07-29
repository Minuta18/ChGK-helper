import * as React from "react";

import * as Tag from "../../tag/index";

import "./question.css";

interface QuestionProps {
    children?: React.ReactNode | React.ReactNode[];
    status?: string;    
}

export function Question(props: QuestionProps) {
    return (
        <div className="question">
            <b>{ props.children }</b>
            { (props.status === "ok") ? 
                <Tag.Tag color="#61E466">ВЕРНО</Tag.Tag> : "" 
            }
            { (props.status === "mistake") ? 
                <Tag.Tag color="#E46161">НЕВЕРНО</Tag.Tag> : "" 
            }
            { (props.status === "skipped") ? 
                <Tag.Tag color="#CFCFCF">ПРОПУЩЕНО</Tag.Tag> : "" 
            }
        </div>
    );
}
