import * as React from "react";

import * as Tag from "../../tag/index";

import "./question.css";

interface QuestionProps {
    children?: React.ReactNode | React.ReactNode[];
    status?: string;    
    onClick?: () => void;
}

export function Question(props: QuestionProps) {
    return (
        <div className="question" onClick={ props.onClick }>
            <b>{ props.children }</b>
            { (props.status === "ok") ? 
                <Tag.Tag color="var(--tag-green)">ВЕРНО</Tag.Tag> : "" 
            }
            { (props.status === "failed") ? 
                <Tag.Tag color="var(--tag-red)">НЕВЕРНО</Tag.Tag> : "" 
            }
            { (props.status === "skipped") ? 
                <Tag.Tag color="var(--tag-grey)">ПРОПУЩЕНО</Tag.Tag> : "" 
            }
            { (props.status === "process") ?
                <Tag.Tag color="var(--primary-color)">В ПРОЦЕССЕ</Tag.Tag> : ""
            }
        </div>
    );
}
