import React from "react";

import "./iconElement.css";

interface IconElementProps {
    icon?: React.ReactNode;
    children: React.ReactNode[] | React.ReactNode;
}

export function IconElement(props: IconElementProps) {
    return (
        <div className="icon-element">
            <div className="icon-element__icon">
                { props.icon }
            </div>
            { props.children }
        </div>
    );
}
