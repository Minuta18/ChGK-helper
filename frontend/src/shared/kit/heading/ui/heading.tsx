import React from "react";

import "./heading.css";

interface HeadingProps {
    underlined?: boolean;
    children?: React.ReactNode[] | React.ReactNode;
}

export function Heading({ underlined = true, children }: HeadingProps) {
    return (
        <div className={ 
            underlined ? "heading-text underlined-text" :
            "heading-text" 
        }>
            { children }
        </div>
    );
}
