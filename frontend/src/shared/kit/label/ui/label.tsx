import * as React from "react";

import "./label.css"

interface LabelProps {
    children: React.ReactNode | React.ReactNode[];
    htmlFor?: string;
}

export function Label(props: LabelProps) {
    return (
        <label className="c-label" htmlFor={ props.htmlFor }>
            { props.children }
        </label>
    );
}
