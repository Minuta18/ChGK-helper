import * as React from "react";

import "./roundTag.css";

interface RoundTagProps {
    color: string;
    children: React.ReactNode | React.ReactNode[];
}

export function RoundTag(props: RoundTagProps) {
    return (
        <div className="round-tag" style={{
            backgroundColor: props.color,
        }}>
            { props.children }
        </div>
    );
}
