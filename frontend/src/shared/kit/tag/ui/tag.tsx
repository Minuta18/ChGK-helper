import * as React from "react";

import "./tag.css";

interface TagProps {
    color: string;
    children: React.ReactNode | React.ReactNode[];
}

export function Tag(props: TagProps) {
    return (
        <div className="tag" style={{
            backgroundColor: props.color,
        }}>
            { props.children }
        </div>
    );
}
